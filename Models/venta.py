class venta():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS venta
                        (
                        codigo VARCHAR(40) NOT NULL,
                        cantidad VARCHAR (40) NOT NULL,
                        descripcion VARCHAR(40) NOT NULL,
                        precio_unit VARCHAR(40) NOT NULL,
                        descuento VARCHAR(40) NOT NULL,
                        total VARCHAR(40) NOT NULL,
                        stock VARCHAR(40) NOT NULL)"""
            cursor.execute(sql)
            self.conn.commit()

   
    
    def getVentas(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM venta"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getVenta(self, codigo):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM venta WHERE codigo = %s"""
            cursor.execute(sql,codigo)
            result = cursor.fetchone()
            if result:
                return result
    
    def updateVenta(self,codigo,cantidad, descripcion, precio_unit,descuento,total,stock):
        with self.conn.cursor() as cursor:
            sql = """UPDATE venta SET  cantidad = %s, descripcion= %s, precio_unit = %s, descuento = %s, total = %s, stock = %s, WHERE codigo = %s """
            cursor.execute(sql,( cantidad,descripcion, precio_unit,descuento,total,stock, codigo))
            self.conn.commit()

    def deleteVenta(self,codigo):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM venta WHERE codigo = %s"""
            cursor.execute(sql, codigo)
            self.conn.commit()
    
    def insertVenta(self,codigo,cantidad, descripcion, precio_unit,descuento,total,stock):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO venta (codigo,cantidad,descripcion,precio_unit,descuento,total,stock) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (self,codigo,cantidad, descripcion, precio_unit,descuento,total,stock))
            self.conn.commit()
            
    