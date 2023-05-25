from schemes import Jugador, Club
import connection as connection

def run(session):       
    clubs = session.query(Club).join(Jugador).\
            filter(Jugador.nombre.like("%Da%")).all()
    
    print("Consulta 1 ")
    """
    Consulta 1 
    Club: nombre=Barcelona deporte=Fútbol fundación=1920
    """
    for e in clubs: 
        print(e) 
    
    # Obtener un listado de todos los registros 
    # de la tabla Club y Jugador, que tengan al menos 
    # un jugador con el nombre que tenga incluida la cadena “Da”
    
    # para la solución se hace uso del método 
    # join aplicado a query
    # en el query se ubican las dos entidades involucradas
    # 
    
    registros = session.query(Club, Jugador).join(Jugador).\
            filter(Jugador.nombre.like("%Da%")).all()
    
    print("Consulta 2 ")
    """
    
    Consulta 2 
    
    Club: nombre=Barcelona deporte=Fútbol fundación=1920
    Jugador: Damian Diaz - dorsal:10 - posición: mediocampo
    
    
    Club: nombre=Barcelona deporte=Fútbol fundación=1920
    Jugador: Dario Aymar - dorsal:2 - posición: defensa
    """
    for registro in registros: 
        # el registro continen 
        # dos valores en un tupla
        # posición 0 el club
        # posición 1 el jugador 
        # que cumplen con la condición
        print(registro[0]) # El nombre del club
        print(registro[1]) # El número del dorsal del jugador
    
    
    
    
    
    


