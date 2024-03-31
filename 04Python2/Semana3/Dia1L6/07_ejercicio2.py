class Pelicula:
    def __init__(self, titulo, director, genero, duracion):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.duracion = duracion

    def mostrar_informacion(self):
        print("Información de la película:")
        print(f"Título: {self.titulo}")
        print(f"Director: {self.director}")
        print(f"Género: {self.genero}")
        print(f"Duración: {self.duracion} minutos")
        print()


def main():
    peliculas = []

    print("Bienvenido al sistema de registro de películas del cine.")

    # Agregar 5 nuevas películas
    for _ in range(5):
        titulo = input("Ingrese el título de la película: ")
        director = input("Ingrese el nombre del director: ")
        genero = input("Ingrese el género de la película: ")
        duracion = input("Ingrese la duración en minutos: ")

        pelicula = Pelicula(titulo, director, genero, duracion)
        peliculas.append(pelicula)
        print("¡Película registrada!\n")

    # Mostrar información detallada de cada película
    print("Información detallada de las películas:")
    for idx, pelicula in enumerate(peliculas, start=1):
        print(f"Película {idx}:")
        pelicula.mostrar_informacion()


if __name__ == "__main__":
    main()
