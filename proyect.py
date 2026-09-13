# Sistema de gestión y seguimiento de proyectos
# Sección 0: Subfunciones de cálculos (Avance 3)
def calcular_restante(inicial, gastado):
    return inicial - gastado
def calcular_porcentaje(cumplidas, total):
    return (cumplidas / total) * 100
def calcular_semanas(dias):
    return dias // 7
def calcular_dias_sobrantes(dias, semanas):
    return dias - (semanas * 7)
# Sección 1: Autenticación y registro
def crear_cuenta():
    print("REGISTRO NUEVA CUENTA")
    nuevo_usuario = input("Ingrese un nombre de usuario: ")
    nueva_contrasena = input("Ingrese una contraseña: ")
    if nuevo_usuario and nueva_contrasena:
        print(f"¡Cuenta de '{nuevo_usuario}' registrada con éxito!")
    else:
        print("Error: Debe llenar todos los campos")
def iniciar_sesion():
    print("INICIO DE SESIÓN")
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario and contrasena:
        print(f"¡Bienvenido/a, '{usuario}'!")
        return True
    else:
        print("Datos incorrectos")
        return False
def registrar_proyecto():
    print("REGISTRA TU PROYECTO")
    nombre = input("Nombre del proyecto: ")
    try:
        avance = float(input("Porcentaje de avance (0-100): "))
        if 0 <= avance <= 100:
            print(f"Proyecto '{nombre}' registrado con {avance:.1f}% de avance") #.1f sirve para mostrar un decimal
        else:
            print("El porcentaje debe estar entre 0 y 100")
    except ValueError:
        print("Error: Por favor ingrese un número válido")
# Sección 2: Métricas
def calcular_metricas():
    print("CÁLCULO DE MÉTRICAS DE TIEMPO Y FINANCIERAS")
    nombre = input("Nombre del proyecto: ")
    try:
        metas_total = int(input("Total de metas planificadas: "))
        metas_cumplidas = int(input("Metas alcanzadas: "))
        presupuesto_inicial = int(input("Presupuesto inicial ($): "))
        presupuesto_gastado = int(input("Presupuesto gastado ($): "))
        dias = int(input("Duración estimada en días del proyecto: "))
        if metas_total <= 0:
            print("Error: Sus metas al menos deben ser 1")
            return
        # Funciones del avance 3
        presupuesto_restante = calcular_restante(
            presupuesto_inicial, presupuesto_gastado
        )
        porcentaje_avance = calcular_porcentaje(metas_cumplidas, metas_total)
        semanas = calcular_semanas(dias)
        dias_s = calcular_dias_sobrantes(dias, semanas)
        print("RESUMEN DE RESULTADOS")
        print(f"Resumen de métricas: {nombre}")
        print(f"Avance real de metas: {porcentaje_avance:.2f}%") #.2fsirve para mostrar dos decimales
        print(f"Presupuesto disponible: ${presupuesto_restante}")
        print(f"Tiempo estimado: {semanas} semanas y {dias_s} días")
    except ValueError:
        print("Error: Ingrese números enteros válidos")
# Sección 3: Menú principal
def mostrar_menu():
    print("  SISTEMA DE GESTIÓN DE PROYECTOS")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. Registrar proyecto")
    print("4. Calcular métricas de proyecto")
    print("5. Salir")
def main():
    print("PROGRAMA INICIADO CORRECTAMENTE")
    ejecutando = True
    while ejecutando:
        mostrar_menu()
        opcion = input("Escribe el número de la opción elegida (1-5): ")
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
            print("Opción no válida. Por favor escribe un número del 1 al 5.")
# Ejecución del programa
main()
