
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from random import randint

def _generate_slug(instance, model):
     if not instance.slug:
            string_to_slugify = f'{get_random_string(8)} {randint(1, 30)}'
            instance.slug = slugify(string_to_slugify)[:8]
            
            i = 0
            while model.objects.filter(slug=instance.slug).exists():
                instance.slug = string_to_slugify[:8+i]