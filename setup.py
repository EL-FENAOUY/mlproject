
# setup.py est un fichier de configuration utilisé pour rendre votre projet Python installable et distribuable.

from setuptools import setup, find_packages

from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements




setup(
    name='mlproject',  # Nom du projet
    version='0.0.1',  # Version du projet
    description='',  # Brève description du projet
    author='elfenaouy',  # Nom de l'auteur
    author_email='elfenaouyreda@gmail.com',  # Adresse email de l'auteur
    url='',  # URL du dépôt du projet
    packages=find_packages(),  # Inclut toutes les sous-packages dans le dossier src
    install_requires = get_requirements('requirements.txt'),
    
    python_requires= '>=3.7'  # Version minimale de Python requise
)
