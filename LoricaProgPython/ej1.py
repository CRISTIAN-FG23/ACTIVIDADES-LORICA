# Esto es un comentario
print("Hola, mundo!")  # Imprime un mensaje en la consola
edad = 30
altura = 1.75
print(f"Edad: {edad}, Altura: {altura} metros")  # Imprime la edad y altura
saludo = "Hola Juana Como  te va"
es_estudiante = True
colores = ["rojo", "verde", "azul"]
persona = {"nombre": "Carlos", "edad": 30}
print(f"Saludo: {saludo}, Es estudiante: {es_estudiante}, Colores: {colores}, Persona: {persona}")  # Imprime variables complejas
#Operadores y estructuras de control
suma = 10 + 5    
print(f"Suma: {suma}")  # Imprime el resultado de la suma
resta = 10 - 3    
producto = 4 * 3
division = 10 / 2 
modulo = 10 % 3    
exponente = 2 ** 3 
print(f"Resta: {resta}, Producto: {producto}, División: {division}, Módulo: {modulo}, Exponente: {exponente}")  # Imprime resultados de operaciones
#comparaciones
igual = (5 == 5) # True

diferente = (5 != 3) # True 

mayor = (10 > 7) # True 

menor = (3 < 5) # True
print(f"Igual: {igual}, Diferente: {diferente}, Mayor: {mayor}, Menor: {menor}")  # Imprime resultados de comparaciones
# Estructuras de control
#Operdores lógicos
print("operadores lógicos")
y_logico = (5 > 3) and (2 < 4)   # True

o_logico = (5 > 3) or (2 > 4)    # True

no_logico = not (5 > 3)          # False
print(f"Y lógico: {y_logico}, O lógico: {o_logico}, No lógico: {no_logico}")  # Imprime resultados de operadores lógicos
# Estructuras de control
print("Estructuras de control")
edad = 12
if edad >= 18:
 print("Eres adulto") 
elif edad >= 13: 
 print("Eres adolescente") 
else: print("Eres menor de edad")
#Bucles o Estructuras repetitivas
print("Bucles o Estructuras repetitivas")
# Itera sobre una lista de números 

numeros = [1, 2, 3, 4, 5,200,-300,17.5, 0.5]  # Lista de números

for numero in numeros: 
    print(numero)  # Imprime cada número en la lista

#Bucle o Estructura repetitiva While
# Imprime números del 0 al 4 contador = 0 
print("Bucle While")
contador = 0
while contador < 5:
    print(contador)  # Imprime el valor del contador
    contador += 1  # Incrementa el contador en 1        
 
#Uso de la instrucción break para salir del bucle
print("Uso de break")
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es igual a 5
    print(i)  # Imprime el valor de i    

# Uso de la instrucción continue para saltar a la siguiente iteración
print("Uso de continue")
for i in range(10): 
  if i % 2 == 0:
    continue
  print(i)
# Salida: 1, 3, 5, 7, 9

#Estructuras de datos y funciones de python
print("Estructuras de datos y funciones de Python")

mi_lista = [1, 2, 3, "cuatro",100,-150,3.14,["Monteria","Cereté","Sincelejo","Planeta Rica"],{"nombre":"Juan","edad":25}]
#Operaciones con la lista
print("Operaciones con la lista")
#Referencias los datos en mi lista
print("referencias datos en mi lista")
print(mi_lista)  # Imprime los datos de la lista
print(mi_lista[8])  # Imprime el elemento de la casilla 8
print(mi_lista[7])  # Imprime el elemento de la casilla 7
print(mi_lista[7][2])  # Imprime el elemento sincelejo de la lista dentro de la lista
print(mi_lista[8]["nombre"])  # Imprime el nombre Juan del diccionario dentro de la lista
#Otras Operaciones con la lista
print("Otras operaciones con la lista")
# Agrega un nuevo elemento al final de la lista
mi_lista.append(["Manzana","Mangos", "Pera","Uva","Guineo"]) 
print(mi_lista)  # Imprime la lista actualizada   
#Eliminar un elemnto de la lista
print("Eliminar un elemento de la lista")
mi_lista.remove("cuatro")  # Elimina el elemento "cuatro" de la lista
print("Lista con el elemento eliminado:")
print(mi_lista)  # Imprime la lista actualizada
#Eliminar Una ciudad de la Lista
print("Eliminar una ciudad de la lista")
mi_lista[6].remove("Cereté")  # Elimina "Cereté" de la sublista de ciudades
print("Lista de ciudades actualizada:")
print(mi_lista[6])  # Imprime la sublista de ciudades actualizada

#Modificar elementos de la lista
print("Modificar elementos de la lista")
mi_lista[0] = "Uno"  # Modifica el primer elemento de la lista
print(mi_lista)  # Imprime la lista actualizada
mi_lista[7]["edad"] = 35  # Modifica la edad en el diccionario dentro de la lista
print(mi_lista[7])  # Imprime el diccionario actualizado

#extraer sublistas de mi_lista
print("Extraer sublistas de mi lista")
sublista = mi_lista[3:6]  # Extrae los elementos de la posición 3 a la 5
print(sublista)  # Imprime la sublista extraída

#estructura de colecciones 
print("Estructura de colecciones")
mi_dict = {"nombre": "Ana", "edad": 30}
print(mi_dict)  # Imprime el diccionario
print(mi_dict["nombre"])  # Imprime el valor asociado a la clave "nombre"
print(mi_dict["edad"])  # Imprime el valor asociado a la clave "edad"

#Elimiar una clave del diccionario
del mi_dict["edad"]  # Elimina la clave "edad" del diccionario
print("Diccionario después de eliminar la clave 'edad':")
print(mi_dict)  # Imprime el diccionario actualizado

#manejo de funciones con python
print("Manejo de funciones con Python")
def suma(a, b):
 return a + b
resultado = suma(5, 3)# llama la funcion suma con los argumentos 3 y 5 
print(f"Resultado de la suma: {resultado}")  # Imprime el resultado de la suma

#ejemplo de funciones que no retornan valores
print("Ejemplo de funciones que no retornan valores")
def imprimir_mensaje(mensaje):
    print(mensaje)  # Imprime el mensaje recibido como argumento
imprimir_mensaje("¡Hola desde una función!")  # Llama a la función con un mensaje