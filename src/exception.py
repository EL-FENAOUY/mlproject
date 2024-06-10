import sys
from src.logger import logging  # Supposons que `logging` soit correctement configuré dans ce module

def error_message_detail(error, error_detail: sys):
    """
    Retourne un message d'erreur détaillé incluant le nom du fichier, le numéro de ligne et le message d'erreur.
    
    Parameters:
    error (Exception): L'exception qui s'est produite.
    error_detail (sys): L'objet sys, utilisé pour obtenir des informations détaillées sur l'exception.
    
    Returns:
    str: Un message d'erreur formaté.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    """
    Exception personnalisée pour inclure des détails supplémentaires sur l'erreur.
    
    Attributes:
    error_message (str): Le message d'erreur détaillé.
    """
    
    def __init__(self, error_message, error_detail: sys):
        """
        Initialise CustomException avec un message d'erreur et des détails sur l'erreur.
        
        Parameters:
        error_message (str): Le message d'erreur initial.
        error_detail (sys): L'objet sys pour obtenir des informations détaillées sur l'erreur.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Retourne le message d'erreur détaillé lorsque l'exception est convertie en chaîne de caractères.
        """
        return self.error_message
