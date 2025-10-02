from django.db import models

class Generocliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name='ID')  # Field name made lowercase.
    genero = models.CharField(max_length=50, verbose_name='Genero')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        managed = False
        db_table = 'generoCliente'
        verbose_name = 'Genero de cliente'
        verbose_name_plural = 'Generos de cliente'
        ordering = ['-creado']

    def __str__(self):
            return self.genero

class Cliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    appaterno = models.CharField(db_column='apPaterno', max_length=50, verbose_name='Apellido paterno')  # Field name made lowercase.
    apmaterno = models.CharField(db_column='apMaterno', max_length=50, verbose_name='Apeliido materno')  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento', verbose_name='Fecha de nacimiento')  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=13, verbose_name='RFC')  # Field name made lowercase.
    curp = models.CharField(db_column='CURP', max_length=18, verbose_name='CURP')  # Field name made lowercase.
    generoid = models.ForeignKey(Generocliente, models.DO_NOTHING, db_column='generoID', verbose_name='Genero')  # Field name made lowercase.
    celular = models.CharField(max_length=10, verbose_name='Celular')
    telefono = models.CharField(max_length=10, verbose_name='Telefono')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    codigopostal = models.CharField(db_column='codigoPostal', max_length=5, verbose_name='Código postal')  # Field name made lowercase.
    pais = models.CharField(max_length=50, verbose_name='País')
    estado = models.CharField(max_length=50, verbose_name='Estado')
    municipio = models.CharField(max_length=50, verbose_name='Municipio')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')
    colonia = models.CharField(max_length=50, verbose_name='Colonia')
    calle = models.CharField(max_length=50, verbose_name='Calle')
    numcasa = models.CharField(db_column='numCasa', max_length=50, verbose_name='Número de casa')  # Field name made lowercase.
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-creado']

    def __str__(self):
        return f'{self.nombre} {self.appaterno} {self.apmaterno}'