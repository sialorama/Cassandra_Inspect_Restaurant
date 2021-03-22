# Cassandra_Inspect_Restaurant
Deux Clusters Cassandra sur Docker et une API Falsk.

## Présentation du projet:

Nous avons préparé un docker-compose qui nous a permis de déployer un cluster Cassandra avec 2 noyaux. Nous avons grace à un fichier Docker-compose pu créer un volume pour garantir la persistance des données.

Après cela nous avons créé la base de données sur le volume du premier cluster et importé les données csv.

Nous avos également créer une API qui propose 4 url pour accéder :

    - Aux infos d'un restaurant à partir de son id,
    - A la liste des noms de restaurants à partir du type de cuisine,
    - Au nombre d'inspection d'un restaurant à partir de son id restaurant,
    - Les noms des 10 premiers restaurants d'un grade donné.

Nous avons également réalisé une page html pour facilité l'accès à ces requetes.
