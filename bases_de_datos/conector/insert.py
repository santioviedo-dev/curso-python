from mysql import connector


# Conexión
personas_db = connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="personas",
    port=3307
)


#Ejecutar INSERT
cursor = personas_db.cursor()
query = 'INSERT INTO personas(nombre, apellido) VALUES(%s, %s)'
valores = ("Víctor", "Dominguez")
cursor.execute(query, valores)
personas_db.commit()
cursor.close
personas_db.close