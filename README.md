# Web Sémantique
Projet de groupe sur la matière Web Sémantique

## Dataset utilisé

**Lien :** [Dataset Monuments Historiques Français](https://public.opendatasoft.com/explore/assets/osm-france-historic/)

---

## Tuto d'installation

### 📦 Récupération et traitement du dataset

#### 1. Téléchargez le dataset au format CSV

<img width="1919" height="1040" alt="dataset" src="https://github.com/user-attachments/assets/49936f19-4b05-473e-b497-44e290d7150e" />
<img width="1920" height="1040" alt="dataset" src="https://github.com/user-attachments/assets/f2cf3d83-e25a-4104-b6ee-e05e01c8f5e0" />

#### 2. Installez la librairie RDFLib

**Commande :**
```bash
pip install rdflib
```

<img width="1324" height="295" alt="install lib" src="https://github.com/user-attachments/assets/8f624424-362d-4f7b-a375-6234f5926b52" />

#### 3. Téléchargez le programme Python

Téléchargez le fichier `rdf_converter_fixed.py` présent sur le dépôt Git.

#### 4. Exécutez le programme Python

⚠️ **Important :** Bien référencer les chemins du programme et du dataset.

**Commande :**
```bash
python rdf_converter_fixed.py osm-france-historic.csv
```

**Temps d'attente :** Entre 10s et 1 min selon la puissance de l'ordinateur.

Si tout se passe comme prévu, vous devriez avoir une fenêtre de ce type :

<img width="1034" height="1080" alt="exec python" src="https://github.com/user-attachments/assets/13757b4c-8497-4e68-a8cf-c9e558354399" />

#### 5. Vérification du fichier généré

Un fichier Turtle d'environ 100 Mo devrait être généré : `monuments_historiques.ttl`

<img width="996" height="482" alt="fichier ttl" src="https://github.com/user-attachments/assets/6186f8cb-99db-4f71-80b0-ecd2ab17feab" />

---

### 🚀 Usage du dataset avec Fuseki

#### 6. Installez Fuseki

**Lien :** [Téléchargement Fuseki](https://jena.apache.org/download/)

<img width="1920" height="1040" alt="fichier ttl" src="https://github.com/user-attachments/assets/ce84bcf1-97f7-4fbb-9375-425dfdd7757a" />

#### 7. Exécutez le serveur Fuseki

⚠️ **Important :** Bien référencer le chemin du programme.

**Commande :**
```bash
./fuseki-server
```

Vous devriez avoir une fenêtre de ce type :

<img width="1382" height="447" alt="exec Fuseki" src="https://github.com/user-attachments/assets/db7ba3ce-46e6-4137-a691-945512bc0a18" />

#### 8. Accédez à l'interface Fuseki

Ouvrez votre navigateur et accédez à : **http://localhost:3030**

*(Pour plus d'explications sur le fonctionnement de Fuseki, revoir le TP1)*

Vous devriez arriver sur cette fenêtre (sinon, cliquez sur `Datasets` ou `Manage` en haut) :

<img width="960" height="516" alt="fuseki" src="https://github.com/user-attachments/assets/fad3f120-9103-4a71-b67b-0075e90c004a" />

#### 9. Créez un nouveau dataset

Cliquez sur `add one` :

<img width="960" height="516" alt="fuseki" src="https://github.com/user-attachments/assets/effb799b-6c3a-423e-8eca-f0510ab39154" />

Vous devriez arriver sur cette fenêtre :

<img width="960" height="516" alt="image" src="https://github.com/user-attachments/assets/7e71fdeb-5ad0-498f-9f14-e992d58294ff" />

**Instructions :**
- Donnez un nom au dataset (par exemple `monuments`)
- Choisissez l'un des 2 modes de stockage des données
- Cliquez sur le bouton `create dataset`

Vous devriez arriver sur une fenêtre de ce genre :

<img width="1248" height="565" alt="fuseki" src="https://github.com/user-attachments/assets/496583fe-9555-4f55-9e6b-97e235feea48" />

#### 10. Importez les données

Cliquez sur `add data`. Vous devriez arriver sur cette page :

<img width="1248" height="706" alt="fuseki" src="https://github.com/user-attachments/assets/93383e14-d7a3-492e-b770-b787d90fcc45" />

**Instructions :**
1. Donnez un nom commençant par `http://` (par exemple `http://monuments`)
2. Cliquez sur `select files` et sélectionnez le fichier `monuments_historiques.ttl` généré précédemment
3. Cliquez sur `upload all` et attendez (entre 10s et 30s selon votre ordinateur)

Si tout fonctionne, vous devriez avoir une fenêtre de ce type :

<img width="1248" height="765" alt="fuseki" src="https://github.com/user-attachments/assets/e838acb7-3eee-486f-8afc-83563f7a01db" />

#### 11. Effectuez vos requêtes SPARQL

Rendez-vous sur `Query` en haut à gauche.

Vous devriez arriver sur une fenêtre de ce type et pouvoir commencer vos requêtes :

<img width="1248" height="921" alt="fuseki" src="https://github.com/user-attachments/assets/85b75900-08ca-46a9-8b61-72c86f829f6c" />

---

## 📝 Exemple de requête SPARQL

```sparql
PREFIX schema: <http://schema.org/>
PREFIX wgs84: <http://www.w3.org/2003/01/geo/wgs84_pos#>

SELECT ?monument ?nom ?lat ?long
WHERE {
    ?monument a schema:Place ;
              schema:name ?nom ;
              wgs84:lat ?lat ;
              wgs84:long ?long .
}
LIMIT 10
```

---

## 🛠️ Prérequis

- Python 3.x
- Java (pour Fuseki)
- Navigateur web

## 📚 Ressources

- [Documentation RDFLib](https://rdflib.readthedocs.io/)
- [Documentation Apache Jena Fuseki](https://jena.apache.org/documentation/fuseki2/)
- [SPARQL Tutorial](https://www.w3.org/TR/sparql11-query/)
