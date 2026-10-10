#Solucion: Mision Kit seguro

nombre = input("Nombre: ").upper().strip()
kit = input("tipo de kit; ").lower().strip()
autorizacion = ("cantidad de kits?: ").lower().strip() == "si"
try:
    cantidad = int(input("cantidad de kits?: "))
except ValueError:
    print("Esa cantidad de kits es invalida, digite del 1 al 100")
    cantidad = -1
try:  
    dias = int(input("Dias de prestamo"))
except ValueError:
    print("Coloque una cantidad de dias valido, digite del 1 al 100")
    dias = -1
    
if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = "Registro rechazado: revise los datos ingresados!"
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f"Solititud aprobada para {nombre}: {cantidad} kit(s) de {kit}"
else:
    resultado = "Solicitud envidad a revisión"
    
print("-" * 50,'\n')
print(resultado)