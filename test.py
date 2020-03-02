from model.model import Model
from model.contacto import Contacto
from model.cita import Cita
from view.view import View
from controller.controller import Controller

'''
contactos = []
c1 = Contacto(1, 'Mariana Arce', '464-149-0299', 'm.arceaguilar@ugto.mx', 'direccion')
c2 = Contacto(2, 'Carlos x', '464-149-0299', 'm.arceaguilar@ugto.mx', 'direccion')

t1 = Cita(1, 1, 'Salamanca', '27 de Febrero del 2020', '12:15p.m', 'cita')
'''
"""
print(c.id_contacto)
print(c.nombre)
print(c.tel)
print(c.correo)
print(c.direccion)

print(d.id_cita)
print(d.id_contacto)
print(d.lugar)
print(d.fecha)
print(d.hora)
print(d.asunto)"""
'''
contactos.append(c1)
contactos.append(c2)
'''
"""t=input('Dame un nombre: ')

for c in contactos:
	if t.lower() == c.nombre.lower():
		print('Si esta')
		break
else:
	print('No esta')"""
'''
m = Model()
m.agregar_contacto(1, 'Daniel Soriano', '464-149-0299', 'da.alcocersorino@ugto.mx', 'direccion')
m.agregar_contacto(2, 'Carlos x', '464-149-0299', 'm.arceaguilar@ugto.mx', 'direccion')
m.agregar_contacto(3, 'Mariana', '464-143-0299', 'ca.alcocersorino@ugto.mx', 'franco')

s = m.leer_contacto(3)
print(s.nombre)

s = m.actualizar_contacto(3, 'Sara Juarez', '23434234',' g@hh', 'direccion')
s = m.leer_contacto(3)
print(s.nombre)

s = m.borrar_contacto(1)
print(s)
s = m.borrar_contacto(1)
print(s)


m.agregar_cita(1, 1, 'Salamanca', '27 de Febrero del 2020', '12:15p.m', 'cita')
m.agregar_cita(2, 2, 'Irapuato', '28 de Febrero del 2020', '12:30p.m', 'citas')

x = m.leer_cita(2,1)
print(x.lugar)

s = m.actualizar_cita(1, 1, 'Mexico', '27 de Febrero del 2020', '12:15p.m', 'cita')
s = m.leer_cita(1)
print(s.lugar)

s = m.borrar_cita(2)
print(s)
s = m.borrar_cita(2)
print(s)

s2 = m.actualizar_cita2(1, 1, 'Mexico', '27 de Febrero del 2020', '12:15p.m', 'cita')
s2 = m.leer_cita(1)
print(s2.lugar)

s2 = m.borrar_cita(2)
print(s2)
s2 = m.borrar_cita(2)
print(s2)
'''
#Actualizar solo ciertos elementos del contacto o la cita 
#Buscar contactos que empiezen con una letra y me devuelva una lista de contactos
#Buscar las citas de la misma fecha
'''
v = View()
s = m.leer_todos_contactos()
v.mostrar_contacto(s)
c = m.leer_contacto(1)
v.mostrar_contacto(c)

f = m.borrar_contacto(1)
if f:
	v.borrar_contacto(c)
else:
	v.contacto_no_existe(1)	
'''


cont = Controller()
cont.start()
