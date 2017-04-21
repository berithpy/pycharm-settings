from django.db import models

from mk2_business_logic.models.entidad import Entidad


class Modelo(Entidad):
    nombre = models.TextField()