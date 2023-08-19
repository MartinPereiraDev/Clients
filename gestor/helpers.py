## Functions ##

import os
import platform


def clear():
       """ Clean the screen     
    Returns:
            cls or clear depending on the operating system

       """
if platform.system() == "Windows":
            os.system('cls')
else:
          os.system('clear')

def text_input (min_length, max_length):
    """ function control the size of the text to be entered

    Args:
        min_length (int) : minimun
        max_length (int) : maximum
    
    Return:
            text (str) 

    """
    while  True:
        text = input("> ")
        if len(text) >= min_length and len(text) <= max_length:
            return text

      
