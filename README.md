# Examen
Biblioteca online 

Este proyecto de biblioteca virtual muy basica, esta organizado de la siguiente manera:

--- blibio.py (Logica de la bilbioteca para ingresar, validar, borrar, buscar

--- templates (carpeta donde se almacena el front-end desarrollado en html)
-----   index.html (tenemos un diseño para la pagina principal)
-----   buscar_libro.html (otro para buscar el libro) 
-----   error.html (una para errores)

---  static (carpeta para el diseño desarrollado en css y con las imagenes para el fondo y una generica a la hora de buscar libro)
-----    style.css


blibio.py 

  class Libro:
    
    Aqui construimos la logica del libro, añadiendo todas las caracteristicas
  
  class LibroFiccion(Libro):
      
    Creamos un hijo de la anterior para los libros de ficcion, heredando caracteristicas y añadiendo nuevas 


  class LibroNoFiccion(Libro):
     
    Creamos un hijo de la anterior para los libros de no-ficcion, heredando caracteristicas y añadiendo nuevas 

  
  class Biblioteca:
  
    construimos la logica para poder implementar libros, elimar, buscar.
  
  @app.route("/")
    def index():
      return render_template("index.html", libros=biblioteca.libros)
      
    Conectamos con el framework de flask nuestra logica con la interfaz que hemos creado en index.html
    
  @app.route("/agregar_libro", methods=["POST"])
  
    def agregar_libro():
    def validarFormulario(tipo_libro, titulo, autor, fecha_publicacion, num_paginas, genero="", num_capitulos="", tema="",num_secciones=""):

  @app.route("/eliminar_libro", methods=["POST"])
    def eliminar_libro():
    
  @app.route("/buscar_libro", methods=["GET"])
    def buscar_libro():
