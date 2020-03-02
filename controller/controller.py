from model.model import Model
from view.view import View

class Controller:
    # Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    # Contacto methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        f,c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if f:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e,c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
    
    def actualizar_contacto(self, id_contacto, n_nombre=None, n_tel=None, n_correo=None, n_dir=None):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)
    
    def borrar_contacto(self, id_contacto):
        e,c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
        
    def leer_contactos_letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)
    
    # Cita methods
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e,c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if e:
            self.view.agregar_cita(c)
        else:
            if type(c) is int:
                self.view.contacto_no_existe(id_contacto)
            else:
                self.view.cita_ya_existe(c)

    def leer_cita(self, id_cita):
        e,ci,con = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(ci, con)
        else:
            self.view.cita_no_existe(id_cita)
    
    def actualizar_cita(self, id_cita=0, n_id_contacto=0, n_lugar=None, n_fecha=None,
    n_hora=None, n_asunto=None):
        e,c = self.model.actualizar_cita(id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto)
        if e:
            self.view.actualizar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)
    
    def borrar_cita(self, id_cita):
        e,c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)
    
    def leer_citas_fecha(self, letra):
        c = self.model.leer_citas_fecha(letra)
        self.view.mostrar_citas(c)

    # General methods
    def insertar_contactos(self):
        self.agregar_contacto(1, 'Mariana Arce Aguilar', '461660804', 'marianarce9@hotmail.com', 'Salamanca')
        self.agregar_contacto(2, 'Sara Sanchez', '123-456-7890', 'sara_22@gamail.com', 'CDMX')
        self.agregar_contacto(3, 'Carlos Alvarado', '467125896', 'carlos_55@gmail.com', 'leon')
    
    def insertar_citas(self):
        self.model.agregar_cita(1, 1, 'Mexico', '27 de Febrero del 2020', '12:15p.m', 'cita')
        self.model.agregar_cita(2, 2, 'salamanca', '27 de Febrero del 2020', '12:15p.m', 'cita')
    
    def start(self):
        self.view.start()
        self.insertar_contactos()
        self.insertar_citas()
        
'''   
    def start(self):
        self.view.start()
        self.insertar_contactos()
        self.insertar_citas()

    def start(self):

        #dispaly a welcome message
        self.view.start()
        #insert data model
        self.insertar_contactos()
        self.insertar_citas()  
        #show all contacts in DB
        self.leer_todos_contactos()
        self.leer_todos_contactos_letra('a')     

    def menu(self):
        #display menu
        self.view.menu()
        o = input('selecciona una opcion (1-9)'):
        if o == '1':
            pass
        elif o == '2':
            pass
         elif o == '3':
            pass
        elif o == '4':
            pass
        elif o == '9':
            self.view.end()
        else:
            self.view.opcion_no_valida()    
 '''    
              
              
              
              
