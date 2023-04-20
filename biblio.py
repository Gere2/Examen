from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


class Libro:
    def __init__(self, titulo, autor, fecha_publicacion, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.num_paginas = num_paginas

    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.fecha_publicacion}, {self.num_paginas} páginas"


class LibroFiccion(Libro):
    def __init__(self, titulo, autor, fecha_publicacion, num_paginas, genero, num_capitulos):
        super().__init__(titulo, autor, fecha_publicacion, num_paginas)
        self.genero = genero
        self.num_capitulos = num_capitulos

    def __str__(self):
        return f"{super().__str__()}, Género: {self.genero}, Capítulos: {self.num_capitulos}"


class LibroNoFiccion(Libro):
    def __init__(self, titulo, autor, fecha_publicacion, num_paginas, tema, num_secciones):
        super().__init__(titulo, autor, fecha_publicacion, num_paginas)
        self.tema = tema
        self.num_secciones = num_secciones

    def __str__(self):
        return f"{super().__str__()}, Tema: {self.tema}, Secciones: {self.num_secciones}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                break

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

biblioteca = Biblioteca()

def main():
    biblioteca = Biblioteca()

    while True:
        print("\nOpciones:")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Buscar libro")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            tipo_libro = input("Ingrese 'ficcion' para libros de ficción o 'no_ficcion' para libros de no ficción: ")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            fecha_publicacion = input("Ingrese la fecha de publicación del libro: ")
            num_paginas = int(input("Ingrese el número de páginas del libro: "))

            if tipo_libro == 'ficcion':
                genero = input("Ingrese el género del libro: ")
                num_capitulos = int(input("Ingrese el número de capítulos del libro: "))
                libro = LibroFiccion(titulo, autor, fecha_publicacion, num_paginas, genero, num_capitulos)
            else:
                tema = input("Ingrese el tema del libro: ")
                num_secciones = int(input("Ingrese el número de secciones del libro: "))
                libro = LibroNoFiccion(titulo, autor, fecha_publicacion, num_paginas, tema, num_secciones)

            biblioteca.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        elif opcion ==   2:
            titulo = input("Ingrese el título del libro a eliminar: ")
            biblioteca.eliminar_libro(titulo)
            print("Libro eliminado exitosamente.")

        elif opcion == 3:
           titulo = input("Ingrese el título del libro a buscar: ")
           libro = biblioteca.buscar_libro(titulo)
           if libro is not None:
             print("Detalles del libro encontrado:")
             print(libro)
           else:
             print("No se encontró el libro con el título especificado.")

        elif opcion == 4:
             print("Saliendo del programa.")
             break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

@app.route("/")
def index():
    return render_template("index.html", libros=biblioteca.libros)


@app.route("/agregar_libro", methods=["POST"])
def agregar_libro():
    # Obtén la información del libro del formulario HTML
    tipo_libro = request.form["tipo_libro"]
    titulo = request.form["titulo"]
    autor = request.form["autor"]
    fecha_publicacion = request.form["fecha_publicacion"]
    num_paginas = request.form["num_paginas"]
    genero = request.form["genero"]
    num_capitulos = request.form["num_capitulos"]
    tema = request.form["tema"]
    num_secciones = request.form["num_secciones"]

    # Validar el formulario
    error = validarFormulario(tipo_libro, titulo, autor, fecha_publicacion, num_paginas, genero, num_capitulos, tema,
                              num_secciones)
    if error:
        return render_template("index.html", libros=biblioteca.libros, error=error)

    # Crear un objeto libro y agregarlo a la biblioteca
    if tipo_libro == "ficcion":
        libro = LibroFiccion(titulo, autor, fecha_publicacion, int(num_paginas), genero, int(num_capitulos))
    else:
        libro = LibroNoFiccion(titulo, autor, fecha_publicacion, int(num_paginas), tema, int(num_secciones))
    biblioteca.agregar_libro(libro)

    # Redirigir al usuario a la página principal
    return redirect(url_for("index"))

def validarFormulario(tipo_libro, titulo, autor, fecha_publicacion, num_paginas, genero="", num_capitulos="", tema="",num_secciones=""):
    if tipo_libro not in ["ficcion", "no_ficcion"]:
        return "Tipo de libro inválido"

    if not titulo:
        return "Título no puede estar vacío"

    if not autor:
        return "Autor no puede estar vacío"

    if not fecha_publicacion:
        return "Fecha de publicación no puede estar vacía"

    if not num_paginas.isdigit() or int(num_paginas) <= 0:
        return "Número de páginas debe ser un número positivo"

    if tipo_libro == "ficcion":
        if not genero:
            return "Género no puede estar vacío"

        if not num_capitulos.isdigit() or int(num_capitulos) <= 0:
            return "Número de capítulos debe ser un número positivo"
    else:
        if not tema:
            return "Tema no puede estar vacío"

        if not num_secciones.isdigit() or int(num_secciones) <= 0:
            return "Número de secciones debe ser un número positivo"

    return ""

@app.route("/eliminar_libro", methods=["POST"])
def eliminar_libro():
    titulo = request.form["titulo"]
    biblioteca.eliminar_libro(titulo)
    return redirect(url_for("index"))

@app.route("/buscar_libro", methods=["GET"])
def buscar_libro():
    titulo = request.args.get("titulo")
    libro = biblioteca.buscar_libro(titulo)
    if libro:
        titulo = request.args.get("titulo")
        libro = biblioteca.buscar_libro(titulo)
        return render_template("buscar_libro.html", libro=libro)
    else:
        return render_template("error.html", message="No se encontró el libro con el título especificado.")





if __name__ == '__main__':
    app.run(debug=True)