from Genero import Genero

class Persona:
    def __init__(self, identificacion: str, nombre: str, edad: int, genero: Genero):
        """
        :param identificacion: str
        :param nombre: str
        :param edad: int
        :param genero: Genero

        Complejidad temporal: O(1) Tiempo constante
        """
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero

    def get_identificacion(self) -> str:
        """
        :return: str identificación

        Complejidad temporal: O(1) Tiempo constante
        """
        return self.__identificacion

    def get_nombre(self) -> str:
        """
        :return: str nombre

        Complejidad temporal: O(1) Tiempo constante
        """
        return self.__nombre

    def get_edad(self) -> int:
        """
        :return: int edad

        Complejidad temporal: O(1) Tiempo constante
        """
        return self.__edad

    def set_edad(self, edad: int):
        """
        :param edad: int

        Complejidad temporal: O(1) Tiempo constante
        """
        self.__edad = edad

    def get_genero(self) -> Genero:
        """
        :return: Genero género

        Complejidad temporal: O(1) Tiempo constante
        """
        return self.__genero

    def set_genero(self, genero: Genero):
        """
        :param genero: Genero

        Complejidad temporal: O(1) Tiempo constante
        """
        if self.__edad >= 18:
            self.__genero = genero
