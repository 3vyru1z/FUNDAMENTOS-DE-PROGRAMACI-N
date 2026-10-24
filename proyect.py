# Sistema de gestión y seguimiento de proyectos

proyectos_registrados = (
    []
)  # [Avance 1 y 6] Declaración de lista global (arreglo unidimensional) para almacenar registros
matriz_proyectos = (
    []
)  # [Avance 7] Declaración de lista anidada (matriz bidimensional) para almacenar filas y columnas


def calcular_restante(inicial, gastado):
    # [Avance 3] Define una función para restar el gasto del presupuesto inicial
    return inicial - gastado  # [Avance 2 y 3] Retorna el resultado numérico de la resta


def calcular_porcentaje(cumplidas, total):
    # [Avance 3] Define una función para calcular el porcentaje de metas logradas
    return (
        cumplidas / total
    ) * 100  # [Avance 2 y 3] Retorna la operación aritmética del porcentaje


def calcular_semanas(dias):
    # [Avance 3] Define una función para calcular las semanas completas
    return dias // 7  # [Avance 2 y 3] Retorna la división entera para obtener las semanas


def calcular_dias_sobrantes(dias, semanas):
    # [Avance 3] Define una función para calcular los días que sobran
    return dias - (
        semanas * 7
    )  # [Avance 2 y 3] Retorna la resta de los días menos las semanas completas


def generar_barra_progreso(porcentaje):
    # [Avance 3] Define una función para crear una representación visual del progreso
    limite = max(
        0, porcentaje
    )  # [Avance 2 y 3] Usa max() para asegurar que el porcentaje no sea menor a 0
    limite = min(
        100, limite
    )  # [Avance 2 y 3] Usa min() para asegurar que el porcentaje no rebase 100
    bloques = int(
        limite // 10
    )  # [Avance 2 y 3] Calcula la cantidad de bloques enteros de 0 a 10
    return "||" * bloques + "||" * (
        10 - bloques
    )  # [Avance 3] Retorna una cadena con caracteres gráficos de barra


def evaluar_salud_presupuesto(inicial, gastado):
    # [Avance 3] Define una función para calificar la salud financiera
    porcentaje_gastado = (
        (gastado / inicial) * 100 if inicial > 0 else 0
    )  # [Avance 2 y 3] Calcula el porcentaje gastado si el presupuesto es mayor a cero
    if (
        porcentaje_gastado > 90
    ):  # [Avance 4] Estructura de decisión evalúa si el gasto supera el 90%
        return "Alerta: Presupuesto casi agotado"  # [Avance 4] Retorna un mensaje de advertencia crítica
    elif (
        porcentaje_gastado >= 70
    ):  # [Avance 4] Estructura de decisión evalúa si está entre el 70% y 90%
        return "Precaución: Presupuesto en riesgo moderado"  # [Avance 4] Retorna un mensaje de precaución
    else:  # [Avance 4] Estructura de decisión caso por defecto si es menor al 70%
        return "Saludable: Presupuesto bajo control"  # [Avance 4] Retorna un mensaje de estado óptimo


def crear_cuenta():
    # [Avance 3] Define una función para el registro de nuevos usuarios
    print("REGISTRO NUEVA CUENTA")  # [Avance 1] Imprime el título del módulo en pantalla
    nuevo_usuario = input(
        "Ingrese un nombre de usuario: "
    ).strip()  # [Avance 1] Solicita y lee el nombre de usuario
    nueva_contrasena = input(
        "Ingrese una contraseña: "
    ).strip()  # [Avance 1] Solicita y lee la contraseña
    if (
        nuevo_usuario and nueva_contrasena
    ):  # [Avance 4] Estructura de decisión verifica que ambos campos tengan texto
        print(
            f"¡Cuenta de '{nuevo_usuario}' registrada con éxito!"
        )  # [Avance 1] Muestra mensaje de éxito
    else:  # [Avance 4] Estructura de decisión se ejecuta si algún campo quedó vacío
        print(
            "Error: Debe llenar todos los campos"
        )  # [Avance 1] Muestra un aviso de error por campos vacíos


def iniciar_sesion():
    # [Avance 3] Define una función para autenticar a un usuario
    print("INICIO DE SESIÓN")  # [Avance 1] Imprime el título del inicio de sesión
    usuario = input(
        "Ingrese su usuario: "
    ).strip()  # [Avance 1] Solicita el nombre de usuario
    contrasena = input(
        "Ingrese su contraseña: "
    ).strip()  # [Avance 1] Solicita la contraseña
    if (
        usuario and contrasena
    ):  # [Avance 4] Estructura de decisión comprueba que no estén vacíos
        print(
            f"¡Bienvenido/a, '{usuario}'!"
        )  # [Avance 1] Muestra el mensaje de bienvenida
        return True  # [Avance 3] Devuelve verdadero confirmando acceso
    else:  # [Avance 4] Estructura de decisión se ejecuta si faltan datos
        print("Datos incorrectos")  # [Avance 1] Imprime aviso de error
        return False  # [Avance 3] Devuelve falso indicando fallo de inicio


def registrar_proyecto():
    # [Avance 3] Define una función para registrar uno o varios proyectos
    print("REGISTRA TU PROYECTO")  # [Avance 1] Muestra el encabezado del registro
    continuar = (
        "s"  # [Avance 5] Inicializa la variable de control del ciclo en "s"
    )
    while (
        continuar.strip().lower() == "s"
    ):  # [Avance 5] Estructura de repetición ciclo para registrar muchos proyectos seguidos
        nombre = input(
            "Nombre del proyecto: "
        ).strip()  # [Avance 1] Solicita el nombre del proyecto
        try:  # [Avance 1] Inicia bloque para manejar errores de entrada numérica
            avance = float(
                input("Porcentaje de avance (0-100): ")
            )  # [Avance 1] Lee y convierte la entrada a número decimal
            if (
                0 <= avance <= 100
            ):  # [Avance 4] Estructura de decisión verifica que el avance esté en el rango permitido
                barra = generar_barra_progreso(
                    avance
                )  # [Avance 3] Llama a la función para obtener la barra gráfica
                proyecto = {
                    "nombre": nombre,
                    "avance": avance,
                }  # [Avance 3 y 6] Estructura de arreglo asociativo (diccionario) con los campos del proyecto
                proyectos_registrados.append(
                    proyecto
                )  # [Avance 6] Operación de listas/arreglos método append() para insertar un elemento al final

                # [Avance 7] Asigna el estado inicial según el porcentaje de avance para la matriz
                estado_inicial = (
                    "Completado"
                    if avance == 100
                    else ("En Proceso" if avance > 0 else "Iniciado")
                )
                fila_matriz = [
                    nombre,
                    f"{avance:.1f}%",
                    estado_inicial,
                ]  # [Avance 7] Crea la fila para la matriz bidimensional
                matriz_proyectos.append(
                    fila_matriz
                )  # [Avance 7] Inserta la fila en la matriz global

                print(
                    f"Proyecto '{nombre}' registrado con {avance:.1f}% de avance"
                )  # [Avance 1] Muestra el avance formateado
                print(
                    f"Progreso visual: [{barra}] {avance:.1f}%"
                )  # [Avance 1] Muestra la barra visual en pantalla
            else:  # [Avance 4] Estructura de decisión se ejecuta si el número está fuera de rango
                print(
                    "El porcentaje debe estar entre 0 y 100"
                )  # [Avance 1] Muestra advertencia de rango válido
        except (
            ValueError
        ):  # [Avance 1] Captura el error si el usuario escribe letras en lugar de números
            print(
                "Error: Por favor ingrese un número válido"
            )  # [Avance 1] Muestra el mensaje de error de formato
        continuar = input(
            "¿Desea registrar otro proyecto? (s/n): "
        )  # [Avance 5] Pregunta si desea repetir el ciclo de registro


def calcular_metricas():
    # [Avance 3] Define una función para calcular métricas financieras y de tiempo
    print(
        "CÁLCULO DE MÉTRICAS DE TIEMPO Y FINANCIERAS"
    )  # [Avance 1] Imprime el título de la sección
    nombre = input(
        "Nombre del proyecto: "
    ).strip()  # [Avance 1] Solicita el nombre del proyecto a evaluar
    try:  # [Avance 1] Inicia bloque de control de errores
        metas_total = int(
            input("Total de metas planificadas: ")
        )  # [Avance 1] Lee el total de metas como número entero
        metas_cumplidas = int(
            input("Metas alcanzadas: ")
        )  # [Avance 1] Lee las metas logradas como entero
        presupuesto_inicial = int(
            input("Presupuesto inicial ($): ")
        )  # [Avance 1] Lee el presupuesto inicial
        presupuesto_gastado = int(
            input("Presupuesto gastado ($): ")
        )  # [Avance 1] Lee el presupuesto gastado
        dias = int(
            input("Duración estimada en días del proyecto: ")
        )  # [Avance 1] Lee los días estimados de duración

        if (
            metas_total <= 0
        ):  # [Avance 4] Estructura de decisión comprueba que las metas sean mayores a cero
            print(
                "Error: Sus metas al menos deben ser 1"
            )  # [Avance 1] Muestra mensaje de error por metas nulas
            return  # [Avance 3] Finaliza la función anticipadamente para evitar errores matemáticos

        presupuesto_restante = calcular_restante(
            presupuesto_inicial, presupuesto_gastado
        )  # [Avance 2 y 3] Obtiene el presupuesto restante llamando a la función
        porcentaje_avance = calcular_porcentaje(
            metas_cumplidas, metas_total
        )  # [Avance 2 y 3] Obtiene el porcentaje de avance llamando a la función
        semanas = calcular_semanas(
            dias
        )  # [Avance 2 y 3] Obtiene las semanas completas llamando a la función
        dias_s = calcular_dias_sobrantes(
            dias, semanas
        )  # [Avance 2 y 3] Obtiene los días sobrantes llamando a la función
        barra = generar_barra_progreso(
            porcentaje_avance
        )  # [Avance 3] Genera la barra visual para el porcentaje obtenido
        estatus = evaluar_salud_presupuesto(
            presupuesto_inicial, presupuesto_gastado
        )  # [Avance 3] Obtiene la evaluación de salud financiera

        print("RESUMEN DE RESULTADOS")  # [Avance 1] Imprime el título del reporte
        print(
            f"Resumen de métricas: {nombre}"
        )  # [Avance 1] Muestra el nombre evaluado
        print(
            f"Avance real de metas: [{barra}] {porcentaje_avance:.2f}%"
        )  # [Avance 1] Imprime la barra y el porcentaje con dos decimales
        print(
            f"Estado del Presupuesto: {estatus}"
        )  # [Avance 1] Imprime el estado financiero obtenido
        print(
            f"Presupuesto disponible: ${presupuesto_restante}"
        )  # [Avance 2] Imprime el dinero restante
        print(
            f"Tiempo estimado: {semanas} semanas y {dias_s} días"
        )  # [Avance 2] Imprime el tiempo desglosado

    except (
        ValueError
    ):  # [Avance 1] Captura errores si los datos ingresados no son números enteros
        print(
            "Error: Ingrese números enteros válidos"
        )  # [Avance 1] Muestra mensaje de error de formato


def ver_historial_proyectos():
    # [Avance 3] Define una función para visualizar el historial guardado
    print(
        "HISTORIAL DE PROYECTOS REGISTRADOS"
    )  # [Avance 1] Imprime el encabezado del historial
    if (
        not proyectos_registrados
    ):  # [Avance 4 y 6] Estructura de decisión evalúa si la lista/arreglo está vacía usando 'not'
        print(
            "No hay proyectos registrados aún. Por favor registre un proyecto en la opción 3."
        )  # [Avance 1] Muestra mensaje de que no hay registros
    else:  # [Avance 4] Estructura de decisión se ejecuta si hay proyectos guardados
        for posicion, p in enumerate(
            proyectos_registrados, 1
        ):  # [Avance 5 y 6] Estructura de repetición y recorrido de listas iteración por elementos e índices
            barra = generar_barra_progreso(
                p["avance"]
            )  # [Avance 3 y 6] Acceso a arreglo asociativo usando la clave ["avance"]
            print(
                f"{posicion}. {p['nombre']} -> [{barra}] {p['avance']:.1f}%"
            )  # [Avance 1 y 6] Lectura e impresión de los elementos del arreglo


def calcular_estadisticas_lista():
    # [Avance 6] Función dedicada exclusivamente al análisis de listas y arreglos
    print("ANÁLISIS ESTADÍSTICO DE LA LISTA DE PROYECTOS")
    if (
        not proyectos_registrados
    ):  # [Avance 4 y 6] Verifica si el arreglo contiene datos
        print(
            "La lista está vacía. Registre proyectos primero en la opción 3."
        )
        return

    lista_avances = [
        p["avance"] for p in proyectos_registrados
    ]  # [Avance 6] Arreglo derivado crea una lista que contiene solo los porcentajes numéricos
    total_proyectos = len(
        proyectos_registrados
    )  # [Avance 6] Operación de listas función len() para obtener la cantidad total de elementos
    promedio_avance = sum(lista_avances) / total_proyectos  # [Avance 2 y 6] Operación de listas sum() para sumar todos los valores del arreglo
    maximo_avance = max(
        lista_avances
    )  # [Avance 6] Operación de listas max() para extraer el valor numérico más alto del arreglo
    minimo_avance = min(
        lista_avances
    )  # [Avance 6] Operación de listas min() para extraer el valor numérico más bajo del arreglo

    print(
        f"Total de proyectos almacenados en la lista: {total_proyectos}"
    )  # [Avance 6] Imprime el tamaño total del arreglo
    print(
        f"Promedio general de avance: {promedio_avance:.2f}%"
    )  # [Avance 6] Imprime el promedio calculado sobre la lista
    print(
        f"Mayor avance registrado en la lista: {maximo_avance:.1f}%"
    )  # [Avance 6] Imprime el valor máximo del arreglo
    print(
        f"Menor avance registrado en la lista: {minimo_avance:.1f}%"
    )  # [Avance 6] Imprime el valor mínimo del arreglo


def ver_matriz_proyectos():
    # [Avance 7] Función para ver la matriz de proyectos en formato de tabla tabular
    print("TABLA DE DATOS  MATRIZ DE PROYECTOS")
    if not matriz_proyectos:
        print(
            "No hay datos en la matriz de proyectos. Registre proyectos en la opción 3."
        )  # [Avance 4 y 7] Valida si la matriz está vacía
        return

    print("-" * 55)
    print(f"{'ÍNDICE':<8} | {'NOMBRE':<18} | {'AVANCE':<10} | {'ESTADO':<8}")
    print("-" * 55)
    for (
        fila_idx,
        fila,
    ) in (
        enumerate(matriz_proyectos)
    ):  # [Avance 5 y 7] Recorrido de filas en la matriz bidimensional
        nombre_m = fila[0]  # [Avance 7] Extrae el nombre de la columna 0
        avance_m = fila[1]  # [Avance 7] Extrae el avance de la columna 1
        estado_m = fila[2]  # [Avance 7] Extrae el estado de la columna 2
        print(
            f"[{fila_idx}]      | {nombre_m:<18} | {avance_m:<10} | {estado_m:<8}"
        )
    print("-" * 55)


def actualizar_estados_matriz():
    # [Avance 7] Función para actualización dinámica de estados en lote usando ciclos anidados sobre la matriz
    if not matriz_proyectos:
        return  # [Avance 4 y 7] Sale de la función si la matriz está vacía
    for i, p in enumerate(
        proyectos_registrados
    ):  # [Avance 5 y 6] Recorre la lista de proyectos registrados
        avance_val = p["avance"]  # [Avance 6] Obtiene el valor del avance numérico
        if avance_val == 100:
            matriz_proyectos[i][2] = (
                "Completado"  # [Avance 7] Actualiza celda de estado a completado si llega a 100
            )
        elif avance_val > 0:
            matriz_proyectos[i][2] = (
                "En Proceso"  # [Avance 7] Actualiza celda de estado si está en progreso
            )
        else:
            matriz_proyectos[i][2] = (
                "Iniciado"  # [Avance 7] Actualiza celda de estado inicial si es cero
            )


def resumen_conteo_matriz():
    # [Avance 7] Función para generar resumen y conteo cruzado por categorías de estado en la matriz
    print("RESUMEN Y CONTEO CRUZADO DE PROYECTOS")
    if not matriz_proyectos:
        print(
            "No hay proyectos registrados en la matriz. Registre proyectos en la opción 3."
        )  # [Avance 4 y 7] Valida si hay datos disponibles
        return
    actualizar_estados_matriz()  # [Avance 7] Sincroniza y actualiza los estados en lote antes del conteo
    conteo_iniciados = 0  # [Avance 1] Inicializa contador para proyectos iniciados
    conteo_proceso = 0  # [Avance 1] Inicializa contador para proyectos en proceso
    conteo_completados = (
        0  # [Avance 1] Inicializa contador para proyectos completados
    )
    for (
        fila
    ) in (
        matriz_proyectos
    ):  # [Avance 5 y 7] Estructura de repetición que recorre cada fila de la matriz bidimensional
        estado = fila[2]  # [Avance 7] Extrae el valor de la columna de estado
        if estado == "Iniciado":
            conteo_iniciados += 1  # [Avance 2] Incrementa el acumulador de iniciados
        elif estado == "En Proceso":
            conteo_proceso += 1  # [Avance 2] Incrementa el acumulador en proceso
        elif estado == "Completado":
            conteo_completados += (
                1  # [Avance 2] Incrementa el acumulador de completados
            )

    print(
        f"Total de registros procesados: {len(matriz_proyectos)}"
    )  # [Avance 6] Imprime el total de filas
    print(
        f"Proyectos en estado 'Iniciado': {conteo_iniciados}"
    )  # [Avance 1] Muestra el conteo cruzado
    print(
        f"Proyectos en estado 'En Proceso': {conteo_proceso}"
    )  # [Avance 1] Muestra el conteo cruzado
    print(
        f"Proyectos en estado 'Completado': {conteo_completados}"
    )  # [Avance 1] Muestra el conteo cruzado


def mostrar_menu():
    # [Avance 3] Define una función para desplegar el menú de opciones
    print("  SISTEMA DE GESTIÓN DE PROYECTOS")  # [Avance 1] Imprime el título general del menú
    print("1. Crear cuenta")  # [Avance 1] Opción 1
    print("2. Iniciar sesión")  # [Avance 1] Opción 2
    print("3. Registrar proyecto (Con ciclo)")  # [Avance 1] Opción 3
    print("4. Calcular métricas de proyecto")  # [Avance 1] Opción 4
    print("5. Ver historial de proyectos")  # [Avance 1] Opción 5
    print("6. Ver estadísticas de las listas")  # [Avance 6] Opción 6 añadida para demostrar operaciones sobre arreglos
    print(
        "7. Ver matriz de proyectos en tabla"
    )  # [Avance 7] Opción 7 para mostrar la matriz completa en tabla
    print(
        "8. Actualizar estados de proyectos en lote"
    )  # [Avance 7] Opción 8 añadida para actualización dinámica
    print(
        "9. Ver resumen y conteo cruzado"
    )  # [Avance 7] Opción 9 añadida para matriz de resumen
    print("10. Salir")  # [Avance 1 y 7] Opción 10 de salida actualizada


def main():
    # [Avance 3] Define la función principal que controla el flujo general del sistema
    print(
        "PROGRAMA INICIADO CORRECTAMENTE"
    )  # [Avance 1] Mensaje de arranque del programa
    ejecutando = (
        True  # [Avance 1] Variable booleana de control para mantener activo el ciclo del menú
    )
    while (
        ejecutando
    ):  # [Avance 5] Estructura de repetición ciclo principal que mantiene el menú corriendo en bucle
        mostrar_menu()  # [Avance 3] Llama a la función para dibujar las opciones en pantalla
        opcion = (
            input("Escribe el número de la opción elegida (1-10): ").strip()
        )  # [Avance 1] Lee la opción seleccionada por el usuario limpiando espacios
        if (
            opcion == "1"
        ):  # [Avance 4] Estructura de decisión evalúa si se eligió la opción 1
            crear_cuenta()  # [Avance 3] Llama a la función de creación de cuenta
        elif (
            opcion == "2"
        ):  # [Avance 4] Estructura de decisión evalúa si se eligió la opción 2
            iniciar_sesion()  # [Avance 3] Llama a la función de inicio de sesión
        elif (
            opcion == "3"
        ):  # [Avance 4] Estructura de decisión evalúa si se eligió la opción 3
            registrar_proyecto()  # [Avance 3] Llama a la función de registro continuo de proyectos
        elif (
            opcion == "4"
        ):  # [Avance 4] Estructura de decisión evalúa si se eligió la opción 4
            calcular_metricas()  # [Avance 3] Llama a la función de cálculo de métricas
        elif (
            opcion == "5"
        ):  # [Avance 4] Estructura de decisión evalúa si se eligió la opción 5
            ver_historial_proyectos()  # [Avance 3 y 6] Llama a la función para mostrar el historial recorriendo la lista
        elif (
            opcion == "6"
        ):  # [Avance 4] Estructura de decisión evalúa si se eligió la opción 6
            calcular_estadisticas_lista()  # [Avance 6] Llama a la función que ejecuta operaciones avanzadas sobre listas
        elif (
            opcion == "7"
        ):  # [Avance 4 y 7] Estructura de decisión evalúa si se eligió la opción 7
            ver_matriz_proyectos()  # [Avance 7] Muestra la matriz de proyectos en formato tabular
        elif (
            opcion == "8"
        ):  # [Avance 4 y 7] Estructura de decisión evalúa si se eligió la opción 8
            actualizar_estados_matriz()  # [Avance 7] Llama a la función de actualización dinámica de estados en lote
            print(
                "¡Estados actualizados en lote correctamente!"
            )  # [Avance 1] Imprime mensaje de éxito
        elif (
            opcion == "9"
        ):  # [Avance 4 y 7] Estructura de decisión evalúa si se eligió la opción 9
            resumen_conteo_matriz()  # [Avance 7] Llama a la función de resumen y conteo cruzado
        elif (
            opcion == "10"
        ):  # [Avance 4 y 7] Estructura de decisión evalúa si se eligió la opción 10
            print(
                "Cerrando el programa"
            )  # [Avance 1] Mensaje de salida del sistema
            ejecutando = (
                False  # [Avance 1] Cambia la variable a False para romper el ciclo while y terminar
            )
        else:  # [Avance 4] Estructura de decisión se ejecuta si ingresan un número fuera del rango 1 al 10
            print(
                "Opción no válida. Por favor escribe un número del 1 al 10."
            )  # [Avance 1] Muestra mensaje de error por opción incorrecta

        input("\nPresiona enter para continuar...\n")
        print("\n" * 2)


main()  # [Avance 3] Ejecuta la función principal para poner en marcha todo el programa
