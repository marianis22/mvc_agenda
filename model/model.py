from .contacto import Contacto
from .cita import Cita

class Model:
    def __init__(self):
        self.contactos = []
        self.citas = []
    
    def esta_id(self, iden, tipo):
        #Tipos: 1-contacto, 2-cita
        if tipo == 1:
            for c in self.contactos:
                if c.id_contacto == iden:
                    return True, c
            return False, None
        if tipo == 2:
            for c in self.citas:
                if c.id_cita == iden:
                    return True, c
            return False, None

    # Contacto methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        f,c = self.esta_id(id_contacto, 1)
        if not f:
            c = Contacto(id_contacto, nombre, tel, correo, dir)
            self.contactos.append(c)
            return True, c
        return False, c
    
    def leer_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto, 1)
        return e, c
    
    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_dir):
        e, c = self.esta_id(id_contacto, 1)
        if e:
            if n_nombre != None:
                c.nombre = n_nombre
            if n_tel != None:
                c.tel = n_tel
            if n_correo != None:
                c.correo = n_correo
            if n_dir != None:
                c.dir = n_dir
            return True
        return False
    
    def borrar_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto, 1)
        if e:
            lista = [ci for ci in self.citas if c.id_contacto == id_contacto]
            for ci in lista:
                self.citas.remove(ci)
            self.contactos.remove(c)
            return True, c
        return False, None

    def leer_contactos_letra(self, letra):
        lista = [c for c in self.contactos if c.nombre.lower().startswith(letra.lower())]
        return lista

    # Cita methods
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        f,c = self.esta_id(id_cita, 2)
        if not f:
            if self.esta_id(id_contacto, 1)[0]:
                c = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
                self.citas.append(c)
                return True, c
            return False, id_contacto
        return False, c
    
    def leer_cita(self, id_cita):
        e, c = self.esta_id(id_cita, 2)
        if e:
            con = self.esta_id(c.id_contacto, 1)[1].nombre
            return e, c, con
        return e, c, None
    
    def actualizar_cita(self, id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        e, c = self.esta_id(id_cita, 2)
        if e:
            if self.esta_id(n_id_contacto, 1)[0]:
                c.id_contacto = n_id_contacto
            if n_lugar != None:
                c.lugar = n_lugar
            if n_fecha != None:
                c.fecha = n_fecha
            if n_hora != None:
                c.hora = n_hora
            if n_asunto != None:
                c.asunto = n_asunto
            return True, c
        return False, c
    
    def borrar_cita(self, id_cita):
        e, c = self.esta_id(id_cita, 2)
        if e:
            self.citas.remove(c)
            return True, c
        return False, None

    def leer_citas_fecha(self, fecha):
        lista = [c for c in self.citas if c.fecha == fecha]
        return lista