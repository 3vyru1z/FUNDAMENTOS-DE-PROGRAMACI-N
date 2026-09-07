#Sistema de gestión y seguimiento de proyectos
def crear_cuenta():
print("REGISTRTO NUEVA CUENTA")
nuevo_usuario = input("Ingrese un nombre de usuario")
nueva_contrasena = input("Ingrese una contraseña")
if nuevo_usuario and nueva_contrasena:
print("¡Cuenta de '{nuevo_usuario}' registrada con éxito!")
else:
print("Error: Debe llenar todos los campos")

def iniciar_sesion():
  print("Inicio de sesión")
  usuario = input("Ingrese su usario:")
  contrasena = input("Ingrese su contraseña: ")
  if usuario and contrasena:
    print("¡Bienvenido/a, '{usuario}'!")
    return True
  else:
    print("Datos incorrectos")
    return False
    
def registrar_proyecto():
  print("Registra tu proyecto")
  nombre = input ("Nombre del proyecto")
  try:
    avance = float(input("Porcentaje de avance (0-100)")
    if 0 <= avance <= 100:
       print("Proyecto '{nombre}' registrado con {avance: .f}% de avance")
  else:
        print("El porcentaje debe estar entre 0 y 100")
except ValueError:
        print("Error: Por favor ingrese algo válido")

def calcular_metricas():
        print("Cálculo de métricas de tiempo y financieras")
  nombre = input("Nombre del proyecto:")
try:
  metas_total = int(input("Total de metas planificadas:"))
  metas_cumplidas = int(input("Metas alcanzadas:"))
  presupuesto_inicial = int(input("Presupuesto inicial($):"))
  presupuesto_gastado = int(input("Presupuesto gastado($):"))
  dias = int(input("Duración estimada en días del proyecto:"))}

  if metas_total <=0:
    print("Error: Sus metas al menos debe de ser de 1")
    return

    presupuesto_restante = presupuesto_inicial - presupuesto_gastado
    porcentaje_avance = (metas_cumplidas / metas_total) * 100
    semanas = dias // 7
    dias_s = dias % 7

    print("Resumen de métricas: {nombre}")
    print("Avance real de metas: {porcentaje_avance:.2f}%")
    print("Presupuesto disponible: {presupuesto_restante:.2f}%")
    print("Tiempo estimado: {semanas} semanas y {dias_s} dias")

except ValueError:
print("Error: Ingrese datos válidos")

def mostrar_menu():
  print("Sistema de gestión de proyectos y resultados")
  print("1. Crear cuenta")
  print("2. Iniciar sesión")
  print("3. Resgitrar proyecto")
  print("4. Calcular métricas de proyecto (operadores)")
  print("5. Salir")

def main():
  ejecutando = True
while ejecutando:
  mostrar_menu()
opcion = input("Selecciona una opción (1-5):")
if opcion == "1":
  crear_cuenta()
elif opcion == "2":
iniciar_sesion()
elif opcion == "3":
registrar_proyecto()
elif opcion == "4":
calcular_metricas()
elif opcion == "5":
print("Cerrando el programa")
ejecutando = False
else: 
print("Opción no válida")
main()
