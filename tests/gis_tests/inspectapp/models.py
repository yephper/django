<<<<<<< HEAD
from ..models import models


class AllOGRFields(models.Model):

    f_decimal = models.FloatField()
    f_float = models.FloatField()
    f_int = models.IntegerField()
    f_char = models.CharField(max_length=10)
    f_date = models.DateField()
    f_datetime = models.DateTimeField()
    f_time = models.TimeField()
    geom = models.PolygonField()
    point = models.PointField()

    objects = models.GeoManager()

    class Meta:
        required_db_features = ['gis_enabled']


class Fields3D(models.Model):
    point = models.PointField(dim=3)
    line = models.LineStringField(dim=3)
    poly = models.PolygonField(dim=3)

    objects = models.GeoManager()

    class Meta:
        required_db_features = ['gis_enabled']
=======
from ..models import models


class AllOGRFields(models.Model):

    f_decimal = models.FloatField()
    f_float = models.FloatField()
    f_int = models.IntegerField()
    f_char = models.CharField(max_length=10)
    f_date = models.DateField()
    f_datetime = models.DateTimeField()
    f_time = models.TimeField()
    geom = models.PolygonField()
    point = models.PointField()

    class Meta:
        required_db_features = ['gis_enabled']


class Fields3D(models.Model):
    point = models.PointField(dim=3)
    line = models.LineStringField(dim=3)
    poly = models.PolygonField(dim=3)

    class Meta:
        required_db_features = ['gis_enabled']
>>>>>>> 6448873197fa4e3df3f5f03201538dc57d7643d6
