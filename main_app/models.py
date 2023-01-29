from django.db import models
from django.urls import reverse

CLOSETS = (
  ('C1', 'Closet_1'),
  ('C2', 'Closet_2'),
  ('C3', 'Closet_3')
)

# class Shoe:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, designer, style, description, size):
#     self.designer = designer
#     self.style = style
#     self.description = description
#     self.size = size

# shoes = [
#   Shoe('Nike', 'Air Jordan', 'Women\'s Basketball Sneaker', 8),
#   Shoe('GoldenGoose', 'Superstar', 'Low Top Tennis Shoe', 8),
#   Shoe('Gucci', 'Lace', 'Combat Boot', 8),
# ]

# Create your models here.
class Sock(models.Model):
  type = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.type

  def get_absolute_url(self):
    return reverse('socks_detail', kwargs={'pk': self.id})

class Shoe(models.Model):
    designer = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.IntegerField()
    socks = models.ManyToManyField(Sock) 

    def __str__(self):
        return self.designer
      
    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})
      
class Storage(models.Model):
    shelf = models.IntegerField(default=1)
    closet = models.CharField(
          max_length=7,
          choices=CLOSETS,
          default=CLOSETS[0][0]
    )      
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    
    def __str__(self):
      return f"{self.get_closet_display()} on {self.shelf}" 