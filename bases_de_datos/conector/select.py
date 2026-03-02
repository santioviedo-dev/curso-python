from mysql import connector


# Conexión
personas_db = connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="personas",
    port=3307
)


#Ejecutar sentencia select
cursor = personas_db.cursor()
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)
    
    
cursor.close
personas_db.close