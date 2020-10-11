#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import xml.etree.ElementTree as ET
import requests
import matplotlib.pyplot as plt
import matplotlib.axes

def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)
    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    json_data = [{
        "nombre": "Persona1", 
        "apellido": "abc", 
        "DNI": "123", 
        "prenda": [{"prenda": "zapatilla", "cantidad": "2"}, {"prenda": "gorra", "cantidad": "4"}]
        },
        {"nombre": "Persona2", 
        "apellido": "def", 
        "DNI": "456", 
        "prenda": [{"prenda": "zapatilla", "cantidad": "6"}, {"prenda": "medias", "cantidad": "8"}]
        },
        {"nombre": "Persona3", 
        "apellido": "ghi", 
        "DNI": "789", 
        "prenda": [{"prenda": "bufanda", "cantidad": "2"}, {"prenda": "medias", "cantidad": "1"}, {"prenda": "campera", "cantidad": "2"}]
        },
        {"nombre": "Persona4", 
        "apellido": "klm", 
        "DNI": "159", 
        "prenda": [{"prenda": "medias", "cantidad": "15"}, {"prenda": "gorra", "cantidad": "2"}]
        }]

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina
    # Observe el archivo y verifique que se almaceno lo deseado

    with open('prendas.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    pass


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    with open('prendas.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1

    json_print = json.dumps(json_data, indent=4)   
    print(json_print)

    pass


def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.

    ## Creado el archivo prendas.xml

    pass


def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.

    tree = ET.parse('prendas.xml')
    root = tree.getroot()

    print('Recorrer el archivo prendas.xml')
    for child in root:
        print('\nEtiqueta:', child.tag, '\nTexto:', child.text, '\nAtributo:', child.attrib)
        for child2 in child:
            print('\tEtiqueta:', child2.tag, '\n\tTexto:', child2.text, '\n\tAtributo:', child2.attrib)

    pass


def ej5():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    response = requests.get(url)
    json_data = response.json()

    x = [user['userId'] for user in json_data if user['completed'] is True]

    xy_pie = dict.fromkeys(x, 0)

    for i in xy_pie.keys():
        xy_pie[i] = x.count(int(i))

    fig = plt.figure()
    ax = fig.add_subplot()
    
    ax.pie(xy_pie.values(), labels = xy_pie.keys(), 
    autopct = '%1.1f%%', startangle = 90)
    
    ax.set_title('Usuarios por cantidad de libros terminados')
    ax.set_facecolor('whitesmoke')
    
    plt.show()

    pass


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
