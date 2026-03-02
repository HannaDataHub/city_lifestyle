# City lifestyle

## Présentation du projet
Ce projet a pour but de simuler un projet collaboratif en travaillant sur un reposity Github commun.
Il s'agit d'un travail en duo ou trio où chacun utilise Git pour gérer le développement à travers des branches et des fusions vers la branche principale.

Chaque membre du groupe doit développer une branche dédiée à une méthode de réduction de dimension (méthodes : PCA, t-SNE et UMAP).

- délais : 3 heures et 30 minutes,
- membres dans le groupe : 2 personnes,
- rendu : lien Github et lien DockerHub.


## Présentation de la base de données
### Descriptif
Ce jeu de données modélise différents profils de ville à l’échelle mondiale afin d’explorer les modes de vie en ville à travers des méthodes d’apprentissage automatique non supervisé. Il met en évidence l’impact du niveau de revenu, de la pollution, des infrastructures numériques et des facteurs environnementaux sur le bien-être, en comparant des contextes variés allant des mégapoles densément peuplées aux petites villes à orientation écologique.

### Caractéristiques
- Taille : 300 lignes x 10 colonnes
- 300 villes
- 10 variables représentant des dimensions sociales, économiques et environnementales
- Aucune valeur manquante

### Structure
| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `city_name` | string | - | Unique synthetic city identifier |
| `country` | string | 6 regions | Geographic region (Europe, Asia, North America, South America, Africa, Oceania) |
| `population_density` | int | 100 - 25,000 | Population per km² |
| `avg_income` | float | 300 - 7,000 | Average monthly household income (USD) |
| `internet_penetration` | float | 30 - 100 | Percentage of households with internet access |
| `avg_rent` | float | 150 - 3,000 | Average monthly apartment rent (USD) |
| `air_quality_index` | int | 20 - 180 | Air Quality Index (lower = cleaner air) |
| `public_transport_score` | float | 10 - 95 | Quality of public transportation (0-100 scale) |
| `happiness_score` | float | 2 - 9 | Subjective life satisfaction (0-10 scale) |
| `green_space_ratio` | float | 2 - 60 | Percentage of city area covered by parks/green spaces |



## Organisation de travail du groupe
### 1- Création du repository commun 
Dans cette étape, nous avons d'abord créer un repository sur Github. Puis nous avons chacune, cloner le repository en local pour travailler chacune sur une méthode de réductions de dimension.


### 2- Création des branches et développement des méthodes 
Ici, une membre du groupe à décider de travailler sur la méthode t-SNE et la seconde de prendre la méthode PCA. Chacune a créé un environnement virtuel et un notebook. 


### 3- Push de chaque membre et fusion dans la main 
A la fin de l'étape, chacune a fait un git push dans sa branche respective, avec un notebook et une sortie.
Ensuite, chacune des membres du groupe on fais la fusion vers la branche principale.


### 4- Comparaison et Docker 
Après la fusion vers la branche principale, une membre du groupe a fait la comparaison des deux méthodes. Pour cela, nous avons créé une application en python, mais deployée avec Docker.
L'autre en anticipation, a écrit le README (que vous êtes en train de lire!).


code pour le docker: 
Tester en local
1. docker build -t app_trust .   -créer l'image
2. docker run -p 8501:8501 app_trust  -deployer en local

Pusher image sur Dockerhub
1. docker tag app_trust username/app_trust:v0- tager une image
2. docker push username/app_trust:v0



## Publication 
Vous pouvez télécharger l'image via ce lien : 
https://hub.docker.com/r/hannasva/app_trust/tags