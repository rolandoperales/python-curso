peso=float(input ("Peso en Kg:"))
altura=float(input ("Altura:"))

indice=round(peso/(altura**2),2)

print("Tu indice de masa corporal es" + str(indice))

if indice <= 16:
     mensaje = "Criterio de ingreso a hospital"
elif indice >=16 and indice <= 17:
    mensaje = "infrapeso"
elif indice <= 18:
    mensaje = "bajo peso"
elif indice <= 25:
   mensaje = "peso normal"
elif indice <= 30:
     mensaje = "sobrepeso"
elif indice <= 35:
    mensaje = "sobrepeso cronico"
elif indice <= 40:
     mensaje = "obesidad premórbida"
else: 
    mensaje = "obesidad morbida"

print ("HOLA el resultado es " + mensaje )