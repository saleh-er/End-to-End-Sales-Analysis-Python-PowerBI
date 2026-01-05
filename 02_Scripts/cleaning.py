import pandas as pd
import os

# Chemins des fichiers
input_path = '../01_Data/sales_data_sample.csv'
output_path = '../01_Data/sales_data_clean.csv'

def clean_data():
    if not os.path.exists(input_path):
        print(f"Erreur : Placez le fichier dans {input_path}")
        return

    # 1. Chargement avec l'encodage correct pour ce dataset
    df = pd.read_csv(input_path, encoding='Latin-1')
    print("✅ Données chargées.")

    # 2. Sélection des colonnes stratégiques
    cols = ['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'ORDERDATE', 
            'PRODUCTLINE', 'CITY', 'COUNTRY', 'DEALSIZE']
    df = df[cols]

    # 3. Conversion de la date
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

    # 4. Création du Chiffre d'Affaires (Sales)
    df['TOTAL_SALES'] = df['QUANTITYORDERED'] * df['PRICEEACH']

    # 5. Export
    df.to_csv(output_path, index=False)
    print(f"✅ Nettoyage terminé. Fichier créé : {output_path}")

if __name__ == "__main__":
    clean_data()