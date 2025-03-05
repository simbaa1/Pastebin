from django.test import TestCase
from django.utils import timezone
from .models import Paste
from .utils import _generate_slug
from django.contrib.auth import get_user_model


class PasteModelTest(TestCase):
    
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="foo", password="bar")
        self.paste = Paste.objects.create(content="Paste item")
        self.paste.author = self.user

    def testPasteModel(self):
        self.assertEquals(str(self.paste), 'Paste item')
        self.assertTrue(isinstance(self.paste, Paste))

    def test_paste_has_slug(self):
        """ Pastes are given slugs correctly when saving """ 
        self.paste.save() 
        self.assertTrue(self.paste.slug)

    def test_paste_expires(self):
        self.paste.expiry_date = timezone.now()
        self.assertEquals(self.paste.expired, True)
        

    

    