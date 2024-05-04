  |                             MÉTODOS USADOS                                                                                                       |
------------------------------------------------------------------------------------------------------------------------------------------------------
1. Libro.__init__: Este método inicializa un objeto Libro con los atributos título, autor y año.

2. Biblioteca.__init__: Inicializa una Biblioteca vacía con una lista para almacenar libros.

3. Biblioteca.agregar_libro: Añade un libro a la biblioteca si tiene título y autor, luego lo imprime.

4. Biblioteca.buscar_libro: Busca un libro por su título en la biblioteca y lo devuelve si lo encuentra, de lo contrario, genera una excepción.

5. Biblioteca.mostrar_libros: Muestra todos los libros en la biblioteca o indica que está vacía.

6. ErrorLibroSinTitulo: Excepción personalizada para libros sin título.

7. ErrorLibroSinAutor: Excepción personalizada para libros sin autor.

8. validar_año_publicacion: Valida que el año de publicación sea un número positivo.

9. main: Función principal que proporciona un menú para interactuar con la biblioteca, permitiendo agregar libros, buscar por título, mostrar todos los libros y salir del programa.
