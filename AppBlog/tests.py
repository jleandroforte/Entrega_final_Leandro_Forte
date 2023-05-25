from django.test import TestCase

# Create your tests here.

from django.test import TestCase

from .models import Articulo

class ArticuloTest(Articulo): 
    
    def test_crear_articulo(self): 
        articulo = Articulo(titulo='Titulo', subtitulo='subtitulo', cuerpo='cuerpo', fecha='fecha', autor='autor')
        articulo.save()
        
        self.assertEqual(Articulo.objects.count(), 1)
        self.assertEqual(articulo.titulo, "Titulo1")
        self.assertEqual(articulo.subtitulo, 'subtitulo')
        self.assertEqual(articulo.cuerpo, 'cuerpo')
        self.assertEqual(articulo.fecha, 'fecha')
        self.assertEqual(articulo.autor, 'autor')

def test_articulo_str(self):
       articulo = Articulo(titulo='Titulo1', subtitulo='subtitulo1', cuerpo='cuerpo1', fecha='2023-05-25', autor='Leandro')
       articulo.save()

       # Compruebo el str funciona como se desea
       self.assertEqual(articulo.__str__(), "Titulo1 | subtitulo1 |cuerpo1 |2023-05-25|Leandro ")

        

