import connection
from queries import consulta_datos1, consulta_datos2, consulta_datos3, consulta_datos4

def run_all_queries():
    queries = [
        consulta_datos1, consulta_datos2, consulta_datos3, consulta_datos4
    ]
    
    session = connection.get_session()  

    for query in queries:
        query.run(session)

    session.close()

