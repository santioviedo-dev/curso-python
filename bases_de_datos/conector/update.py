from mysql import connector


# Conexión
personas_db = connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="personas",
    port=3307
)


#Ejecutar UPDATE
cursor = personas_db.cursor()
query = "UPDATE personas SET nombre=%s, apellido=%s WHERE idpersonas=%s"
valores =("Victoria", "Flores", 3)
cursor.execute(query, valores)
personas_db.commit()
cursor.close()
personas_db.close()