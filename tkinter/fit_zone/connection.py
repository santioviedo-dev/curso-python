
from mysql.connector import pooling
from mysql.connector import Error
class Connection:
    DATABASE = "zona_fit"
    USERNAME = "root"
    PASSWORD = "root"
    DB_PORT = "3307"
    HOST = "localhost"
    POOL_SIZE = 5 # number of available connections
    POOL_NAME = "zona_fit_pool"
    pool = None
    
    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f"Error: {e}")
        else:
            return cls.pool
    @classmethod
    def acquire(cls):
        return cls.get_pool().get_connection()
    @classmethod
    def release(cls, connection):
        connection.close()
        

    