# Diabète Intelligent

Application web de prédiction du risque de diabète à partir d'un modèle de Machine Learning. L'utilisateur renseigne quelques informations de santé (âge, sexe, IMC, taux d'HbA1c, glycémie, etc.) et l'application estime s'il présente un risque de diabète.

Projet universitaire réalisé en groupe (4 personnes) à La Rochelle Université.

## Fonctionnalités

- Formulaire web de saisie des données de santé
- Affichage du résultat de la prédiction
- Modèle de Machine Learning entraîné sur un jeu de 100 000 dossiers patients

## Démarche data

- Nettoyage du jeu de données : suppression des doublons, traitement des valeurs aberrantes (méthode IQR), filtrage des âges incohérents
- Analyse exploratoire des données (EDA) avec Pandas et Seaborn : les variables les plus liées au diabète sont le taux d'HbA1c et la glycémie
- Encodage des variables catégorielles (one-hot) et normalisation (MinMax)
- Traitement du déséquilibre des classes (seulement 8,5 % de cas positifs)
- Modèle : régression logistique (Scikit-learn)

## Technologies

- **Front-end** : HTML, CSS, JavaScript
- **Back-end** : Python, Flask
- **Machine Learning** : Pandas, Seaborn, Scikit-learn

## Structure du projet

- `EDA.ipynb` — exploration et visualisation des données
- `Diabetesintelligente.ipynb` — préparation des données et modèle
- `ajustement_diabete/` — application Flask (interface web et intégration du modèle)
- `diabetes_prediction_dataset.csv` — jeu de données
- `requirements.txt` — dépendances Python

## Installation et lancement

```
git clone https://github.com/Ghiles-bia16/diabete_intelligent.git
cd diabete_intelligent
pip install -r requirements.txt
```

Puis lancer l'application Flask et ouvrir le lien affiché dans le terminal.

## Crédits

- [Yassine Oussama](https://github.com/oussamazzz)
- [Bia Ghiles](https://github.com/Ghiles-bia16)
- [Gokmen Ilhan](https://github.com/Igokmen)
- Khelf Massinissa
