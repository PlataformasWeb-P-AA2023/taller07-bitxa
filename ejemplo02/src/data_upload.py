import pandas as pd
from schemes import Club, Jugador
import connection

def load_clubs_data(data, session):
    for index, row in data.iterrows():
        nombre = row["nombre"]
        deporte = row["deporte"]
        fundacion = row["fundacion"]
        club = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
        session.add(club)
        
def load_players_data(data, session):
    for index, row in data.iterrows():
        nombre = row["nombre"]
        club_nombre = row["club"]
        numero = row["numero"]
        posicion = row["posicion"]
        
        club = session.query(Club).filter(Club.nombre == club_nombre).first()
        jugador = Jugador(nombre=nombre, dorsal=numero, posicion=posicion, club=club)
        session.add(jugador)
        
if __name__ == '__main__':
    clubs_data = pd.read_csv('../data/datos_clubs.txt', sep=';', header=None)
    clubs_data.columns = ["nombre", "deporte", "fundacion"]
    
    players_data = pd.read_csv('../data/datos_jugadores.txt', sep=';', header=None)
    players_data.columns =["club", "posicion", "numero", "nombre"]
    
    session = connection.get_session()
    
    load_clubs_data(clubs_data, session)
    load_players_data(players_data, session)
    
    session.commit()
