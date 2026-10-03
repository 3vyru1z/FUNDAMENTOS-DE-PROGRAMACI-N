# Sistema de gestión y seguimiento de proyectos

# Estructura de datos global para almacenar proyectos guardados
proyectos_registrados = [] # Lista global (como un cuaderno) donde guardaremos los proyectos

# Sección 0: Subfunciones de cálculos (Avance 3)
def calcular_restante(inicial, gastado): # Define función para restar el gasto del presupuesto
    return inicial - gastado # Retorna el resultado de la resta de valores

def calcular_porcentaje(cumplidas, total): # Define función para calcular el porcentaje de metas
    return (cumplidas / total) * 100 # Retorna la división y multiplicación para el porcentaje

def calcular_semanas(dias): # Define función para calcular las semanas completas
    return dias // 7 # Retorna la división entera para calcular semanas

def calcular_dias_sobrantes(dias, semanas): # Define función para calcular los días sobrantes
    return dias - (semanas * 7) # Retorna la resta para obtener días sobrantes

def generar_barra_progreso(porcentaje): # Define función para crear la barra visual
    limite = max(0, porcentaje) # max() elige el número más grande para evitar negativos
    limite = min(100, limite) # min() elige el número más pequeño para no pasar de 100
    bloques = int(limite // 10) # Divide entre 10 para saber cuántos cuadritos pintar de 0 a 10
    return "||" * bloques + "|||" * (10 - bloques) # Repite los cuadritos '||' y rellena los vacíos con '|||'

def evaluar_salud_presupuesto(inicial, gastado): # Define función para evaluar el presupuesto
    porcentaje_gastado = (gastado / inicial) * 100 if inicial > 0 else 0 # Calcula el porcentaje gastado
    if porcentaje_gastado > 90: # (Avance 4) Estructura de decisión: evalúa si excede el 90%
        return "Alerta: Presupuesto casi agotado" # Devuelve aviso rojo si falta poco dinero
    elif porcentaje_gastado >= 70: # (Avance 4) Estructura de decisión: evalúa si está entre 70% y 90%
        return "Precaución: Presupuesto en riesgo moderado" # Devuelve aviso amarillo de cuidado
    else: # (Avance 4) Estructura de decisión: si es menor al 70%
        return "Saludable: Presupuesto bajo control" # Devuelve aviso verde de todo bien

# Sección 1: Autenticación y registro (Avance 1)
def crear_cuenta(): # Define función para registrar usuario
    print("REGISTRO NUEVA CUENTA") # Muestra mensaje de encabezado
    nuevo_usuario = input("Ingrese un nombre de usuario: ") # Solicita y guarda el usuario
    nueva_contrasena = input("Ingrese una contraseña: ") # Solicita y guarda la contraseña
    if nuevo_usuario and nueva_contrasena: # (Avance 4) Estructura de decisión: verifica campos llenos
        print(f"¡Cuenta de '{nuevo_usuario}' registrada con éxito!") # Confirma el registro exitoso
    else: # (Avance 4) Estructura de decisión: ejecuta si falta algún campo
        print("Error: Debe llenar todos los campos") # Advierte que falta completar información

def iniciar_sesion(): # Define función para autenticar usuario
    print("INICIO DE SESIÓN") # Muestra encabezado de inicio
    usuario = input("Ingrese su usuario: ") # Solicita el usuario
    contrasena = input("Ingrese su contraseña: ") # Solicita la contraseña
    if usuario and contrasena: # (Avance 4) Estructura de decisión: valida que ambos campos tengan datos
        print(f"¡Bienvenido/a, '{usuario}'!") # Muestra mensaje de bienvenida
        return True # Devuelve True si la sesión fue exitosa
    else: # (Avance 4) Estructura de decisión: ejecuta si faltan datos
        print("Datos incorrectos") # Informa fallo en autenticación
        return False # Devuelve False si no se inició sesión

def registrar_proyecto(): # Define función para registrar proyecto
    print("REGISTRA TU PROYECTO") # Muestra título de la opción
    nombre = input("Nombre del proyecto: ") # Solicita el nombre del proyecto
    try: # Inicia bloque de prevención de errores
        avance = float(input("Porcentaje de avance (0-100): ")) # Lee y convierte a flotante
        if 0 <= avance <= 100: # (Avance 4) Estructura de decisión: evalúa el rango correcto
            barra = generar_barra_progreso(avance) # Genera la barra llamando a la función
            proyecto = {"nombre": nombre, "avance": avance} # Crea una ficha (diccionario) con los datos
            proyectos_registrados.append(proyecto) # append() agrega la ficha a la lista global
            print(f"Proyecto '{nombre}' registrado con {avance:.1f}% de avance") # Muestra confirmación
            print(f"Progreso visual: [{barra}] {avance:.1f}%") # Muestra la barra pintada
        else: # (Avance 4) Estructura de decisión: si está fuera de rango
            print("El porcentaje debe estar entre 0 y 100") # Muestra advertencia de rango
    except ValueError: # Atrapa error si ingresan texto en vez de número
        print("Error: Por favor ingrese un número válido") # Informa de error de entrada

# Sección 2: Métricas (Avance 2)
def calcular_metricas(): # Define función para calcular métricas
    print("CÁLCULO DE MÉTRICAS DE TIEMPO Y FINANCIERAS") # Imprime título de sección
    nombre = input("Nombre del proyecto: ") # Solicita el nombre del proyecto
    try: # Inicia validación de datos de entrada
        metas_total = int(input("Total de metas planificadas: ")) # Lee total de metas
        metas_cumplidas = int(input("Metas alcanzadas: ")) # Lee metas logradas
        presupuesto_inicial = int(input("Presupuesto inicial ($): ")) # Lee presupuesto inicial
        presupuesto_gastado = int(input("Presupuesto gastado ($): ")) # Lee monto gastado
        dias = int(input("Duración estimada en días del proyecto: ")) # Lee días estimados

        if metas_total <= 0: # (Avance 4) Estructura de decisión: comprueba metas válidas
            print("Error: Sus metas al menos deben ser 1") # Advierte sobre la condición
            return # Detiene la función para evitar división entre cero

        presupuesto_restante = calcular_restante(presupuesto_inicial, presupuesto_gastado) # Resta presupuestos
        porcentaje_avance = calcular_porcentaje(metas_cumplidas, metas_total) # Calcula porcentaje de metas
        semanas = calcular_semanas(dias) # Calcula semanas
        dias_s = calcular_dias_sobrantes(dias, semanas) # Calcula días restantes
        barra = generar_barra_progreso(porcentaje_avance) # Crea la barra visual
        estatus = evaluar_salud_presupuesto(presupuesto_inicial, presupuesto_gastado) # Evalúa el estado del dinero

        print("RESUMEN DE RESULTADOS") # Imprime título del reporte
        print(f"Resumen de métricas: {nombre}") # Muestra el nombre asignado
        print(f"Avance real de metas: [{barra}] {porcentaje_avance:.2f}%") # Imprime barra y porcentaje
        print(f"Estado del Presupuesto: {estatus}") # Muestra la alerta con emoji
        print(f"Presupuesto disponible: ${presupuesto_restante}") # Imprime saldo disponible
        print(f"Tiempo estimado: {semanas} semanas y {dias_s} días") # Imprime desglose de tiempo

    except ValueError: # Atrapa error si la conversión falla
        print("Error: Ingrese números enteros válidos") # Informa error de número

def ver_historial_proyectos(): # Define función para ver los proyectos guardados
    print("HISTORIAL DE PROYECTOS REGISTRADOS") # Imprime encabezado del historial
    if not proyectos_registrados: # (Avance 4) Estructura de decisión: revisa si la lista está vacía
        print("No hay proyectos registrados aún.") # Avisa que no hay nada guardado
    else: # (Avance 4) Estructura de decisión: si sí hay proyectos
        for posicion, p in enumerate(proyectos_registrados, 1): # enumerate() da un número de lista (1, 2, 3..., etc)
            barra = generar_barra_progreso(p["avance"]) # Crea la barra para el porcentaje de cada uno
            print(f"{posicion}. {p['nombre']} -> [{barra}] {p['avance']:.1f}%") # Muestra el número, nombre y barra

# Sección 3: Menú principal (Avance 3)
def mostrar_menu(): # Define función para imprimir opciones
    print("  SISTEMA DE GESTIÓN DE PROYECTOS") # Imprime encabezado principal
    print("1. Crear cuenta") # Imprime opción 1
    print("2. Iniciar sesión") # Imprime opción 2
    print("3. Registrar proyecto") # Imprime opción 3
    print("4. Calcular métricas de proyecto") # Imprime opción 4
    print("5. Ver historial de proyectos") # Imprime opción 5
    print("6. Salir") # Imprime opción 6

def main(): # Define función principal
    print("PROGRAMA INICIADO CORRECTAMENTE") # Notifica inicio del sistema
    ejecutando = True # Variable de control para mantener el ciclo activo
    while ejecutando: # Ciclo mientras ejecutando sea True
        mostrar_menu() # Llama a la función que dibuja el menú
        opcion = input("Escribe el número de la opción elegida (1-6): ") # Lee la selección
        if opcion == "1": # (Avance 4) Estructura de decisión: compara si eligió 1
            crear_cuenta() # Ejecuta registro
        elif opcion == "2": # (Avance 4) Estructura de decisión: compara si eligió 2
            iniciar_sesion() # Ejecuta inicio de sesión
        elif opcion == "3": # (Avance 4) Estructura de decisión: compara si eligió 3
            registrar_proyecto() # Ejecuta registro de proyecto
        elif opcion == "4": # (Avance 4) Estructura de decisión: compara si eligió 4
            calcular_metricas() # Ejecuta cálculo de métricas
        elif opcion == "5": # (Avance 4) Estructura de decisión: compara si eligió 5
            ver_historial_proyectos() # Ejecuta el historial
        elif opcion == "6": # (Avance 4) Estructura de decisión: compara si eligió 6
            print("Cerrando el programa") # Notifica la salida
            ejecutando = False # Rompe el ciclo cambiando la variable a False
        else: # (Avance 4) Estructura de decisión: opción no válida
            print("Opción no válida. Por favor escribe un número del 1 al 6.") # Muestra mensaje de error

# Ejecución del programa
main() # Inicia la función principal
