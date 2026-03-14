from mamiferos.mamifero import Mamifero
class Persona(Mamifero):
    def __init__(self, name, specie, age, habitat, gestacion_period, ocupacion):
        super().__init__(name, specie, age, habitat, gestacion_period)
        self.ocupacion = ocupacion
        self.pensar = True

    def eat(self, food):
        return super().eat(food)
    
    def sleep(self, hours):
        return super().sleep(hours)
    
    def trabajar(self, hours):
        if self.alive:
            return f"{self.name} está trabajando por {hours} horas como {self.ocupacion}."
        else:
            return f"{self.name} No puede trabajar porque no está vivo."
        
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nOcupación: {self.ocupacion}"