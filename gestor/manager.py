 ### customer manager ####
import re
import helpers

clients = []


""" mock data """
marta ={'nombre': 'Marta', 'apellido':'Perez', 'dni':'15J'}
clients.append(marta)



clients.append({'nombre': 'Manolo', 'apellido':'Lopez', 'dni':'48H'})
clients.append({'nombre': 'Ana', 'apellido':'Garcia', 'dni':'28Z'})

def show(client):
    """ Function displayed by a client
    Arg:
    client    
     """
    print(f"{client['dni']}:{client['nombre']} {client['apellido']}")

def show_all():
    """ Function that shows all customers
         Call the show() function
    """
    for client in clients:
        show(client)


def find():

    #test in dni 
    """
    >>> is_valid ('48H') # no valido 
    False

    >>> is_valid ('H25') # no valido 
    False

    >>> is_valid ('21A') # valido 
    True
    """
    dni = input("introduce el DNI del cliente \n>") 

    for client in clients:
        if client ['dni'] == dni:
            show(client)
            
            return client
    print("No se ha encontrado el cliente con ese DNI")

def is_valid(dni):
    """ Function that checks that the DNI is valid
        Args
            dni : input
        prefex check dni
    """

    if not re.match('[0-9]{2}[A-Z]',dni):
        return False
    
    """ for to check that the DNI is not repeated"""
    for client in clients:
        if client['dni'] == dni:
            return False
    return True


def add():

    """  Function that adds client Check that Dni is not repeated before adding it """ 
    client = dict()

    print("Introduce nombre (de 2 a 30 caracteres)")
    client['nombre'] = helpers.input_text(2,30)

    print("Introduce apellido (de 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2,30)

    while True:
        print("Introduce DNI (2 numeros y 1 caracter Mayuscula)")
        dni = helpers.input_text(3,3)
        if is_valid(dni):
            client['dni'] = dni
            break
        print("DNI incorrecto o En uso ")

    clients.append(client)
    return client

def edit():

    """ Function edited by a client
     It is verified that the ID exists to change customer data
    """

    dni = input("Introduce el DNI del cliente\n")

    for i, client in enumerate(clients):

        if client['dni'] == dni:

            print(f"Introduce nuevo nombre ({client['nombre']})")
            clients[i]['nombre'] = helpers.input_text(2,30)

            print(f"Introduce nuevo apellido ({client['apellido']})")
            clients[i]['apellido'] = helpers.input_text(2,30)

            return True
    return False

def delete():

    """ Function that delete a client
    Arg: 
        dni (str)
           Return True : deleted customer
           False : customer not deleted
    """

    dni = input("Introduce el DNI del cliente\n>")

    for i, client in enumerate(clients):

        if client['dni'] == dni:
            client = clients.pop(i)
            show(client)
            return True
        
    return False


if __name__== "__main__":
    import doctest
    doctest.testmod()