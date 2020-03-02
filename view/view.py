class View:
    def mostrar_contacto(self, contacto):
        print('***Datos del contacto***')
        print('Nombre:', contacto.nombre)
        print('Teléfono:', contacto.tel)
        print('Correo:', contacto.correo)
        print('Dirección:', contacto.dir)
        print('*******************')
        
    def mostrar_contactos(self, contactos):
        print('**** contactos *****')

        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('********************************')
    def agregar_contacto(self, id_contacto):
        print(id_contacto.nombre, 'se ha agregado a la base de datso')

    def borrar_contacto(self, contacto):
        print(contacto.nombre, ' se ha borrado el contacto')    

    def actualizar_contacto(self, contacto_o,contacto_n):
        print(contacto_o, 'se ha modificado')

    def contacto_ya_existe(self, contacto):
        print(contacto.id_contacto,'ya existe')    

    def contacto_no_existe(self, id_contacto):
        print(id_contacto,'no existe')    

    def start(self):
        print('esto es un ejemplo')     

    def end(self):
        print('bye')     
# metodos para citas:
    def mostrar_cita(self, cita):
        print('***Datos del cita***')
        print('Lugar:', cita.lugar)
        print('Fecha:', cita.fecha)
        print('Hora:', cita.hora)
        print('Asunto:', cita.asunto)
        print('*******************')

    def mostrar_citas(self, citas):
        print('**** citas *****')   
        for c in citas:
            print(c.lugar, c.fecha, c.hora, c.asunto)
        print('********************************')

    def crear_cita(self, cita):
        print(cita.asunto, 'se ha agregado a la base de datos')

    def borrar_cita(self, cita):
        print(cita.asunto, ' se ha borrado la cita')       

    def modificar_cita(self, cita_o):
        print(cita_o.asunto, 'se ha modificado')

    def cita_ya_existe(self,cita):
        print(cita.id_cita,'ya existe')    

    def cita_no_existe(self, id_cita):
        print(id_cita,'no existe')     

    def start(self):
        print('esto es un ejemplo sencillo de mvc')       
    
    
    def end(self):
        print('bye')     
             
    def menu(self):
        print('1. agregar contacto')
        print('2. ver contacto')
        print('3. actualizar contacto')
        print('4. borrar contacto')
        print('5. agregar cita')
        print('6. ver cita')
        print('7. actualizar cita')
        print('8. borrar cita')
        print('9. terminar')
