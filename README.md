# Web-Semantique
Projet de groupe sur la matiere Web semantique

soit le DATA set  utilisé :

https://public.opendatasoft.com/explore/assets/osm-france-historic/


Comment l'utiliser  :
1. telecharger le DataSet au format csv 
2. telecharger le programme python et installer la lib : pip install rdflib
3. executer le fichier (csv et prog python dans le meme rep) : python rdf_converter_fixed.py
4. attendez...
5. un fichier turtle d'environ 100 mb est generé : monuments_historiques.ttl

6. utiliser fuseki server pour l'importer
  lien : https://jena.apache.org/download/
  revoir TP1 pour utilisation
7. Accédez à http://localhost:3030
8. creer un DataSet monument et importez en fichier le fichier turtle
9. attendez...
10. faites des requetes SPARQL dessus
