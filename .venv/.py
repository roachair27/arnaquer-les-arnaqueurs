import os

# Dossier à analyser
base_path = "C:/Users/HP/Desktop/Scam"

# Taille limite (en Mo)
size_limit = 10  # Mo

print(f"📁 Fichiers > {size_limit} Mo dans {base_path} :\n")

for folder, _, files in os.walk(base_path):
    for f in files:
        path = os.path.join(folder, f)
        size_mb = os.path.getsize(path) / (1024 * 1024)
        if size_mb > size_limit:
            print(f"{path} - {round(size_mb, 2)} Mo")
