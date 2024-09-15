#creando una lista(se puede modificar)
lista = ["Yesi Windecker", "Soy QA", True,1.62]
#creando una tupla(no se puede modificar)
tupla = ("Yesi Windecker", "Soy QA", True,1.64, "Soy QA")
#es valido para lista(se puede modificar)
lista[3] = "QA automation"
#no es valido(no se puede modificar las tuplas)
#tupla[3] = "QA automation"
#print(lista[3])
print(tupla)

#conjunto(set) datos que no se pueden interar con indice ni modificar el valor de un dato, tampoco se duplican el mismo dato, pueden estar desordenado
conjunto = {"Yesi Windecker", "Soy QA", True,1.64, "Soy QA"}

print(conjunto)

#estructura del dicc es como json en js: key y valor
diccionario = {
    'nombre': "Yesi Windecker",
     'rol': "Soy QA",
     'es_feliz': True,
     'altura': 1.64
}

print(diccionario['nombre'])