import csv
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD
import re

# ==================== NAMESPACES ====================
BASE = Namespace("http://monuments-historiques.fr/resource/")
SCHEMA = Namespace("http://schema.org/")
WGS84 = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
DCTERMS = Namespace("http://purl.org/dc/terms/")
OSM = Namespace("https://www.openstreetmap.org/")

# ==================== FONCTIONS UTILITAIRES ====================

def safe_uri(base_ns, identifier):
    """Crée un URI sûr en nettoyant l'identifiant"""
    clean_id = str(identifier).strip()
    clean_id = re.sub(r'[^\w\-_.]', '_', clean_id)
    clean_id = re.sub(r'_+', '_', clean_id)
    clean_id = clean_id.strip('_')
    
    if not clean_id:
        clean_id = "unknown"
    
    if isinstance(base_ns, Namespace):
        return base_ns[clean_id]
    else:
        return URIRef(str(base_ns) + clean_id)

def parse_coordinates(coord_string):
    """
    Parse une chaîne de coordonnées "lat, lon" 
    Exemple: "48.9729994423037, 5.51115192187422"
    Retourne: (lat, lon) ou (None, None)
    """
    if not coord_string or not isinstance(coord_string, str):
        return None, None
    
    try:
        parts = coord_string.split(',')
        if len(parts) == 2:
            lat = float(parts[0].strip())
            lon = float(parts[1].strip())
            return lat, lon
    except (ValueError, AttributeError):
        pass
    
    return None, None

def clean_value(value):
    """Nettoie une valeur CSV"""
    if not value or not isinstance(value, str):
        return None
    value = value.strip()
    return value if value else None

# ==================== MAPPING SIMPLIFIÉ ====================

def map_csv_to_rdf(row, monument_uri, g):
    """
    Mappe UNIQUEMENT les colonnes essentielles (comme votre camarade)
    
    Colonnes mappées:
    - Type → schema:category
    - Nom → schema:name
    - Commune → schema:addressLocality
    - Département → dbo:department
    - Région → schema:addressRegion
    - OSM Point → wgs84:lat + wgs84:long
    - OSM Id → osm:osmId
    - OSM URL → schema:url
    - OSM Date mise à jour → dcterms:modified
    """
    
    # ===== TYPE (memorial, castle, etc.) =====
    monument_type = clean_value(row.get("Type"))
    if monument_type:
        type_uri = safe_uri(SCHEMA, monument_type)
        g.add((monument_uri, SCHEMA.category, type_uri))
    
    # ===== NOM =====
    nom = clean_value(row.get("Nom"))
    if nom:
        g.add((monument_uri, SCHEMA.name, Literal(nom)))
    
    # ===== COMMUNE =====
    commune = clean_value(row.get("Commune"))
    if commune:
        g.add((monument_uri, SCHEMA.addressLocality, Literal(commune)))
    
    # ===== DÉPARTEMENT =====
    departement = clean_value(row.get("Département"))
    if departement:
        g.add((monument_uri, SCHEMA.department, Literal(departement)))
    
    # ===== RÉGION =====
    region = clean_value(row.get("Région"))
    if region:
        g.add((monument_uri, SCHEMA.addressRegion, Literal(region)))
    
    # ===== COORDONNÉES GPS =====
    osm_point = clean_value(row.get("OSM Point"))
    if osm_point:
        lat, lon = parse_coordinates(osm_point)
        if lat is not None and lon is not None:
            g.add((monument_uri, WGS84.lat, Literal(lat, datatype=XSD.decimal)))
            g.add((monument_uri, WGS84.long, Literal(lon, datatype=XSD.decimal)))
    
    # ===== OSM ID =====
    osm_id = clean_value(row.get("OSM Id"))
    if osm_id:
        g.add((monument_uri, OSM.osmId, Literal(osm_id)))
    
    # ===== OSM URL =====
    osm_url = clean_value(row.get("OSM URL"))
    if osm_url:
        g.add((monument_uri, SCHEMA.url, URIRef(osm_url)))
    
    # ===== OSM DATE MISE À JOUR =====
    osm_date = clean_value(row.get("OSM Date mise à jour"))
    if osm_date:
        g.add((monument_uri, DCTERMS.modified, Literal(osm_date, datatype=XSD.date)))

# ==================== CRÉATION DU GRAPHE ====================

def convert_csv_to_rdf(csv_file, output_file="monuments_historiques.ttl", limit=None):
    """
    Convertit le CSV des monuments historiques en RDF/Turtle
    VERSION SIMPLIFIÉE - Colonnes essentielles uniquement
    
    Args:
        csv_file: Chemin vers le fichier CSV
        output_file: Nom du fichier de sortie
        limit: Nombre max de lignes à traiter (None = tout)
    """
    g = Graph()
    
    # Déclaration des namespaces
    g.bind("monuments", BASE)
    g.bind("schema", SCHEMA)
    g.bind("wgs84", WGS84)
    g.bind("dcterms", DCTERMS)
    g.bind("osm", OSM)
    
    print(f"📖 Lecture du fichier CSV: {csv_file}")
    print(f"📋 Colonnes mappées: Type, Nom, Commune, Département, Région, OSM Point, OSM Id, OSM URL, OSM Date\n")
    
    errors_count = 0
    success_count = 0
    
    # IMPORTANT: Délimiteur point-virgule
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';')
        
        for idx, row in enumerate(reader, 1):
            # Limite optionnelle pour tests
            if limit and idx > limit:
                break
            
            if idx % 5000 == 0:
                print(f"  ✓ {idx} monuments traités... ({success_count} succès, {errors_count} erreurs)")
            
            try:
                # ===== CRÉER L'URI DU MONUMENT =====
                osm_id = clean_value(row.get("OSM Id"))
                if osm_id:
                    monument_id = f"osm_{osm_id}"
                else:
                    monument_id = f"monument_{idx}"
                
                monument_uri = safe_uri(BASE, monument_id)
                
                # ===== TYPE DE BASE =====
                g.add((monument_uri, RDF.type, SCHEMA.Place))
                
                # ===== MAPPER LES COLONNES ESSENTIELLES =====
                map_csv_to_rdf(row, monument_uri, g)
                
                success_count += 1
                
            except Exception as e:
                errors_count += 1
                if errors_count <= 5:
                    print(f"  ⚠️  Erreur ligne {idx}: {str(e)[:100]}")
    
    # ===== SÉRIALISATION =====
    print(f"\n💾 Génération du fichier Turtle: {output_file}")
    g.serialize(destination=output_file, format="turtle")
    
    print(f"\n✅ Fichier généré avec succès!")
    print(f"📊 Statistiques:")
    print(f"   • {success_count} monuments traités")
    print(f"   • {len(g)} triplets RDF créés")
    if errors_count > 0:
        print(f"   ⚠️  {errors_count} erreurs ignorées")
    
    return g

# ==================== EXÉCUTION ====================

if __name__ == "__main__":
    print("🏛️  Conversion monuments historiques OSM → RDF (VERSION SIMPLIFIÉE)\n")
    print("=" * 80)
    
    # Traiter tout le fichier (ou mettre une limite pour tester)
    graph = convert_csv_to_rdf(
        csv_file="osm-france-historic.csv",
        output_file="monuments_historiques.ttl",
        limit=None  # None = tout le fichier
    )
    
    
    print("\n💡 Pour charger dans Fuseki:")
    print("   1. Lancez Fuseki: ./fuseki-server")
    print("   2. Accédez à http://localhost:3030")
    print("   3. Créez un dataset 'monuments'")
    print("   4. Uploadez monuments_historiques.ttl")
    print("   5. Testez les requêtes ci-dessus!")