from django.db import models


class Costumer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    costumer_user = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    order_data = models.DateTimeField(auto_now_add=True)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.costumer_user} | price: {self.order_price}"

    """
        
    
    """


