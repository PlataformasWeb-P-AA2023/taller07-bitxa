from schemes import Club

def run(session):       
    clubs = session.query(Club).all() 

    # Se recorre la lista a través de un ciclo
    # repetitivo for en python
    print("Presentación de Clubs y sus jugadores")
    for s in clubs:
        print("%s" % (s))
        # desde cada objeto de la lista
        # de tipo Club
        # se puede acceder 
        # a los jugadores
        jugadores = s.jugadores # es una secuencia; es una lista
        # [objJugador1, objJugador2, objJugador3, ..., objJugadorN]
        for i in jugadores:
            print(i.dorsal)

        print("---------")


