# Web-Semantique
Projet de groupe sur la matiere Web semantique

soit le DATA set utilisé :

Lien : [DataSet Monuments Historiques Français](https://public.opendatasoft.com/explore/assets/osm-france-historic/)

## Tuto d'installation :

### Récuperation et traitement du DataSet 

1. Telechargez le DataSet au format csv
<img width="1919" height="1040" alt="dataset" src="https://github.com/user-attachments/assets/49936f19-4b05-473e-b497-44e290d7150e" />
<img width="1920" height="1040" alt="dataset" src="https://github.com/user-attachments/assets/f2cf3d83-e25a-4104-b6ee-e05e01c8f5e0" />

2. Installez la librairie RDFLIB
   Commande : `pip install rdflib`
   <img width="1324" height="295" alt="install lib" src="https://github.com/user-attachments/assets/8f624424-362d-4f7b-a375-6234f5926b52" />

3. Téléchargez le programme python présent sur le Git

4. executez le programme python (⚠ Bien référencer les chemins du programme et du Dataset)
   Commande : `python .\rdf_converter_fixed.py .\osm-france-historic.csv `

   attendez... (Entre 10s et 1 min selon la puissance de l'ordinateur)
   
   Si tout ce passe comme prévu vous devriez avoir une fenêtre de ce type là :
<img width="1034" height="1080" alt="exec python" src="https://github.com/user-attachments/assets/13757b4c-8497-4e68-a8cf-c9e558354399" />

5. un fichier turtle d'environ 100 mb devrait être generé : monuments_historiques.ttl
<img width="996" height="482" alt="fichier ttl" src="https://github.com/user-attachments/assets/6186f8cb-99db-4f71-80b0-ecd2ab17feab" />


### Usage du DataSet ave Fuseki

6. Installer Fuseki

Lien : [Executable Fuseki Téléchargement]([https://public.opendatasoft.com/explore/assets/osm-france-historic/](https://jena.apache.org/download/))
<img width="1920" height="1040" alt="fichier ttl" src="https://github.com/user-attachments/assets/ce84bcf1-97f7-4fbb-9375-425dfdd7757a" />

7. Executez le serveur Fuseki (⚠ Bien référencer les chemins du programme)
   Commande : `.\fuseki-server`
   Vous devriez avoir une fenêtre de ce type là :
   <img width="1382" height="447" alt="exec Fuseki" src="https://github.com/user-attachments/assets/db7ba3ce-46e6-4137-a691-945512bc0a18" />

9. Accédez à http://localhost:3030 sur votre navigateur (Pour plus d'explication sur le fonctionnement de Fuseki revoir TP1)
   Vous devriez arriver sur cette fenêtre (Sinon cliquer sur `DataSets` ou `Manage en haut`):
   <img width="960" height="516" alt="fuseki" src="https://github.com/user-attachments/assets/fad3f120-9103-4a71-b67b-0075e90c004a" />

10. Cliquez sur `add one`
   <img width="960" height="516" alt="fuseki" src="https://github.com/user-attachments/assets/effb799b-6c3a-423e-8eca-f0510ab39154" />
   Vous devriez arriver sur cette fenêtre :
   <img width="960" height="516" alt="image" src="https://github.com/user-attachments/assets/7e71fdeb-5ad0-498f-9f14-e992d58294ff" />
   Donner un nom au Dataset (par exemple monuments).
   Choisissez l'un des 2 modes de stockage des données.
   Enfin, cliquez sur le bouton `create dataset`.
   Vous devriez arriver sur une fenêtre de ce genre :
   <img width="1248" height="565" alt="fuseki" src="https://github.com/user-attachments/assets/496583fe-9555-4f55-9e6b-97e235feea48" />
   

12. Cliquez sur `add data`
    Vous devriez arriver sur cette page :
    <img width="1248" height="706" alt="fuseki" src="https://github.com/user-attachments/assets/93383e14-d7a3-492e-b770-b787d90fcc45" />
    De là, donnez un nom commencer par `http://` (par exemple `http://monuments`).
    Ensuite cliquez sur `select files` et prenez le fichier `monuments_historiques.ttl` généré dans la première section du tuto.
    Enfin cliquez sur `upload all` et attendez (Entre 10s et 30s selon la vitesse de votre ordinateur).
    Normalement si tout fonctionne vous devriez avoir une fenêtre de ce type :
    <img width="1248" height="765" alt="fuseki" src="https://github.com/user-attachments/assets/e838acb7-3eee-486f-8afc-83563f7a01db" />

13. Vous pouvez commencer les requêtes.
Rendez vous sur `Query` un peu plus haut sur la gauche.
Vous devriez arriver sur une fenêtre de ce type et pouvoir commencer les requêtes :
<img width="1248" height="921" alt="fuseki" src="https://github.com/user-attachments/assets/85b75900-08ca-46a9-8b61-72c86f829f6c" />

