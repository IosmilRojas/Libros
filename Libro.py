class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if not libro.titulo or not libro.autor:
            raise ValueError("El libro debe tener un título y un autor.")
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        raise ValueError(f"No se encontró ningún libro con el título '{titulo}'.")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro.titulo} (Autor: {libro.autor}, Año: {libro.año_publicacion})")


class ErrorLibroSinTitulo(Exception):
    def __init__(self, mensaje="El libro debe tener un título."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorLibroSinAutor(Exception):
    def __init__(self, mensaje="El libro debe tener un autor."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def validar_año_publicacion(año_publicacion):
    if not año_publicacion.isdigit() or int(año_publicacion) < 0:
        raise ValueError("El año de publicación debe ser un número positivo.")

def main():
    biblioteca = Biblioteca()

    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Buscar libro por título")
        print("3. Mostrar todos los libros")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:  # Bucle para manejar la entrada de datos del libro
                try:
                    titulo = input("Ingrese el título del libro: ")
                    if not titulo:
                        raise ErrorLibroSinTitulo("El libro debe tener un título.")

                    autor = input("Ingrese el autor del libro: ")
                    if not autor:
                        raise ErrorLibroSinAutor("El libro debe tener un autor.")
                    if any(char.isdigit() for char in autor):
                        raise ValueError("El nombre del autor no puede contener números.")

                    año_publicacion = input("Ingrese el año de publicación del libro: ")
                    validar_año_publicacion(año_publicacion)

                    libro = Libro(titulo, autor, año_publicacion)
                    biblioteca.agregar_libro(libro)
                    break  # Si se agregó el libro correctamente, salimos del bucle interno

                except (ErrorLibroSinTitulo, ErrorLibroSinAutor, ValueError) as e:
                    print(f"Error: {e}")
                    continuar = input("¿Desea intentarlo de nuevo? (s/n): ")
                    if continuar.lower() != "s":
                        break  # Si el usuario no desea intentarlo de nuevo, salimos del bucle interno
            continue  # Continuar con el siguiente ciclo del menú después de agregar el libro

        elif opcion == "2":
            titulo = input("Ingrese el título del libro a buscar: ")
            try:
                libro_encontrado = biblioteca.buscar_libro(titulo)
                print(f"Libro encontrado: {libro_encontrado.titulo} (Autor: {libro_encontrado.autor}, Año: {libro_encontrado.año_publicacion})")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            biblioteca.mostrar_libros()

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
