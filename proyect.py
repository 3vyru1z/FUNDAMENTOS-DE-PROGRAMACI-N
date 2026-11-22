# Sistema de gestion y seguimiento de proyectos

ARCHIVO_PROYECTOS = (
    "proyectos_guardados.txt"
)  # Guarda el nombre del archivo donde se anotan los proyectos
ARCHIVO_MATRIZ = (
    "matriz_proyectos.txt"
)  # Guarda el nombre del archivo donde se anota la tabla de proyectos

proyectos_registrados = (
    []
)  # Crea una lista vacia para ir guardando los proyectos
matriz_proyectos = (
    []
)  # Crea una tabla vacia (lista dentro de lista) para filas y columnas


def calcular_restante(inicial, gastado):
    # Calcula cuanto dinero queda del presupuesto
    return (
        inicial - gastado
    )  # Resta lo que se gasto a lo que habia al inicio y regresa el resultado


def calcular_porcentaje(cumplidas, total):
    # Calcula que porcentaje de metas se lograron
    return (
        cumplidas / total
    ) * 100.0  # Divide las metas logradas entre el total y multiplica por 100.0


def calcular_semanas(dias):
    # Calcula cuantas semanas completas caben en esos dias
    return (
        dias // 7
    )  # Divide los dias entre 7 sin decimales para sacar las semanas


def calcular_dias_sobrantes(dias, semanas):
    # Calcula cuantos dias quedan sueltos despues de contar las semanas
    return dias - (
        semanas * 7
    )  # Quita los dias de las semanas completas al total de dias


def generar_barra_progreso(porcentaje):
    # Arma una barra visual de 10 partes segun el porcentaje
    limite = max(
        0.0, porcentaje
    )  # Evita que el porcentaje baje de 0.0
    limite = min(
        100.0, limite
    )  # Evita que el porcentaje pase de 100.0
    bloques = int(
        limite // 10
    )  # Calcula cuantas partes llenas (de 0 a 10) lleva la barra
    return "||" * bloques + "||" * (
        10 - bloques
    )  # Junta las partes llenas y las restantes y regresa el texto


def evaluar_salud_presupuesto(inicial, gastado):
    # Revisa como va el dinero del presupuesto segun lo gastado
    if inicial > 0:  # Revisa si el presupuesto inicial es mayor que cero
        porcentaje_gastado = (
            gastado / inicial
        ) * 100.0  # Saca que porcentaje del dinero inicial ya se gasto
    else:  # Si el presupuesto inicial es cero o menos
        porcentaje_gastado = (
            0.0  # Pone 0.0 para no dividir entre cero
        )
    if (
        porcentaje_gastado > 90.0
    ):  # Revisa si ya se gasto mas del 90%
        return (
            "Alerta: Presupuesto casi agotado"
        )  # Regresa aviso de que queda muy poco dinero
    if (
        porcentaje_gastado >= 70.0
    ):  # Revisa si se gasto entre 70% y 90%
        return (
            "Precaucion: Presupuesto en riesgo moderado"
        )  # Regresa aviso de tener cuidado con el gasto
    return (
        "Saludable: Presupuesto bajo control"
    )  # Regresa aviso de que el gasto va bien (menos del 70%)


def crear_cuenta():
    # Pide datos para crear una cuenta nueva y revisa que no esten vacios
    print(
        "REGISTRO NUEVA CUENTA"
    )  # Muestra el titulo para crear cuenta
    nuevo_usuario = input(
        "Ingrese un nombre de usuario: "
    ).strip()  # Pide el nombre de usuario y quita espacios de las orillas
    nueva_contrasena = input(
        "Ingrese una contrasena: "
    ).strip()  # Pide la contrasena y quita espacios de las orillas
    if (
        nuevo_usuario and nueva_contrasena
    ):  # Revisa que se hayan escrito ambos datos
        print(
            f"Cuenta de '{nuevo_usuario}' registrada con exito!"
        )  # Avisa que la cuenta quedo lista
    else:  # Si falta escribir usuario o contrasena
        print(
            "Error: Debe llenar todos los campos"
        )  # Avisa que hay que llenar los dos datos


def iniciar_sesion():
    # Pide usuario y contrasena para entrar al sistema
    print(
        "INICIO DE SESION"
    )  # Muestra el titulo de inicio de sesion
    usuario = input(
        "Ingrese su usuario: "
    ).strip()  # Pide el usuario y quita espacios de las orillas
    contrasena = input(
        "Ingrese su contrasena: "
    ).strip()  # Pide la contrasena y quita espacios de las orillas
    if (
        usuario and contrasena
    ):  # Revisa que ambos campos tengan texto
        print(
            f"Bienvenido/a, '{usuario}'!"
        )  # Saluda al usuario
        return True  # Regresa verdadero para indicar que si entro
    print(
        "Datos incorrectos"
    )  # Avisa que faltaron datos
    return False  # Regresa falso para indicar que no pudo entrar


def registrar_proyecto():
    # Guarda uno o varios proyectos con su porcentaje de avance
    print(
        "REGISTRA TU PROYECTO"
    )  # Muestra el titulo para registrar proyectos
    continuar = (
        "s"  # Empieza con "s" para entrar al ciclo de registro
    )
    while (
        continuar.strip().lower() == "s"
    ):  # Repite el registro mientras el usuario escriba "s"
        nombre = input(
            "Nombre del proyecto: "
        ).strip()  # Pide el nombre del proyecto y quita espacios extras
        try:  # Intenta leer el avance como numero para evitar fallos si escriben letras
            avance = float(
                input("Porcentaje de avance (0-100): ")
            )  # Pide el avance y lo convierte a numero con decimales
            if (
                0.0 <= avance <= 100.0
            ):  # Revisa que el avance este entre 0.0 y 100.0
                barra = generar_barra_progreso(
                    avance
                )  # Crea la barra visual segun el avance
                proyecto = {
                    "nombre": nombre,
                    "avance": avance,
                }  # Guarda el nombre y el avance del proyecto juntos
                proyectos_registrados.append(
                    proyecto
                )  # Mete el proyecto a la lista general
                if (
                    avance == 100.0
                ):  # Revisa si ya llego al 100%
                    estado_inicial = (
                        "Completado"  # Marca el proyecto como completado
                    )
                elif (
                    avance > 0.0
                ):  # Revisa si ya empezo pero no ha terminado
                    estado_inicial = (
                        "En Proceso"  # Marca el proyecto como en proceso
                    )
                else:  # Si el avance es 0.0%
                    estado_inicial = (
                        "Iniciado"  # Marca el proyecto como iniciado
                    )
                fila_matriz = [
                    nombre,
                    f"{avance:.1f}%",
                    estado_inicial,
                ]  # Arma una fila con nombre, avance y estado
                matriz_proyectos.append(
                    fila_matriz
                )  # Mete la fila nueva a la tabla de proyectos
                print(
                    f"Proyecto '{nombre}' registrado con "
                    f"{avance:.1f}% de avance"
                )  # Muestra que el proyecto ya se guardo
                print(
                    f"Progreso visual: [{barra}] {avance:.1f}%"
                )  # Muestra la barra y el porcentaje
            else:  # Si el numero no esta entre 0 y 100
                print(
                    "El porcentaje debe estar entre 0 y 100"
                )  # Avisa que el numero debe estar en ese rango
        except (
            ValueError
        ):  # Si el usuario escribio algo que no es numero
            print(
                "Error: Por favor ingrese un numero valido"
            )  # Avisa que debe escribir un numero
        continuar = input(
            "Desea registrar otro proyecto? (s/n): "
        )  # Pregunta si quiere anotar otro proyecto


def calcular_metricas():
    # Pide datos de un proyecto y muestra sus cuentas de metas, dinero y tiempo
    print(
        "CALCULO DE METRICAS DE TIEMPO Y FINANCIERAS"
    )  # Muestra el titulo de esta seccion
    nombre = input(
        "Nombre del proyecto: "
    ).strip()  # Pide el nombre del proyecto
    try:  # Intenta convertir los datos a numeros enteros
        metas_total = int(
            input("Total de metas planificadas: ")
        )  # Pide cuantas metas se pensaron en total
        metas_cumplidas = int(
            input("Metas alcanzadas: ")
        )  # Pide cuantas metas ya se cumplieron
        presupuesto_inicial = int(
            input("Presupuesto inicial ($): ")
        )  # Pide con cuanto dinero empezaron
        presupuesto_gastado = int(
            input("Presupuesto gastado ($): ")
        )  # Pide cuanto dinero ya se gasto
        dias = int(
            input("Duracion estimada en dias del proyecto: ")
        )  # Pide en cuantos dias se piensa terminar
        if (
            metas_total <= 0
        ):  # Revisa que haya por lo menos 1 meta
            print(
                "Error: Sus metas al menos deben ser 1"
            )  # Avisa que el total de metas no puede ser cero o menor
            return  # Sale de la funcion para no dividir entre cero
        presupuesto_restante = calcular_restante(
            presupuesto_inicial, presupuesto_gastado
        )  # Saca cuanto dinero queda disponible
        porcentaje_avance = calcular_porcentaje(
            metas_cumplidas, metas_total
        )  # Saca el porcentaje de metas cumplidas
        semanas = calcular_semanas(
            dias
        )  # Saca cuantas semanas completas son
        dias_s = calcular_dias_sobrantes(
            dias, semanas
        )  # Saca cuantos dias quedan extra
        barra = generar_barra_progreso(
            porcentaje_avance
        )  # Dibuja la barra de avance
        estatus = evaluar_salud_presupuesto(
            presupuesto_inicial, presupuesto_gastado
        )  # Revisa como esta el presupuesto
        print(
            "RESUMEN DE RESULTADOS"
        )  # Muestra el titulo del resumen
        print(
            f"Resumen de metricas: {nombre}"
        )  # Muestra el nombre del proyecto
        print(
            f"Avance real de metas: [{barra}] "
            f"{porcentaje_avance:.2f}%"
        )  # Muestra la barra y el porcentaje con dos decimales
        print(
            f"Estado del Presupuesto: {estatus}"
        )  # Muestra si el presupuesto va bien o en alerta
        print(
            f"Presupuesto disponible: ${presupuesto_restante}"
        )  # Muestra el dinero que sobra
        print(
            f"Tiempo estimado: {semanas} semanas y {dias_s} dias"
        )  # Muestra la duracion en semanas y dias
    except (
        ValueError
    ):  # Si alguno de los datos no es un numero entero valido
        print(
            "Error: Ingrese numeros enteros validos"
        )  # Avisa que escriba numeros enteros


def ver_historial_proyectos():
    # Muestra en pantalla todos los proyectos guardados hasta ahora
    print(
        "HISTORIAL DE PROYECTOS REGISTRADOS"
    )  # Muestra el titulo del historial
    if (
        not proyectos_registrados
    ):  # Revisa si todavia no hay proyectos guardados
        print(
            "No hay proyectos registrados aun. "
            "Por favor registre un proyecto en la opcion 3."
        )  # Avisa que la lista esta vacia
    else:  # Si ya hay proyectos guardados
        for posicion, proyecto in enumerate(
            proyectos_registrados, 1
        ):  # Recorre cada proyecto poniendole numero desde el 1
            barra = generar_barra_progreso(
                proyecto["avance"]
            )  # Dibuja la barra del avance de ese proyecto
            print(
                f"{posicion}. {proyecto['nombre']} -> "
                f"[{barra}] {proyecto['avance']:.1f}%"
            )  # Muestra el numero, nombre, barra y avance del proyecto


def calcular_estadisticas_lista():
    # Saca el total, promedio, mayor y menor avance de los proyectos
    print(
        "ANALISIS ESTADISTICO DE LA LISTA DE PROYECTOS"
    )  # Muestra el titulo de estadisticas
    if (
        not proyectos_registrados
    ):  # Revisa si hay proyectos en la lista
        print(
            "La lista esta vacia. "
            "Registre proyectos primero en la opcion 3."
        )  # Avisa que no hay datos para calcular
        return  # Sale de la funcion porque no hay proyectos
    lista_avances = [
        proyecto["avance"] for proyecto in proyectos_registrados
    ]  # Junta todos los porcentajes de avance en una lista
    total_proyectos = len(
        proyectos_registrados
    )  # Cuenta cuantos proyectos hay en total
    promedio_avance = (
        sum(lista_avances) / total_proyectos
    )  # Suma todos los avances y divide entre el total para sacar el promedio
    maximo_avance = max(
        lista_avances
    )  # Busca el avance mas alto
    minimo_avance = min(
        lista_avances
    )  # Busca el avance mas bajo
    print(
        f"Total de proyectos almacenados en la lista: "
        f"{total_proyectos}"
    )  # Muestra cuantos proyectos hay guardados
    print(
        f"Promedio general de avance: {promedio_avance:.2f}%"
    )  # Muestra el promedio con dos decimales
    print(
        f"Mayor avance registrado en la lista: {maximo_avance:.1f}%"
    )  # Muestra el avance mas alto
    print(
        f"Menor avance registrado en la lista: {minimo_avance:.1f}%"
    )  # Muestra el avance mas bajo


def ver_matriz_proyectos():
    # Muestra los proyectos acomodados como una tabla con columnas
    print(
        "TABLA DE DATOS  MATRIZ DE PROYECTOS"
    )  # Muestra el titulo de la tabla
    if not matriz_proyectos:  # Revisa si la tabla esta vacia
        print(
            "No hay datos en la matriz de proyectos. "
            "Registre proyectos en la opcion 3."
        )  # Avisa que aun no hay filas en la tabla
        return  # Sale de la funcion si no hay datos
    print("-" * 55)  # Dibuja una linea de guiones para separar
    print(
        f"{'INDICE':<8} | {'NOMBRE':<18} | "
        f"{'AVANCE':<10} | {'ESTADO':<8}"
    )  # Escribe los nombres de las columnas
    print("-" * 55)  # Dibuja otra linea de guiones debajo de los titulos
    for fila_idx, fila in enumerate(
        matriz_proyectos
    ):  # Recorre cada fila de la tabla junto con su numero de fila
        nombre_m = fila[
            0
        ]  # Toma el nombre del proyecto de la primera columna
        avance_m = fila[
            1
        ]  # Toma el avance de la segunda columna
        estado_m = fila[
            2
        ]  # Toma el estado de la tercera columna
        print(
            f"[{fila_idx}]      | {nombre_m:<18} | "
            f"{avance_m:<10} | {estado_m:<8}"
        )  # Imprime una fila completa bien acomodada
    print("-" * 55)  # Dibuja la linea final de la tabla


def actualizar_estados_matriz():
    # Actualiza el estado de todos los proyectos en la tabla segun su avance
    if not matriz_proyectos:  # Revisa si la tabla tiene datos
        return  # Sale de la funcion si esta vacia
    for idx, proyecto in enumerate(
        proyectos_registrados
    ):  # Recorre cada proyecto registrado con su posicion
        avance_val = proyecto[
            "avance"
        ]  # Toma el porcentaje de avance del proyecto
        if avance_val == 100.0:  # Si ya esta al 100%
            matriz_proyectos[idx][
                2
            ] = "Completado"  # Cambia su estado a Completado
        elif avance_val > 0.0:  # Si lleva algo de avance pero no llega a 100%
            matriz_proyectos[idx][
                2
            ] = "En Proceso"  # Cambia su estado a En Proceso
        else:  # Si su avance es 0.0%
            matriz_proyectos[idx][
                2
            ] = "Iniciado"  # Cambia su estado a Iniciado


def resumen_conteo_matriz():
    # Cuenta cuantos proyectos hay en cada estado
    print(
        "RESUMEN Y CONTEO CRUZADO DE PROYECTOS"
    )  # Muestra el titulo del resumen
    if not matriz_proyectos:  # Revisa si hay datos en la tabla
        print(
            "No hay proyectos registrados en la matriz. "
            "Registre proyectos en la opcion 3."
        )  # Avisa que no hay datos para contar
        return  # Sale de la funcion si no hay datos
    actualizar_estados_matriz()  # Pone al dia los estados antes de contar
    conteo_iniciados = (
        0  # Empieza en 0 la cuenta de proyectos iniciados
    )
    conteo_proceso = (
        0  # Empieza en 0 la cuenta de proyectos en proceso
    )
    conteo_completados = (
        0  # Empieza en 0 la cuenta de proyectos completados
    )
    for (
        fila
    ) in (
        matriz_proyectos
    ):  # Revisa cada fila de la tabla
        estado = fila[
            2
        ]  # Toma el estado que esta en la tercera columna
        if estado == "Iniciado":  # Si dice Iniciado
            conteo_iniciados += (
                1  # Suma 1 a los iniciados
            )
        elif estado == "En Proceso":  # Si dice En Proceso
            conteo_proceso += (
                1  # Suma 1 a los que estan en proceso
            )
        elif estado == "Completado":  # Si dice Completado
            conteo_completados += (
                1  # Suma 1 a los completados
            )
    print(
        f"Total de registros procesados: {len(matriz_proyectos)}"
    )  # Muestra cuantos proyectos se contaron en total
    print(
        f"Proyectos en estado 'Iniciado': {conteo_iniciados}"
    )  # Muestra cuantos estan iniciados
    print(
        f"Proyectos en estado 'En Proceso': {conteo_proceso}"
    )  # Muestra cuantos estan en proceso
    print(
        f"Proyectos en estado 'Completado': {conteo_completados}"
    )  # Muestra cuantos estan completados


def buscar_analizar_cadenas():
    # Busca una palabra en los nombres de proyectos y muestra como se ve el texto
    print(
        "BUSQUEDA Y ANALISIS DE CADENAS EN PROYECTOS"
    )  # Muestra el titulo de busqueda de texto
    if not proyectos_registrados:  # Revisa si hay proyectos registrados
        print(
            "No hay proyectos registrados para analizar. "
            "Registre proyectos en la opcion 3."
        )  # Avisa que no hay proyectos para revisar
        return  # Sale de la funcion si la lista esta vacia
    keyword = (
        input("Ingrese una palabra clave para buscar: ")
        .strip()
        .lower()
    )  # Pide la palabra a buscar, quita espacios y la pasa a minusculas
    encontrados = (
        0  # Empieza en 0 la cuenta de proyectos que coinciden
    )
    for (
        proyecto
    ) in (
        proyectos_registrados
    ):  # Revisa uno por uno los proyectos guardados
        nombre_proyecto = proyecto[
            "nombre"
        ]  # Toma el nombre del proyecto
        nombre_mayus = (
            nombre_proyecto.upper()
        )  # Pone todo el nombre en mayusculas
        nombre_formateado = (
            nombre_proyecto.title()
        )  # Pone en mayuscula la primera letra de cada palabra
        longitud_nombre = len(
            nombre_proyecto
        )  # Cuenta cuantas letras o espacios tiene el nombre
        if (
            keyword in nombre_proyecto.lower()
        ):  # Revisa si la palabra buscada aparece dentro del nombre
            encontrados += (
                1  # Suma 1 a los proyectos encontrados
            )
            print(
                f"\n--- REPORTE DE CADENA [{encontrados}] ---"
            )  # Muestra el encabezado del resultado
            print(
                f"  * Nombre original:    '{nombre_proyecto}'"
            )  # Muestra el nombre tal como se escribio
            print(
                f"  * Formato Titulo:     '{nombre_formateado}'"
            )  # Muestra el nombre con inicial mayuscula en cada palabra
            print(
                f"  * Todo en Mayusculas: '{nombre_mayus}'"
            )  # Muestra el nombre todo en mayusculas
            print(
                f"  * Total caracteres:   {longitud_nombre}"
            )  # Muestra cuantas letras y espacios tiene
            print(
                f"  * Avance registrado:  "
                f"{proyecto['avance']:.1f}%"
            )  # Muestra el avance del proyecto
            print(
                "-" * 35
            )  # Dibuja una linea de guiones para separar resultados
    if (
        encontrados == 0
    ):  # Si no se encontro ningun proyecto con esa palabra
        print(
            f"No se encontraron proyectos que coincidan "
            f"con '{keyword}'."
        )  # Avisa que no hubo coincidencias
    else:  # Si se encontro al menos uno
        print(
            f"\nBusqueda finalizada. "
            f"Total de coincidencias: {encontrados}"
        )  # Muestra cuantos proyectos coincidieron


def guardar_datos_archivos():
    # Guarda los proyectos y la tabla en archivos de texto
    print(
        "GUARDAR PROYECTOS Y MATRIZ EN ARCHIVO"
    )  # Muestra el titulo para guardar en archivo
    if (
        not proyectos_registrados
    ):  # Revisa si hay proyectos guardados en el programa
        print(
            "No hay proyectos en memoria para guardar. "
            "Registre proyectos primero."
        )  # Avisa que no hay nada que guardar
        return  # Sale de la funcion si no hay proyectos
    actualizar_estados_matriz()  # Pone al dia los estados de la tabla antes de guardar
    try:  # Intenta guardar los archivos en la carpeta
        with open(
            ARCHIVO_PROYECTOS, "w", encoding="utf-8"
        ) as archivo_p:  # Abre el archivo de proyectos para escribir desde cero
            for (
                proyecto
            ) in (
                proyectos_registrados
            ):  # Recorre cada proyecto guardado
                linea = f"{proyecto['nombre']}|{proyecto['avance']}\n"  # Prepara una linea con nombre, barra y avance
                archivo_p.write(
                    linea
                )  # Escribe esa linea en el archivo de proyectos
        with open(
            ARCHIVO_MATRIZ, "w", encoding="utf-8"
        ) as archivo_m:  # Abre el archivo de la tabla para escribir desde cero
            for (
                fila
            ) in (
                matriz_proyectos
            ):  # Recorre cada fila de la tabla
                linea_m = f"{fila[0]}|{fila[1]}|{fila[2]}\n"  # Prepara una linea con las tres columnas separadas por barra
                archivo_m.write(
                    linea_m
                )  # Escribe esa fila en el archivo de la tabla
        print(
            f"Datos guardados en '{ARCHIVO_PROYECTOS}' "
            f"y '{ARCHIVO_MATRIZ}'."
        )  # Avisa que los dos archivos ya se guardaron
    except OSError as error_archivo:  # Si hubo algun problema al crear o escribir los archivos
        print(
            f"Error al escribir archivos: {error_archivo}"
        )  # Muestra que fallo al guardar


def cargar_datos_archivos():
    # Lee los proyectos y la tabla desde los archivos de texto
    print(
        "CARGAR PROYECTOS Y MATRIZ DESDE ARCHIVO"
    )  # Muestra el titulo para cargar desde archivo
    try:  # Intenta abrir y leer el archivo de proyectos
        with open(
            ARCHIVO_PROYECTOS, "r", encoding="utf-8"
        ) as archivo_p:  # Abre el archivo de proyectos solo para leerlo
            proyectos_cargados = (
                []
            )  # Crea una lista vacia para ir guardando lo que se lea
            for (
                linea
            ) in archivo_p:  # Lee el archivo linea por linea
                limpia = (
                    linea.strip()
                )  # Quita espacios y saltos de renglon de la linea
                if (
                    limpia
                ):  # Revisa que el renglon no este vacio
                    partes = limpia.split(
                        "|"
                    )  # Separa el texto donde haya una barra "|"
                    if (
                        len(partes) == 2
                    ):  # Revisa que vengan dos datos: nombre y avance
                        nombre_p = partes[
                            0
                        ].strip()  # Toma el nombre del proyecto sin espacios extras
                        avance_p = float(
                            partes[1].strip()
                        )  # Convierte el avance a numero con decimales
                        proyectos_cargados.append(
                            {
                                "nombre": nombre_p,
                                "avance": avance_p,
                            }
                        )  # Agrega el proyecto leido a la lista temporal
    except (
        FileNotFoundError
    ):  # Si todavia no existe el archivo de proyectos
        print(
            f"No se encontro el archivo '{ARCHIVO_PROYECTOS}'."
        )  # Avisa que no encontro el archivo
        return  # Sale de la funcion porque no hay archivo que leer
    except (
        OSError,
        ValueError,
    ) as error_lectura:  # Si hubo error al leer o al pasar el avance a numero
        print(
            f"Error al leer el archivo: {error_lectura}"
        )  # Muestra el error que ocurrio
        return  # Sale de la funcion por el error

    matriz_cargada = (
        []
    )  # Crea una lista vacia para las filas de la tabla
    try:  # Intenta abrir y leer el archivo de la tabla
        with open(
            ARCHIVO_MATRIZ, "r", encoding="utf-8"
        ) as archivo_m:  # Abre el archivo de la tabla solo para leerlo
            for (
                linea_m
            ) in archivo_m:  # Lee la tabla linea por linea
                limpia_m = (
                    linea_m.strip()
                )  # Quita espacios y saltos de renglon
                if (
                    limpia_m
                ):  # Revisa que el renglon tenga texto
                    campos = limpia_m.split(
                        "|"
                    )  # Separa las columnas donde haya "|"
                    if (
                        len(campos) == 3
                    ):  # Revisa que tenga tres columnas
                        matriz_cargada.append(
                            [
                                campos[0].strip(),
                                campos[1].strip(),
                                campos[2].strip(),
                            ]
                        )  # Agrega la fila a la tabla temporal
    except (
        FileNotFoundError
    ):  # Si no existe el archivo de la tabla, la arma con los proyectos cargados
        for (
            proyecto
        ) in (
            proyectos_cargados
        ):  # Recorre los proyectos que se acaban de cargar
            avance_val = proyecto[
                "avance"
            ]  # Toma el avance del proyecto
            if avance_val == 100.0:  # Si esta al 100%
                estado_c = (
                    "Completado"  # Pone estado Completado
                )
            elif avance_val > 0.0:  # Si tiene algo de avance
                estado_c = (
                    "En Proceso"  # Pone estado En Proceso
                )
            else:  # Si esta en 0.0%
                estado_c = (
                    "Iniciado"  # Pone estado Iniciado
                )
            matriz_cargada.append(
                [
                    proyecto["nombre"],
                    f"{avance_val:.1f}%",
                    estado_c,
                ]
            )  # Agrega la fila armada a la tabla temporal
    except OSError as error_mat:  # Si hubo error al leer el archivo de la tabla
        print(
            f"Error al leer matriz: {error_mat}"
        )  # Muestra el error al leer la tabla
        return  # Sale de la funcion si hubo error

    proyectos_registrados.clear()  # Borra lo que habia antes en la lista de proyectos
    proyectos_registrados.extend(
        proyectos_cargados
    )  # Pone los proyectos cargados del archivo en la lista principal
    matriz_proyectos.clear()  # Borra lo que habia antes en la tabla
    matriz_proyectos.extend(
        matriz_cargada
    )  # Pone las filas cargadas del archivo en la tabla principal
    print(
        f"Se cargaron {len(proyectos_registrados)} "
        f"proyectos correctamente."
    )  # Muestra cuantos proyectos se cargaron


def mostrar_menu():
    # Muestra en pantalla todas las opciones del programa
    print(
        "  SISTEMA DE GESTION DE PROYECTOS"
    )  # Muestra el titulo del menu
    print(
        "1. Crear cuenta"
    )  # Muestra la opcion 1
    print(
        "2. Iniciar sesion"
    )  # Muestra la opcion 2
    print(
        "3. Registrar proyecto (Con ciclo)"
    )  # Muestra la opcion 3
    print(
        "4. Calcular metricas de proyecto"
    )  # Muestra la opcion 4
    print(
        "5. Ver historial de proyectos"
    )  # Muestra la opcion 5
    print(
        "6. Ver estadisticas de las listas"
    )  # Muestra la opcion 6
    print(
        "7. Ver matriz de proyectos en tabla"
    )  # Muestra la opcion 7
    print(
        "8. Actualizar estados de proyectos en lote"
    )  # Muestra la opcion 8
    print(
        "9. Ver resumen y conteo cruzado"
    )  # Muestra la opcion 9
    print(
        "10. Buscar y analizar cadenas en proyectos"
    )  # Muestra la opcion 10
    print(
        "11. Guardar proyectos en archivo"
    )  # Muestra la opcion 11
    print(
        "12. Cargar proyectos desde archivo"
    )  # Muestra la opcion 12
    print(
        "13. Salir"
    )  # Muestra la opcion 13


def main():
    # Arranca el programa y repite el menu hasta que el usuario decida salir
    print(
        "PROGRAMA INICIADO CORRECTAMENTE"
    )  # Muestra mensaje de que el programa ya inicio
    ejecutando = (
        True  # Deja encendido el ciclo del menu
    )
    while (
        ejecutando
    ):  # Repite el menu mientras ejecutando sea verdadero
        mostrar_menu()  # Dibuja el menu en pantalla
        opcion = input(
            "Escribe el numero de la opcion elegida (1-13): "
        ).strip()  # Lee el numero que eligio el usuario y quita espacios
        if opcion == "1":  # Si eligio la 1
            crear_cuenta()  # Abre la funcion para crear cuenta
        elif opcion == "2":  # Si eligio la 2
            iniciar_sesion()  # Abre la funcion para iniciar sesion
        elif opcion == "3":  # Si eligio la 3
            registrar_proyecto()  # Abre la funcion para registrar proyectos
        elif opcion == "4":  # Si eligio la 4
            calcular_metricas()  # Abre la funcion para calcular metricas
        elif opcion == "5":  # Si eligio la 5
            ver_historial_proyectos()  # Abre la funcion para ver el historial
        elif opcion == "6":  # Si eligio la 6
            calcular_estadisticas_lista()  # Abre la funcion de estadisticas
        elif opcion == "7":  # Si eligio la 7
            ver_matriz_proyectos()  # Abre la funcion para ver la tabla
        elif opcion == "8":  # Si eligio la 8
            actualizar_estados_matriz()  # Pone al dia los estados de la tabla
            print(
                "Estados actualizados en lote correctamente!"
            )  # Avisa que se actualizaron los estados
        elif opcion == "9":  # Si eligio la 9
            resumen_conteo_matriz()  # Muestra el conteo por estado
        elif opcion == "10":  # Si eligio la 10
            buscar_analizar_cadenas()  # Abre la funcion para buscar y revisar texto
        elif opcion == "11":  # Si eligio la 11
            guardar_datos_archivos()  # Guarda los datos en los archivos de texto
        elif opcion == "12":  # Si eligio la 12
            cargar_datos_archivos()  # Carga los datos desde los archivos de texto
        elif opcion == "13":  # Si eligio la 13
            print(
                "Cerrando el programa"
            )  # Muestra mensaje de despedida
            ejecutando = (
                False  # Apaga el ciclo para terminar el programa
            )
        else:  # Si escribio otro numero o letra que no esta en el menu
            print(
                "Opcion no valida. "
                "Por favor escribe un numero del 1 al 13."
            )  # Avisa que la opcion no es valida
        input(
            "\nPresiona enter para continuar.\n"
        )  # Espera a que presione Enter antes de seguir
        print(
            "\n" * 2
        )  # Deja dos renglones en blanco para separar


main()  # Llama a main para que empiece a correr todo el programa
