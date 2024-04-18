from django.test import TestCase
from .models import Paste
from .utils import _generate_slug

class PasteModelTest(TestCase):
    
    def setUp(self):
        self.paste = Paste.objects.create(content="Paste item")

    def testPasteModel(self):
        self.assertEquals(str(self.paste), 'Paste item')
        self.assertTrue(isinstance(self.paste, Paste))

    def test_paste_has_slug(self):
        """ Pastes are given slugs correctly when saving """ 
        self.paste.save() 
        self.assertTrue(self.paste.slug)

    

    