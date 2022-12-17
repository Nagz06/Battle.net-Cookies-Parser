import os

# Définissez le dossier à analyser | Set the folder to scan
dossier = input('Single Cookies Folder Path : ')

# Définissez la chaîne à rechercher | Define the string to search
chaine = '-tassadar'

# Ouvrez un fichier texte pour écrire les résultats | Open a text file to write the results
with open('resultats.txt', 'w') as f:
  # Parcourez tous les fichiers texte dans le dossier | Browse all text files in the folder
  for nom_fichier in os.listdir(dossier):
    # Ignorez les fichiers qui ne sont pas des fichiers texte | Ignore files that are not text files
    if not nom_fichier.endswith('.txt'):
      continue
    # Ouvrez le fichier texte | Open the text file
    with open(os.path.join(dossier, nom_fichier), 'r') as fichier:
      # Parcourez toutes les lignes du fichier | Go through all the lines in the file
      for ligne in fichier:
        # Vérifiez si la chaîne est présente dans la ligne | Check if the string is present in the line
        if chaine in ligne:
          # Découpez la ligne en utilisant la tabulation comme séparateur | Cut the line using the tab as a separator
          valeurs = ligne.split("\t")
          # Récupérez la sixième valeur | Get the sixth value
          cook = valeurs[6]
          # Écrivez la sixième  valeur dans le fichier de résultats | Write the sixth value to the result file
          f.write(cook + "\n")
