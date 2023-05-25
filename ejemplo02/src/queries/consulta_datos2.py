from schemes import Jugador
import connection as connection

def run(session):    
    jugadores = session.query(Jugador).all() 
    # Se recorre la lista a través de un ciclo
    # repetitivo for en python
    print("Presentación de Jugadores")
    for s in jugadores:
        print("%s" % (s))
        # desde cada objeto de la lista
        # jugador
        # se puede acceder al club; como lo definimos
        # al momento de crear la clase Jugador
        print("El Jugador pertenece a: %s " % (s.club))
        print("---------")

    print("Presentación de Jugadores - op2")
    for s in jugadores:
        print("%s" % (s))
        # desde cada objeto de la lista
        # jugador
        # se puede acceder al club; como lo definimos
        # al momento de crear la clase Jugador
        print("El Jugador pertenece a: %s " % (s.club.nombre))
        print("---------")



