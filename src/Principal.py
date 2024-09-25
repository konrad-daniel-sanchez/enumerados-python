from Persona import Persona
from Genero import Genero

class Principal:

    @staticmethod
    def main():
        homero = Persona("1234", "Homero Simpson", 34, Genero.MASCULINO)

        print("El objeto homero tiene los siguientes valores:")
        print(f"Identificación: {homero.get_identificacion()}")
        print(f"Nombre: {homero.get_nombre()}")
        print(f"Edad: {homero.get_edad()}")

        if homero.get_genero() == Genero.MASCULINO:
            print("Homero es masculino")

        print("Los siguientes son todos los géneros disponibles:")
        generos_disponibles = list(Genero)
        for genero in generos_disponibles:
            print(genero.name)

if __name__ == "__main__":
    Principal.main()
