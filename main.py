from seres_vivos.ser_vivo import SerVivo
from mamiferos.mamifero import Mamifero
from personas.persona import Persona

def main_poo():
    # Crear un ser vivo
    ruperto = SerVivo("Ruperto", "Perro", 5, "Casa")
    print(ruperto.show_info())
    print('\n')

    # Crear un mamífero
    felix = Mamifero("Felix", "Gato", 3, "Casa", 2)
    print(felix.show_info())
    print('\n')

    # Crear una persona
    juan = Persona("Juan", "Humano", 30, "Ciudad", 9, "Ingeniero")
    print(juan.show_info())
    print('\n')

if __name__ == "__main__":
    main_poo()