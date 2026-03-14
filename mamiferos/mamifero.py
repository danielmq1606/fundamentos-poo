from seres_vivos.ser_vivo import SerVivo

class Mamifero(SerVivo):
    def __init__(self, name, specie, age, habitat, gestacion_period):
        super().__init__(name, specie, age, habitat)
        self.gestacion_period = gestacion_period
        self.warm_blooded = True

    def parir(self):
        if self.alive:
            return f"{self.name} da a luz después de un período de gestación de {self.gestacion_period} meses."
        else:            
            print(f"{self.name} No puede parir porque no está vivo.")

    #eat
    def eat(self, food):
        if self.alive:
            return f"{self.name} está comiendo {food} con sus dientes."
        else:
            return f"{self.name} No puede comer porque no está vivo."
    
    #sleep
    def sleep(self, hours):
        if self.alive:
            return f"{self.name} está durmiendo por {hours} horas en su madriguera."
        else:
            return f"{self.name} No puede dormir porque no está vivo."