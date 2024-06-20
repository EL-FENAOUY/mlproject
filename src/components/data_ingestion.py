"""
Module de gestion de l'ingestion des données.

Ce module utilise la Programmation Orientée Objet (POO) pour structurer
le processus d'ingestion des données. Il permet de lire un fichier CSV,
de diviser les données en ensembles d'entraînement et de test, et de
sauvegarder ces ensembles dans des fichiers séparés.
"""


import os 
import sys

import pandas as pd

from src.exception import CustomException

from src.logger import logging



from sklearn.model_selection import train_test_split

from dataclasses import dataclass



#############################################################################################
############################      Approche simple   #########################################
#############################################################################################

""""
import os
import pandas as pd
from sklearn.model_selection import train_test_split

def ingest_data(input_path, output_dir):
    try:
        df = pd.read_csv(input_path)
        os.makedirs(output_dir, exist_ok=True)
        train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
        df.to_csv(os.path.join(output_dir, 'data.csv'), index=False)
        train_set.to_csv(os.path.join(output_dir, 'train.csv'), index=False)
        test_set.to_csv(os.path.join(output_dir, 'test.csv'), index=False)
        print("Data ingestion completed successfully.")
    except Exception as e:
        print(f"Error during data ingestion: {e}")

# Utilisation
ingest_data('notebook/data/stud.csv', 'artifacts')






"""
@dataclass
class DataIngestionConfig:
    """
    Configuration pour l'ingestion des données.

    Attributes:
        train_data_path (str): Chemin du fichier de données d'entraînement.
        test_data_path (str): Chemin du fichier de données de test.
        raw_data_path (str): Chemin du fichier de données brutes.
    """
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    """
    Classe pour gérer l'ingestion des données.
    """

    def __init__(self):
        """
        Initialisation de la configuration d'ingestion.
        """
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Méthode pour initier le processus d'ingestion des données.

        Lit les données à partir d'un fichier CSV, divise les données en
        ensembles d'entraînement et de test, et sauvegarde ces ensembles
        dans des fichiers séparés.

        Returns:
            tuple: Chemins des fichiers de données d'entraînement et de test.

        Raises:
            CustomException: Si une erreur se produit lors de l'ingestion des données.
        """
        logging.info("Entered the data ingestion method or component")

        try:
            # Lecture du fichier CSV contenant les données
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            # Création des répertoires si nécessaire
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Sauvegarde des données brutes
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train-test split initiated')

            # Division des données en ensembles d'entraînement et de test
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Sauvegarde des ensembles d'entraînement et de test
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            # Retour des chemins des fichiers de données
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            # Gestion des exceptions et levée d'une exception personnalisée
            raise CustomException(e, sys)
        


# Exemple d'utilisation
if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()
    print(f"Data ingestion completed. Train data path: {train_path}, Test data path: {test_path}")