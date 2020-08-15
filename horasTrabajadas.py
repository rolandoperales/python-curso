horas=int(input ("Horas trabajadas:"))
if horas <= 40:
    suma=(horas*16)
else:
   horas_extra=horas-40
   suma=(40*16)+(horas_extra*20);

print ("HOLA el resultado es " + str(suma) )