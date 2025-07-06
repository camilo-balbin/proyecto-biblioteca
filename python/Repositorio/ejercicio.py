#proyecto biblioteca

def menu():#menu de la biblioteca
    print("\nBienvenido a nuestra biblioteca MINIBIBLIOTECA ")
    print("\n1. Registrar un libro")
    print("2. Registrar un socio")
    print("3. Prestar un libro")
    print("4. Devolver un libro")
    print("5. Ver libros prestados ")
    print("6. Ver todos los libros ")
    print("7. Ver todos los socios ")
    print("0. Salir")
    print("por fin dio esta mierda?")
    
def RegistrarLibro():
    titulo = input("\ningrese el titulo del libro:").split()#.lower()# split:para separa con una coma cada vez que se ingrese un titulo.
    if not titulo:
        print("Titulo no puede estar vacio")
        
    autor = input("\ningrese el autor del libro: ").split()#.lower()#lower: colocar todas en minusculas
    
    if not autor:
        print("el autor no puede estar vacio")
        
        
    Isbn =input("\ningrese el ISBN del libro: ").split()#.lower()
    print("libro registrado con exito")
    if not Isbn:
        print("el ISBN no puede estar vacio")
    

def RegistrarSocio():
    pass

def PrestarLibro():
    pass

def DevolverLibro():
    pass

def VerLibrosPrestados():
    pass

def VerTodosLibros():
    pass

def VerTodosSocios():
    pass


def main():#funcion principal
    while True:
        menu()
        opcion = int(input("\ningrese la opcion que desea escojer(0-7): "))
        
        if opcion == 1:
            RegistrarLibro()
        elif opcion == 2:
            RegistrarSocio()
        elif opcion == 3:
            PrestarLibro()
        elif opcion == 4:
            DevolverLibro()
        elif opcion == 5:
            VerLibrosPrestados()
        elif opcion == 6:
            VerTodosLibros()
        elif opcion == 7:
            VerTodosSocios()
        elif opcion == 0:
            break
        else:
            print("Opcion no valida, ingresa una opcion del 0 al 7")
  

main()
