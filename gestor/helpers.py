## Funciones de ayuda ##

import os
import platform


def clear():
       """ Limpia la Pantalla

    Args:
        os.system = verifica sistema operativo 
        
    
    Returns:
            cls o clear dependiendo del sistema operativo

       """
if platform.system() == "Windows":
            os.system('cls')
else:
          os.system('clear')

def text_input (min_length, max_length):
    """ Permite controlar el tamaño del texto a ingresar 

    Args:
        min_length  (int) : minimo de texto a ingresar
        max_length (int) : maximo de texto a ingresar
    
    Returns:
            text (str) :  minimo y maximo de longitud establecida

    """
    while  True:
        text = input("> ")
        if len(text) >= min_length and len(text) <= max_length:
            return text

      
