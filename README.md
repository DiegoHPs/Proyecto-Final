# Nombre del Proyecto

HR MANAGER.

# Versión

2.0

# Descripción del Proyecto

- OBJETIVO GENERAL

Simular entorno visual de un modulo de recursos humanos de una empresa
Cargar datos a legajos y llevar registro de capacitaciones y de proyectos donde trabajo la persona (serian 3 tablas y el comun de cada tabla seria el nro de legajo).
Consultar legajos de cada empleado y demas registros.
Dar alta a usuarios.
El admin puede consultar todos los datos con una busqueda. Dar de alta, modificar y dar de baja.


- PAGINAS

Logueo

Dar de alta usuario y contraseña.

Deslogueo.

Vista de su legajo.

Acceso para dar alta, modificar y eliminar registros

Envio de mensajes

Datos del desarrollador

# funcionalidades

Al iniciar la aplicacion se direcciona a la pantalla de logueo. Si el usuario se encuentra ya registrado o ingresa mal los datos solicitara la corrección.
Desde la misma pantalla se puede registrar como usuario nuevo.
Posteriormente y cumpliendo alguno de los pasos anteriores se accede a la pantalla inicial.
Importante!. En cada pantalla se puede acceder a un boton llamado inicio que lleva a la pantalla principar desde cualquier lugar donde este.
Estando logueado se habilitan varios accesos en la barra de navegaion.
El objeto de los accesos mencionados y su funcion estan resumidos en la pantalla inicial como guia para el usuario.
Desde dichos enlaces en la nav se puede:
Ver los datos del desarrollador.
Enviar mensajes para requerir o comentar cuestiones de interes. Se permite acceder sin logueo con el objetivo de contactarse ante un eventual problema al ingresar.
Ver datos de los legajos basicos
De igual modo ver datos ampliados de cada legajo como las capacitaciones realizadas.
Eliminar legajos. En este punto es destacable que al eliminar el legajo base se eliminan en cadena los datos vinculados a ese legajo de las otras tablas vinculados por DNI.
Modificar datos.
Por ultimo, salir del sistema.

# Tecnología.

 # Front

- HTML 5

- CSS 3

- Javascript

- Bootstrap 5.2

 
 # Back

- Python 3.11.14

- Django 4.2.6


# Test

Archivo "testing.xlsx" 

# Video 

https://youtu.be/4scnPTIIgKs