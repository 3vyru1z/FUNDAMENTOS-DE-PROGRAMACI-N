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
1. Algoritmo Sistema Gestión Proyectos
2. 
3. SECCION 0: SUBFUNCIONES DE CÁLCULOS (AVANCE 3)
4.   Funcion calcular_restante (inicial, gastado)
5.      Entradas: inicial, gastado
6.      Salidas: Resultado de la resta
7.        Retornar inicial - gastado
8.   FunFuncion
9.   Funcion calcular_porcentaje (cumplidas, total)
10.    Entradas: cumplidas, total
11.    Salidas: porcentaje calculado
12.      Retornar (cumplidas / total) *100
13.   Finfuncion
14.   Duncion calcular_semanas (dias)
15.     Entradas: dias
16.     Salidas: total de semanas
17.       Retornar dias / 7
18.   Finfuncion
19.  Funcion calcular_dias_sobrantes (dias, semanas)
20.     Entradas: dias, semanas
21.     Salidas: dias restantes
22.        Retornar dias - (semanas * 7)
23. Finfuncion
24. 
25. SECCION 1: AUTENTICACIÓN Y REGISTRO DE PROYECTOS
26. 
27. Funcion crear_cuenta()
28.     Entradas: nuevo_usuario, nueva_contrasena
29.     Salidas: Mensaje en pantalla
30.     
31.     Escribir "REGISTRO NUEVA CUENTA"
32.    Escribir "Ingrese un nombre de usuario:"
33.    Leer nuevo_usuario
34.    Escribir "Ingrese una contrasena:"
35.    Leer nueva_contrasena
36.    
37.    Escribir "Cuenta registrada con exito para: ", nuevo_usuario
38. FinFuncion
39. 
40. Funcion iniciar_sesion()
41.     Entradas: usuario, contrasena
42.     Salidas: Mensaje en pantalla
43.     
44.     Escribir "INICIO DE SESION"
45.     Escribir "Ingrese su usuario:"
46.     Leer usuario
47.     Escribir "Ingrese contrasena:"
48.     Leer contrasena
49.     
50.     Escribir "Bienvenido, ", usuario
51. FinFuncion
52. 
53. Funcion registrar_proyecto()
54.     Entradas: nombre, avance
55.     Salidas: Mensaje en pantalla
56.     
57.     Escribir "REGISTRO DE PROYECTO"
58.     Escribir "Nombre del proyecto:"
59.     Leer nombre
60.     Escribir "Porcentaje de avance (0 a 100):"
61.     Leer avance
62.     
63.     Si avance >= 0 Y avance <= 100 Entonces
64.         Escribir "Proyecto ", nombre, " registrado con ", avance, "% de avance"
65.     Sino
66.         Escribir "El porcentaje debe estar entre 0 y 100"
67.     FinSi
68. FinFuncion
69. 
70. SECCION 2: METRICAS Y OPERADORES ARITMETICOS
71. 
72. Funcion calcular_metricas()
73.     Entradas: nombre, metas_total, metas_cumplidas, presupuesto_inicial, presupuesto_gastado, dias
74.     Salidas: presupuesto_restante, porcentaje_avance, semanas, dias_s, Resumen en pantalla
75.     
76.     Escribir "CALCULO DE METRICAS DE FINANZAS Y TIEMPO"
77.     Escribir "Nombre del proyecto:"
78.     Leer nombre
79.     Escribir "Total de metas:"
80.     Leer metas_total
81.     Escribir "Metas alcanzadas:"
82.     Leer metas_cumplidas
83.     Escribir "Presupuesto inicial:"
84.     Leer presupuesto_inicial
85.     Escribir "Presupuesto gastado:"
86.     Leer presupuesto_gastado
87.     Escribir "Duracion estimada en dias del proyecto:"
88.     Leer dias
89.     
90.     Si metas_total <= 0 Entonces
91.         Escribir "Error: Sus metas deben ser al menos 1"
92.     Sino
93.         presupuesto_restante = presupuesto_inicial - presupuesto_gastado
94.         porcentaje_avance = (metas_cumplidas / metas_total) * 100
95.         semanas = dias / 7
96.         dias_s = dias MOD 7
97.         
98.         Escribir "Resumen de metricas: ", nombre
99.         Escribir "Avance real de metas: ", porcentaje_avance, "%"
100.         Escribir "Presupuesto disponible: ", presupuesto_restante
101.         Escribir "Tiempo estimado: ", semanas, " semanas y ", dias_s, " dias"
102.     FinSi
103. FinFuncion
104. 
105. SECCION 3: MENU Y FLUJO PRINCIPAL
106. 
107. Funcion mostrar_menu()
108.     Entradas: Ninguna
109.     Salidas: Opciones en pantalla
110.     
111.     Escribir "Sistema de gestion de proyectos y resultados"
112.     Escribir "1. Crear cuenta"
113.     Escribir "2. Iniciar sesion"
114.     Escribir "3. Registrar proyecto"
115.     Escribir "4. Calcular metricas de proyecto"
116.     Escribir "5. Salir"
117. FinFuncion
118. 
119. Funcion principal()
120.     Entradas: opcion
121.     Salidas: Ejecucion de funciones
122.    
123.    ejecutando = Verdadero
124.    
125.    Mientras ejecutando Hacer
126.        mostrar_menu()
127.        Escribir "Selecciona una opcion (1 a 5):"
128.        Leer opcion
129.        
130.        Si opcion == "1" Entonces
131.            crear_cuenta()
132.        FinSi
133.        Si opcion == "2" Entonces
134.            iniciar_sesion()
135.        FinSi
136.        Si opcion == "3" Entonces
137.            registrar_proyecto()
138.        FinSi
139.        Si opcion == "4" Entonces
140.            calcular_metricas()
141.        FinSi
142.        Si opcion == "5" Entonces
143.            Escribir "Cerrando programa"
144.            ejecutando = Falso
145.        FinSi
146.    FinMientras
147. FinFuncion
148. 
149. Inicio
150.     principal()
151. FinFuncion
152. 
