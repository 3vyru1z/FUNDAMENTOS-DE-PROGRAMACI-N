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
