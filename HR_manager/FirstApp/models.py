from django.db import models
#from django.contrib.auth.models import User

class Hoja1(models.Model):
    #id = models.IntegerField(primary_key=)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField(unique=True)
    nacimiento = models.DateField()
    ingreso = models.DateField()
    

    def __str__(self):
            return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} -  Fecha de Nacimiento: {self.nacimiento} - Fecha de Ingreso: {self.ingreso}"

class Hoja2(models.Model):
    calle = models.CharField(max_length=40)
    altura = models.IntegerField()
    localidad = models.CharField(max_length=40)
    correo = models.EmailField(max_length=40)
    dni = models.ForeignKey(Hoja1, on_delete=models.CASCADE, to_field='dni')

    def __str__(self):
            return f"Calle: {self.calle} - Altura: {self.altura} - Localidad: {self.localidad} - Email: {self.correo} - DNI: {self.dni}"

class Capacitacion(models.Model):
    nombre = models.CharField(max_length=60)
    Horas = models.IntegerField()
    puntaje = models.IntegerField()
    fecha = models.DateField()
    dni = models.ForeignKey(Hoja1, on_delete=models.CASCADE, to_field='dni')

    def __str__(self):
            return f"Nombre de la Capacitacion: {self.nombre} - Cantidad de Horas de Duracion: {self.Horas} - Puntaje: {self.puntaje} - Fecha: {self.fecha} - DNI: {self.dni}"

class Mensaje(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenido
