from django.db import models

class Planets(models.Model):
    class Meta:
        db_table = 'ex10_planets'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(max_length=64, null=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.CharField(max_length=128, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class People(models.Model):
    class Meta:
        db_table = 'ex10_people'
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=32, null=True)
    eye_color = models.CharField(max_length=32, null=True)
    hair_color = models.CharField(max_length=32, null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.IntegerField(null=True, unique=True)
    opening_crawl = models.TextField(null=True)
    characters = models.ManyToManyField(People, related_name='characters')
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()

    def __str__(self):
        return self.title
