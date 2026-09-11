# FUNDAMENTOS-DE-PROGRAMACION
Repositorio
#Sistema de gestión y seguimiento de proyectos sociales 
#Descripción del problema
En iniciativas comunitarias y académicas, el seguimiento de proyectos, la asignación de recursos y la medición de resultados normalmente se gestionan de forma dispersa en herramientas poco apropiadas. Esta falta de centralización dificulta el tomar decisiones, el avance de los objetivos y el control de presupiuestos.
Para resolver esta problemática, se desarrollará un programa interactivo en consola en python. El sistema funcionará como un centro de control dónde los usuarios podrán crear una cuenta, iniciar sesión de forma segura y administrar un portafolio de proyectos organizados con matrices.
#Objetivos:
General:
Desarrollar un programa de consola en python que permita administrar y registrar usuarios con sus respectivos proyectos de impacto social/académico y monitorear sus resultados cuantitativos.
Específicos: 
1. Implementar un módulo de autenticación de usuarios ( registro e inicio de sesión).
2. Diseñar una matriz para el almacenamiento dinámico de los proyectos y sus atributos.
3. Incorporar funciones con paso de parámetros y retornos para el cálculo de estadísticas.
4. Garantizar la persistencia de la información mediante la lectura y escritura de archivos externos.

Pseudocódigo:
SECCIÓN 1 (AUTENTICACIÓN DE USUARIOS)


1.Función crear cuenta


2.Escribir "Registro nueva cuenta"


3.Escribir "Ingrese un nombre de usuario:"


4.Leer nuevo_usuario


5.Escribir "Ingrese una contraseña:"


6.Leer nueva_contraseña


7.Función iniciar sesion



8.Definir usuario cómo input



9.Definir autenticado cómo lógico



10.Escribir inicio de sesión 



11.Escribir "Ingrese su usario:"



12.Leer usuario 



13.Escribir "Ingrese contraseña:"



14.Leer contraseña



15.Si validar usuario entonces



16.Escribir "Bienvenido"



17.Sino



18.Escribir "Datos incorrectos"



19.Fin si 



20.Fin función



21.Función registrar proyecto



22.Escribir "Nombre del proyecto:"



23.Leer nombre



24.Escribir "Porcentaje de avance (0-100):"



25.Leer avance



26.si avance >=0 y avance <= 100 entonces



27.Escribir "Proyecto, nombre, registrado con, avance, % de avance"



28.Sino 



29.Escribir "El porcentaje debe estar entre 0 y 100"



30.Fin si



31.Fin función



32.Función calcular_metricas



33.Escribir "Calculo de métricas de finanzas y tiempo"



34.Escribir "Nombre del proyecto:"



35.Leer nombre



36.Escribir "Total de metas:"



37.Leer metas_total



38.Escribir"Metas alcanzadas:"



39.Leer metas_cumplidas



40.Escribir "Presupuesto inicial($):"



41.Leern presupuesto_inicial



42.Escribir "Presupuesto gastado ($):"



43.Leer presupuesto_gastado



44.Escribir "Duración estimada en días del proyecto:"



45.Leer días


46.Si metas_total <= 0 Entonces



47.Escribir "Error: Sus metas deben ser al menos 1"



48.Sino



49.presupuesto_restante (presupuesto_inicial - presupuesto_gastado)



50.porcentaje_avance (metas_cumplidas / metas_total)*100



51.semanas = dias // 7



52.dias_s = dias % 7



53.Escribir "Resumen de métricas: ", nombre



54.Escribir "Avance real de metas: ", porcentaje_avance, "%"



55.Escribir "Presupuesto disponible : $", presupuesto_restante



56.Escribir "Tiempo estimado: ", semanas, "semanas y", dias_s, "dias"



57.Fin si



58.Fin función



59.Función mostrar_menu



60.Escribir "Sistema de gestión de proyectos y resultados"



61.Escribir "1. Crear cuenta"



62.Escribir "2. Iniciar sesión"



63.Escribir "3. Registrar proyecto"



64.Escribir "4. Cálcular métricas del proyecto (operadores)"



65.Escribir "5. Salir"



66.Fin función



70.Función principal



71.Definir ejecutando como lógico



72.Definir opcion como cadena



73.ejecutando como Verdadero



74.Mientras ejecutando hacer



75.mostrar_menu()



76.Escribir "Selecciona una opción (1-5):"



77.Leer opción



78.Si opcion hacer



79.caso == 1}



80.crear cuenta()



81.caso == 2



82.iniciar_sesion()



83.caso == 3



84.registrar_proyecto()



85.caso == 4



86.calcular_metricas()



87.caso == 5



88.Escribir "Cerrando programa"



89.ejecutando = falso



90.Sino



91.Escribir "Opción no válida"



92.Finsi



93.Fin mientras



94.Fin función



95.Inicio



96.principal()
97.Fin codigo

