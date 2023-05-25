from schemes import Jugador, Club

def run(session):
    clubs = session.query(Club).all()
    # Se recorre la lista a través de un ciclo
    # repetitivo for en python
    print("Presentación de Clubs")
    for s in clubs:
        print("%s" % (s))
        print("---------")

    # Obtener todos los registros de 
    # la entidad Jugador
    jugadores = session.query(Jugador).all()

    # Se recorre la lista a través de un ciclo
    # repetitivo for en python

    print("Jugadores")
    for s in jugadores:
        print("%s" % (s))
        print("---------")



