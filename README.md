# Fundamentos de Programación Orientada a Objetos (POO)

## Descripción del Proyecto

Este proyecto, ubicado en la carpeta `fundamentos-poo`, implementa una jerarquía de clases en Python para ilustrar los principios fundamentales de la Programación Orientada a Objetos (POO). Se enfoca en conceptos como herencia, encapsulamiento y polimorfismo a través de una estructura modular que representa seres vivos, mamíferos y personas. El archivo principal `main.py` demuestra la creación de instancias y la invocación de métodos, mostrando cómo las clases derivadas heredan y extienden el comportamiento de las clases base.

El proyecto está diseñado para ser educativo, permitiendo a los desarrolladores comprender cómo modelar entidades del mundo real con POO, promoviendo la reutilización de código y la organización lógica.

## Objetivos Alcanzados

- **Jerarquía de Clases**: Se creó una cadena de herencia donde `SerVivo` es la clase base, `Mamifero` hereda de `SerVivo`, y `Persona` hereda de `Mamifero`, demostrando la progresión de atributos y métodos.
- **Encapsulamiento**: Los atributos de las clases están protegidos mediante convenciones de Python (e.g., `_atributo` para privado), y se accede a ellos a través de métodos públicos.
- **Polimorfismo**: El método `show_info()` se redefine en cada subclase para proporcionar información específica, ilustrando cómo las subclases pueden adaptar el comportamiento heredado.
- **Modularidad**: El código está dividido en módulos separados (`seres_vivos`, `mamiferos`, `personas`), facilitando la mantenibilidad y la escalabilidad.
- **Demostración Práctica**: El archivo `main.py` instancia objetos de cada clase y muestra su información, sirviendo como punto de entrada y ejemplo de uso.

## Estructura del Proyecto

fundamentos-poo/
├── README.md # Este archivo de documentación
├── main.py # Archivo principal que demuestra el uso de las clases
├── seres_vivos/
│ └── ser_vivo.py # Clase base SerVivo con atributos como nombre, especie, edad y hábitat
├── mamiferos/
│ └── mamifero.py # Clase Mamifero que hereda de SerVivo, añade atributo de patas
├── personas/
│ └── persona.py # Clase Persona que hereda de Mamifero, añade atributos de educación y profesión
└── (posibles tests o requirements si se añaden)


### Descripción de Archivos Principales

- **`seres_vivos/ser_vivo.py`**: Define la clase `SerVivo`, que representa un ser vivo genérico. Incluye atributos como `nombre`, `especie`, `edad` y `habitat`. El método `show_info()` devuelve una cadena con la información básica.
- **`mamiferos/mamifero.py`**: Define la clase `Mamifero`, que hereda de `SerVivo`. Añade el atributo `patas` (número de patas) y sobrescribe `show_info()` para incluir este detalle, demostrando herencia y polimorfismo.
- **`personas/persona.py`**: Define la clase `Persona`, que hereda de `Mamifero`. Añade atributos como `educacion` (años de educación) y `profesion`. Sobrescribe `show_info()` para mostrar información completa, incluyendo herencia de atributos superiores.
- **`main.py`**: Función `main_poo()` que crea instancias de cada clase (e.g., un perro como `SerVivo`, un gato como `Mamifero`, y una persona como `Persona`). Imprime la información de cada objeto usando `show_info()`, ilustrando la jerarquía y el comportamiento polimórfico.

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Entorno**: Compatible con cualquier IDE, como VS Code, para ejecutar y depurar.
- **Dependencias**: Ninguna externa; utiliza solo bibliotecas estándar de Python.

## Instalación y Uso

1. **Requisitos**: Asegúrate de tener Python 3.x instalado en tu sistema.
2. **Ejecución**:
   - Navega a la carpeta `fundamentos-poo`.
   - Ejecuta `python main.py` desde la terminal o tu IDE.
3. **Salida Esperada**: El programa imprimirá información detallada para cada instancia creada, mostrando cómo la herencia y el polimorfismo afectan la salida.
4. **Modificaciones**: Puedes editar los archivos de clases para añadir más atributos o métodos, y actualizar `main.py` para probar nuevas instancias.

## Ejemplo de Ejecución

Al ejecutar `main.py`, se obtiene una salida similar a:

Nombre: Ruperto, Especie: Perro, Edad: 5, Hábitat: Casa

Nombre: Felix, Especie: Gato, Edad: 3, Hábitat: Casa, Patas: 2

Nombre: Juan, Especie: Humano, Edad: 30, Hábitat: Ciudad, Patas: 2, Educación: 9 años, Profesión: Ingeniero


Esto demuestra cómo cada subclase añade información específica mientras mantiene la estructura base.

## Contribuciones y Mejoras

- **Extensibilidad**: Puedes añadir más subclases, como `Ave` heredando de `SerVivo`, o métodos adicionales como `moverse()`.
- **Pruebas**: Considera añadir pruebas unitarias con `unittest` para validar el comportamiento de las clases.
- **Contribuciones**: Si deseas mejorar el proyecto, crea un issue o pull request en el repositorio correspondiente.

## Licencia

Este proyecto es de código abierto bajo la Licencia MIT.

## Autor

Desarrollado como parte de un curso o proyecto educativo. Para consultas, revisa los comentarios en el código.

---

*¡Explora la POO a través de este ejemplo práctico!*

{
    "fileName": "README.md"
}