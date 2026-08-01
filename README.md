# G2G 2FA Generator

Génère les codes 2FA (TOTP) en direct pour des comptes achetés sur G2G, à partir du fichier CSV fourni par le vendeur.

Aucune dépendance externe : uniquement Python standard (pas de `pip install` nécessaire).

## Comment ça marche

1. Tu déposes le(s) fichier(s) CSV d'export G2G dans ce dossier.
2. Le script lit chaque CSV, récupère le nom du compte, le mot de passe et la clé secrète 2FA.
3. Il affiche un tableau qui se met à jour tout seul avec le code à 6 chiffres actuel de chaque compte (le code change toutes les 30 secondes, comme sur Google Authenticator).

## Installation (pour débutant complet)

### 1. Installer Python

Le script a besoin de Python pour fonctionner (c'est comme un moteur qui fait tourner le programme).

1. Va sur https://www.python.org/downloads/
2. Clique sur le gros bouton jaune "Download Python" (ça télécharge la dernière version).
3. Lance le fichier `.exe` téléchargé.
4. **Important** : sur le premier écran de l'installateur, coche la case en bas **"Add python.exe to PATH"** avant de cliquer sur "Install Now". Si tu oublies cette case, le script ne fonctionnera pas.
5. Laisse l'installation se terminer, puis ferme la fenêtre.

Pour vérifier que Python est bien installé : ouvre l'invite de commande (touche Windows, tape `cmd`, entrée), puis tape :

```
python --version
```

Si ça affiche un numéro de version (ex: `Python 3.12.4`), c'est bon.

### 2. Télécharger ce projet

1. Sur cette page GitHub, clique sur le bouton vert **"Code"** puis **"Download ZIP"**.
2. Décompresse le ZIP où tu veux sur ton PC (clic droit → "Extraire tout").

### 3. Ajouter ton fichier CSV

Copie le fichier CSV que le vendeur G2G t'a donné dans le même dossier que `a2f.py`.

### 4. Lancer l'outil

Double-clique simplement sur **`lancer.bat`**.

Une fenêtre noire s'ouvre et affiche la liste de tes comptes avec leur code 2FA actuel, qui se rafraîchit automatiquement. Pour quitter, ferme la fenêtre ou fais `Ctrl + C`.

## Format du CSV attendu

Le script reconnaît le format d'export standard G2G, avec le nom d'utilisateur en colonne 2 et la clé secrète TOTP au début de la colonne "Remark" (avant le `:`).

## Sécurité

- Les fichiers `.csv` ne sont **jamais** envoyés sur GitHub (voir `.gitignore`) — ils contiennent des mots de passe, ils restent uniquement sur ton PC.
- Ne partage jamais ton dossier avec les CSV dedans.
