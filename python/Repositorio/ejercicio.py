#proyecto biblioteca

#base de datos en memoria

libros = [
    {
        'isbn': '1',
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'estado': 'Disponible',
        'socioPrestado': None
    },
    {
        'isbn': '2',
        'titulo': 'Don Quijote de la Mancha',
        'autor': 'Miguel de Cervantes',
        'estado': 'Disponible',
        'socioPrestado': None
    },
    {
        'isbn': '3',
        'titulo': 'El código Da Vinci',
        'autor': 'Dan Brown',
        'estado': 'Disponible',
        'socioPrestado': None
    },
    {
        'isbn': '4',
        'titulo': 'El amor en los tiempos del cólera',
        'autor': 'Gabriel García Márquez',
        'estado': 'Disponible',
        'socioPrestado': None
    }
]
socios = []
auxContador =1


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
 
 
 
 
  
def RegistrarLibro():
    
    global libros 
    print("\nRegistar libros📖")
    
    titulo = input("\ningrese el titulo del libro:").lower()# .split():para separa con una coma cada vez que se ingrese un titulo.
    
    if not titulo:
        print("\n❌Titulo no puede estar vacio❌")#.strip() STRIP = quitar espacios o tabulaciones
        
        print("\nintenta de nuevo")
        RegistrarLibro()#reinicia nuevamente la funcion registar libro
        
    autor = input("\ningrese el autor del libro: ")
    if not autor:
        print("❌el autor no puede estar vacio❌")#lower: colocar todas en minusculas
        print("\nintenta de nuevo")
        RegistrarLibro()
        
        
    isbn =input("\ningrese el ISBN del libro: ").split()#.lower()
    if not isbn:
        print("❌el ISBN no puede estar vacio❌")
        print("\nintenta de nuevo")
        RegistrarLibro()
        
    #funcion para verificiar que no haya otro libro con el mismo isbn
    for l in libros:
        if l ['isbn'] == isbn:
            print(f"❌ya existe un libro con el ISBN {isbn}❌")
            return
    #crear el nuevo libro   
    nuevoLibro = {#diccionario
        
        'isbn' : isbn,
        'titulo' : titulo,
        'autor' : autor,
        'estado' : 'Disponible',
        'socioPrestado': None # no se a prestado a ningun socio
      
    }
    libros.append(nuevoLibro)#append: agregar a la lista
    print("\n✅libro registrado exitosamente✅")
    print(f"{titulo} - {autor}")
    print(f"ISBN: {isbn}")
    





def RegistrarSocio():
    pass

def PrestarLibro():
    pass

def DevolverLibro():
    pass

def VerLibrosPrestados():
    pass

def VerTodosLibros():
    print("\n📖 mostrando todos los libros")
    
    if not libros:
        print("\n❌no hay libros registrados en la biblioteca❌")
        return

    for i, libro in enumerate(libros,1):
        print(f"\n{i}.Nombre del libro: {libro['titulo']}")
        print(f" Autor:{libro['autor']}")
        print(f" ISBN:{libro['isbn']}")
        print(f" Estado:{libro['estado']}")



def VerTodosSocios():
    print("\n mostrando todos los socios")
    
    if not socios:
        print("\n❌no hay socios registrados en la biblioteca❌")
   


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
