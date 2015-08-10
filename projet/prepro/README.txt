#### A PROPOS

Cette commande nous permet de créer une base de connaissance à partir des termes présent dans le fichier xml correspondant à un corpus QUALD donnée en paramètres.



#### Utilisation


Lancer la commande "python prepro.py [input_file_path]"

Output : 


./output/phrases.txt : contient l'ensemble des phrases (dans le sens 'termes extrait') du document

./output/data.txt : contient les lignes extraites par le document xml d'origine.

./output/ressources1.txt : contient l'ensemble des ressources que nous allons utiliser pour créer la feature ressourceType.

./output/quest-XX.txt : contient l'ensemble des questions en language naturelle extraite pour la langue XX

./output/ressourceType : contient l'ensemble des variables créée pour la feature ressourceType.



