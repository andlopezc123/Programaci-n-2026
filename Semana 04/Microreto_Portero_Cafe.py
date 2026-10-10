"""Microreto: el portero del café."""

nombre = input("¿Como te llamas?; "). upper(). strip()
eneria = int(input("'Canta energia tienes de 0 a 100: "))
trae_cafe = input("¿Trae su cafe (si/no)?: ").lower().strip() == "si"

mensaje = ""
#Si yo vengo con menos del 50 por ciento de energia, y no tengo cafe, por favor vaya y me mandan a descansar
if energia < 50 and not(trae_cafe):  #trae_cafe == False
    mensaje = "Acceso Denegado: Necesitas cafe o dormir"
#si voy con 50 o mas, me dan acceso o que tenga un cafe
    elif energia > 50 or trae_cafe:
        mensaje = "Acceso permitido, pero invita a el cafe"
#cualquier otro escenario: Portero confundido: revisar respuestas
else:
    mensaje "portero confundido: revise sus respuestas"
    
print(f"{nombre}: {mensaje}")