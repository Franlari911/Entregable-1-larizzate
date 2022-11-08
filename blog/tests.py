from django.test import TestCase

# Create your tests here.from datetime import datetime
from django.test import TestCase
from blog.models import AutosNuevo


class ViewTestCase(TestCase):

    def test_crear_auto(self):
        AutosNuevo.objects.create(modelo="Cronos", marca="Fiat")
        todos_los_autos = AutosNuevo.objects.all()
        assert len(todos_los_autos) == 1
        assert todos_los_autos[0].modelo == "Cronos"


    def test_crear_auto_sin_color(self):
        AutosNuevo.objects.create(marca="Volkswagen", modelo="Amarok")
        todos_los_autos = AutosNuevo.objects.all()
        assert todos_los_autos[0].color is None


    def test_crear_4_autos(self):
        AutosNuevo.objects.create(marca="Ford", modelo=1)
        AutosNuevo.objects.create(marca="Fiat", modelo=2)
        AutosNuevo.objects.create(marca="Toyota", modelo=3)
        AutosNuevo.objects.create(marca="Lexus", modelo=4)
        AutosNuevo.objects.create(marca="Pagani", modelo=5)
        todos_los_autos = AutosNuevo.objects.all()
        assert len(todos_los_autos) == 4
