import helpers
import manager

def loop():
    """ Funcion que genera loop para el menu
    Args:
        opcion (int) : numero de opcion del menu
    Returns:
        Segun  opcion retorna  funcion listada
        loop rompe con break en opcion 6  
    """
    while True:

        helpers.clear()

        print("========================")
        print("     Menu Clientes      ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Buscar cliente      ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Cerrar el Manager   ")
        print("========================")

        opcion = input("> ")
        helpers.clear()

        if opcion == '1':
            print("Listando los clientes...\n")
            manager.show_all()
        if opcion == '2':
            print("Buscando un cliente...\n")
            manager.find()
        if opcion == '3':
            print("Añadiendo un cliente...\n")
            manager.add()
            print("Cliente añadido correctamente")
        if opcion == '4':
            print("Modificando un cliente...\n")
            if  manager.edit():
              print("Cliente modificado correctamente\n") 
            else:
                print("cliente no modificado \n") 
        if opcion == '5':
            print("Borrando un cliente...\n")
            manager.delete()
            print("Cliente Borrado.... \n ")
        if opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")