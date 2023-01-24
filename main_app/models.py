from django.db import models
from django.urls import reverse

class Shoe:  # Note that parens are optional if not inheriting from another class
  def __init__(self, designer, style, description, size):
    self.designer = designer
    self.style = style
    self.description = description
    self.size = size

shoes = [
  Shoe('Nike', 'Air Jordan', 'Women\'s Basketball Sneaker', 8),
  Shoe('GoldenGoose', 'Superstar', 'Low Top Tennis Shoe', 8),
  Shoe('Gucci', 'Lace', 'Combat Boot', 8),
]

# Create your models here.
class Shoe(models.Model):
    designer = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.IntegerField() 

    def __str__(self):
        return self.designer
      
    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})
      