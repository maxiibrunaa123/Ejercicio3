# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0


class Coche(Vehiculo):
    velocidad = 0
    Cilindrada = 0

auto = Coche()

auto.color="Azul"
auto.ruedas = 4
auto.puertas = 5
auto.velocidad= 300
auto.Cilindrada=2000

print(auto.__dict__)







