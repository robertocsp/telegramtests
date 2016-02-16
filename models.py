from django.db import models

# Create your models here.

class Loja(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    razao_social = models.CharField(max_length=100)
    cnpj_cpf = models.IntegerField()
    endereco = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='/var/www/html/logos',height_field=None,width_field=None,max_length=100,blank=True)
    #espaco = models.ManyToManyField(Espaco,blank=True)

    def __unicode__(self):
        return self.nome

class TipoEspaco(models.Model):
    largura = models.IntegerField()
    altura = models.IntegerField()
    profundidade = models.IntegerField()
    tipo = models.CharField(max_length=10)
    preco = models.FloatField()

    def __unicode__(self):
        return self.tipo

class Espaco(models.Model):
    identificador = models.CharField(max_length=20)
    tipo = models.ForeignKey(TipoEspaco)
    loja = models.ForeignKey(Loja)

    def __unicode__(self):
        return u'%s %s' % (self.identificador, self.tipo)


class Periodo(models.Model):
    nome = models.CharField(max_length=30)
    de = models.DateField(auto_now=False,auto_now_add=False)
    ate = models.DateField(auto_now=False,auto_now_add=False)

    def __unicode__(self):
        return self.nome

class Alocacao(models.Model):
    data_alocacao = models.DateField()
    marca = models.ForeignKey(Marca)
    espaco = models.ManyToManyField(Espaco)
    periodo = models.ManyToManyField(Periodo)

