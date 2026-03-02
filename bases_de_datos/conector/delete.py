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
query = "DELETE FROM personas WHERE idpersonas=%s"
valores =(2, )
cursor.execute(query, valores)
personas_db.commit()
cursor.close()
personas_db.close()