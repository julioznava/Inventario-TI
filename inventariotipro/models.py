from django.db import models


opcion_MARCA = [
    ["AOC", "AOC"],
    ["DELL", "DELL"],
    ["GENIUS", "GENIUS"],
    ["LENOVO", "LENOVO"],
    ["LG", "LG"],
    ["LOGITEC", "LOGITEC"],
    ["HP", "HP"],
    ["GENERICO", "GENERICO"],
    ["POLI", "POLI"],
    ["D-LINK", "D-LINK"],
]

opcion_TIPO = [
    ["DESKTOP", "DESKTOP"],
    ["LAPTOP", "LAPTOP"],
]

opcion_so = [
    ["Windows 7", "Windows 7"],
    ["Windows 10", "Windows 10"],
    ["Android", "Android"],
    ["Otros", "Otros"],
]

opcion_HDD = [
    ["100GB", "100GB"],
    ["120GB", "120GB"],
    ["200GB", "200GB"],
    ["250GB", "250GB"],
    ["500GB", "500GB"],
    ["1TB", "1TB"],
]

opcion_RAM = [
    ["2GB", "2GB"],
    ["4GB", "4GB"],
    ["6GB", "6GB"],
    ["8GB", "8GB"],
    ["16GB", "16GB"],
    ["32GB", "32GB"],
]

opcion_PROCESADOR = [
    ["AMD A6-3500", "AMD A6-3500"],
    ["AMD A6-6400", "AMD A6-6400"],
    ["CELERON G1610", "CELERON G1610"],
    ["CELERON G550", "CELERON G550"],
    ["I3 7100U", "I3 7100U"],
    ["I5 8400", "I5 8400"],
    ["I5-1035G1", "I5-1035G1"],
    ["I5-3570", "I5-3570"],
    ["I5-8265U", "I5-8265U"],
    ["RYZEN-5 5500U", "RYZEN-5 5500U"],
]

opcion_ESTADO = [
    ["Nuevo", "Nuevo"],
    ["Usado", "Usado"],
    ["Activo", "Activo"],
    ["Inactivo", "Inactivo"],
    ["Desuso", "Desuso"],
]

opcion_PERIFERICO = [
    ["Audifonos", "Audifonos"],
    ["Adaptador inalambrico", "Adaptador inalambrico"],
    ["Cargadores", "Cargadores"],
    ["Cintillos", "Cintillos"],
    ["Mouse", "Mouse"],
    ["Teclado", "Teclado"],
    ["Webcam", "Webcam"],
]

opcion_TELEFONIA = [
    ["Telefonia fija", "Telefonia fija"],
    ["Telefonia movil", "Telefonia movil"],
]

opcion_DEPARTAMENTOS = [
    ["Informatica","Informatica"],
    ["Corporativo","Corporativo"],
    ["Ventas","Ventas"],
    ["BTA","BTA"],
    ["Grupos","Grupos"],
    ["BTO","BTO"],
    ["Administracion","Administracion"],
    ["Operaciones","Operaciones"],
    ["Gerencia General","Gerencia General"],
    ["KAM","KAM"],
    ["Despacho","Despacho"],
]

opcion_USUARIOS = [
    ["Boggie, Maria Fernanda", "Boggie, Maria Fernanda"],
    ["Bravo, Marta Jimena", "Bravo, Marta Jimena"],
    ["Bustamante, Luis Armando", "Bustamante, Luis Armando"],
    ["Cardenas, Daisy Dayana", "Cardenas, Daisy Dayana"],
    ["Caviedes, Manuel Enrique", "Caviedes, Manuel Enrique"],
    ["Céspedes, Casandra Catalina", "Céspedes, Casandra Catalina"],
    ["Gonzalez, Erica Del Carmen", "Gonzalez, Erica Del Carmen"],
    ["Gonzalez, Margarita Del Carmen", "Gonzalez, Margarita Del Carmen"],
    ["Grandon, Pamela Loreto", "Grandon, Pamela Loreto"],
    ["Hermosilla, Valois Eleazar", "Hermosilla, Valois Eleazar"],
    ["Hernandez, America", "Hernandez, America"],
    ["Jantzent, Fernando", "Jantzent, Fernando"],
    ["Jimenez, Gianina Andrea", "Jimenez, Gianina Andrea"],
    ["Kromschroder, Juan Oscar", "Kromschroder, Juan Oscar"],
    ["Kromschroder, Juan", "Kromschroder, Juan"],
    ["Meneses, Yesenia Jackeline", "Meneses, Yesenia Jackeline"],
    ["Merchan, Gisselle Karolina", "Merchan, Gisselle Karolina"],
    ["Navarro, Julio Esteban", "Navarro, Julio Esteban"],
    ["Olea, Mireya Pamela", "Olea, Mireya Pamela"],
    ["Ramirez, Carlos Rafael", "Ramirez, Carlos Rafael"],
    ["Sanchez, Yineth Esperanza", "Sanchez, Yineth Esperanza"],
    ["Toro, Maritza Soledad", "Toro, Maritza Soledad"],
    ["Valenzuela, Karina Andrea", "Valenzuela, Karina Andrea"],
    ["Vargas, Karina Andrea", "Vargas, Karina Andrea"],
    ["Venegas, Carlos Sebastian", "Venegas, Carlos Sebastian"],
    ["Vera, Nelly", "Vargas, Vera, Nelly"],
    ["Zamora, Francisco Javier", "Zamora, Francisco Javier"],
]


class Equipos(models.Model):
    codigo = models.CharField(max_length=100)
    serieproducto = models.CharField(max_length=100,  blank=True)
    tipo = models.CharField(max_length=50, choices=opcion_TIPO, blank=True, null=True)
    marca = models.CharField(max_length=100, choices=opcion_MARCA)
    modelo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=50, choices=opcion_PROCESADOR)
    sistema_operativo = models.CharField(max_length=100, choices=opcion_so)
    disco_duro = models.CharField(max_length=100, choices=opcion_HDD)
    memoria_ram = models.CharField(max_length=100, choices=opcion_RAM)
    direccion_ip = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)


    def __str__(self):
        return (self.codigo)

class Monitores(models.Model):
    codigo = models.CharField(max_length=100)
    serieproducto = models.CharField(max_length=100, blank=True)
    marca = models.CharField(max_length=100, choices=opcion_MARCA)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.codigo


class Perifericos(models.Model):
    tipo_periferico = models.CharField(max_length=100, choices=opcion_PERIFERICO)
    serieproducto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, choices=opcion_MARCA)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.serieproducto

class Departamento(models.Model):
    departamento = models.CharField(max_length=50, choices=opcion_DEPARTAMENTOS)

    def __str__(self):
        return self.departamento

class Asignacion(models.Model):
    usuarios = models.CharField(max_length=100, choices=opcion_USUARIOS, verbose_name='Asignado')
    departamentos = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE, blank=True, null=True)
    monitor = models.ForeignKey(Monitores, on_delete=models.CASCADE, blank=True, null=True)
    periferico = models.ForeignKey(Perifericos, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return (self.usuarios, self.departamentos, self.equipo, self.monitor, self.periferico)



