import  csv

def entre(a):
    while True:
        if a < 0:
            print("EL PORCENTAJE NO PUEDE SER MENOR A 0")
            a = int(input("INGRESE EL VALOR NUEVAMENTE: "))
        elif a > 100:
            print("EL PORCENTAJE NO PUEDE SER MAYOR A 100")
            a = int(input("INGRESE EL VALOR NUEVAMENTE: "))
        else:
            break
        
def categ(a):
    if 0 <= a <= 25:
        categoria = "CHISTE"
    elif 26 <= a <= 50:
        categoria = "ANECDOTA"
    elif 51 <= a <= 75:
        categoria = "PELIGRO"
    elif 76 <= a <= 99:
        categoria = "ATENCION"
    elif a == 100:
        categoria = "ESCLAVITUD"
    print(f"SEGUN EL PORCENTAJE DE EFECTIVIDAD SE LE ASIGNÓ LA CATEGORIA {categoria} ")  
    return a     
    
def estadistica():
    total = 0
    mayor = 0 
    for i in lista:
        porcentaje = int(i['efectividad'])
        total = total + porcentaje
        if porcentaje > mayor:
            mayor = porcentaje
    cantidad = len(lista)
    promedio = total/cantidad
    print(f"EL PROMEDIO DE PORCENTAJES ES {promedio}")
    print(f"EL PLAN CON MAYOR EFECTIVIDAD ES {mayor}")
    
lista = []

while True:
    print(".-.--.-.-.-.-.-. MENU  -..-.-.-.-.-.-.-.")
    print("")
    print("1- AGREGAR PLAN")
    print("2- LISTA DE PLANES")
    print("3- ELIMINAR PLAN POR ID")
    print("4- GENERAR CSV")
    print("5- CARGAR CSV (SE ELIMINARAN DATOS)")
    print("6- ESTADISTICAS")
    print("0- SALIR")
    
    op = int(input("SELECCIONE UNA OPCION DEL MENU: "))
    
    if op == 1:
        id = int(input("INGRESE EL ID DEL PLAN: "))
        nombre = input("INGRESE NOMBRE: ")
        efectividad = int(input("INGRESE PORCENTAJE DE EFECTIVIDAD: "))
        
        entre(efectividad)
        
        categ(efectividad)
        
        diccionario = {'id':id , 'nombre':nombre, 'efectividad':efectividad}
        lista.append(diccionario)
        
    elif op == 2:
        for i in lista:
            print("ID: ",i['id'], "NOMBRE: ",i['nombre'], "EFECTIVIDAD: ",i['efectividad'], "CATEGORIA: ", categ)     
        
    elif op == 3:
        
        eliminar = int(input("INGRESE EL ID DEL PLAN A ELIMINAR: "))
        for i in lista:
            if eliminar == i['id']:
                pregunta = input("¿ESTA SEGURO QUE DESEA ELIMINAR ESTE PLAN? (SI/NO): ").lower()
                if pregunta == "si" or pregunta == "s":
                    lista.remove(i)
                    print("PLAN ELIMINADO CORRECTAMENTE")
                    break
                else:
                    print("NO ELIMINADO")
    
    elif op == 4:
        
        with open("planes.csv", "w", newline="") as planes:
            escritor_csv = csv.writer(planes)
            
            escritor_csv.writerow(["ID", "NOMBRE", "EFECTIVIDAD", "CATEGORIA"])
            escritor_csv.writerows(lista)
            print("ARCHIVO CREADO CORRECTAMENTE...")
        
    elif op == 5:
        
        lista.clear
        with open("planes.csv", "r", newline="") as planes:
            leercsv = csv.reader(planes)
            for i in leercsv:
                lista.append(i)
        lista.pop(0)
        for x in lista:
            print("ID: ",x['id'], "NOMBRE: ",x['nombre'], "EFECTIVIDAD: ",x['efectividad'], "CATEGORIA: ", x['categoria'])
        
    elif op == 6:
        estadistica()
    elif op == 0:
        print("")
        print("SALIENDO DEL MENU...")
        break
    else:
        print("HA SELECCIONADO UNA OPCION INVALIDA, VOLVIENDO AL MENU...")
        print("")
        
#https://github.com/mgaliano1/prueba3  link github