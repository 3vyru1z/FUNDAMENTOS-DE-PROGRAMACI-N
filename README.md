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
Función crear cuenta
Escribir "Registro nueva cuenta"
Escribir "Ingrese un nombre de usuario:"
Leer nuevo_usuario
Escribir "Ingrese una contraseña:"
Leer nueva_contraseña
Función iniciar sesion
Definir usuario cómo input
Definir autenticado cómo lógico
Escribir inicio de sesión 
Escribir "Ingrese su usario:"
Leer usuario 
Escribir "Ingrese contraseña:"
Leer contraseña
Si validar usuario entonces
Escribir "Bienvenido"
Sino
Escribir "Datos incorrectos"
Fin si 
Fin función
Función registrar proyecto
Escribir "Nombre del proyecto:"
Leer nombre
Escribir "Porcentaje de avance (0-100):"
Leer avance
si avance >=0 y avance <= 100 entonces
Escribir "Proyecto, nombre, registrado con, avance, % de avance"
Sino 
Escribir "El porcentaje debe estar entre 0 y 100"
Fin si
Fin función

Función calcular_metricas
Escribir "Calculo de métricas de finanzas y tiempo"
Escribir "Nombre del proyecto:"
Leer nombre
Escribir "Total de metas:"
Leer metas_total
Escribir"Metas alcanzadas:"
Leer metas_cumplidas
Escribir "Presupuesto inicial($):"
Leern presupuesto_inicial
Escribir "Presupuesto gastado ($):"
Leer presupuesto_gastado
Escribir "Duración estimada en días del proyecto:"
Leer días

Si metas_total <= 0 Entonces
Escribir "Error: Sus metas deben ser al menos 1"
Sino
presupuesto_restante (presupuesto_inicial - presupuesto_gastado)
porcentaje_avance (metas_cumplidas / metas_total)*100
semanas = dias // 7
dias_s = dias % 7
Escribir "Resumen de métricas: ", nombre
Escribir "Avance real de metas: ", porcentaje_avance, "%"
Escribir "Presupuesto disponible : $", presupuesto_restante
Escribir "Tiempo estimado: ", semanas, "semanas y", dias_s, "dias"
Fin si
Fin función

Función mostrar_menu
Escribir "Sistema de gestión de proyectos y resultados"
Escribir "1. Crear cuenta"
Escribir "2. Iniciar sesión"
Escribir "3. Registrar proyecto"
Escribir "4. Cálcular métricas del proyecto (operadores)"
Escribir "5. Salir"
Fin función

Función principal
Definir ejecutando como lógico
Definir opcion como cadena
ejecutando como Verdadero

Mientras ejecutando hacer
mostrar_menu()
Escribir "Selecciona una opción (1-5):"
Leer opción

Si opcion hacer
caso == 1
crear cuenta()
caso == 2
iniciar_sesion()
caso == 3
registrar_proyecto()
caso == 4
calcular_metricas()
caso == 5
Escribir "Cerrando programa"
ejecutando = falso
Sino
Escribir "Opción no válida"
Finsi
Fin mientras
Fin función
 Inicio
 principal()
 Fin codigo

