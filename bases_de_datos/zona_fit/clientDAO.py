from connection import Connection
from client import Client

class ClientDAO:
    SELECT = "SELECT * FROM clients ORDER BY id"
    INSERT = "INSERT INTO clients(first_name, last_name, membership) VALUES(%s, %s, %s)"
    UPDATE = "UPDATE clients SET first_name=%s, last_name=%s, membership=%s WHERE id=%s"
    DELETE = "DELETE FROM clients WHERE id=%s"
    
    @classmethod
    def select(cls):
        conn = None
        try:
            conn = Connection.acquire()
            cursor = conn.cursor()
            cursor.execute(cls.SELECT)
            registries = cursor.fetchall() 
            # Mapping
            clients = []
            for registry in registries:
                client = Client(registry[0], registry[1], registry[2], registry[3])
                clients.append(client)
            return clients
        except Exception as e:
            print(f"An error occurred while obtaining clients: {e}")
        finally:
            if conn is not None:
                cursor.close()
                Connection.release(conn)
            


if __name__ == "__main__":
    clients = ClientDAO.select()
    # for client in clients:
    #     print(client)
    print([str(client) for client in clients])