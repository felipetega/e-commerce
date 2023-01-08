from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.conf import settings
#from products.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_delete


class Product(models.Model):
    product_id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # produto_quantidade = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=9, decimal_places=2)
    product_score = models.IntegerField()
    product_img = models.ImageField()

    def __str__(self):
        return f"{self.product_name}"


User = settings.AUTH_USER_MODEL
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    ordered = models.BooleanField(default=False)
    fee = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    total_price = models.FloatField(default=0)

    #def __str__(self):
        #return str(self.user.username) + " " + str(self.total_price)

    def __str__(self):
        return f"{str(self.user)}'s cart"



class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)


    #def __str__(self):
        #return str(self.user.username) + " " + str(self.price)

    def __str__(self):
        return f"{str(self.product)} | Quantidade: {str(self.quantity)} | Subtotal: R${str(self.price)}"


@receiver(pre_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    print(cart_items)

    price_of_product = Product.objects.get(product_id=cart_items.product.product_id)
    cart_items.price = cart_items.quantity * float(price_of_product.product_price)

    list_item = CartItems.objects.all()
    #print(list_item)
    cart = Cart.objects.get(id = cart_items.cart.id)
    total_price = cart_items.price
    # print(total_price)
    for i in list_item:
        # if i.product.id != cart_items.product.id:
            total_price =total_price+ float(i.product.product_price)
    cart.total_price = round(total_price,2)
    cart.save()
    

@receiver(post_save, sender=CartItems)
def correct_price_post(sender, **kwargs): 
    cart_items = kwargs['instance']
    cart = Cart.objects.get(id = cart_items.cart.id)
    list_item = CartItems.objects.filter(cart=cart)
    total_price = 0
    for i in list_item:
            total_price = total_price + i.price
    cart.total_price = round(total_price, 2)
    cart.save()


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


@receiver(post_delete, sender=CartItems)
def update_total_price_on_delete(sender, instance, **kwargs):
    # Recupera o item que está sendo removido e o carrinho ao qual ele pertence
    cart_item = instance
    cart = Cart.objects.get(id=cart_item.cart.id)

    # Calcula o novo valor de total_price com base nos itens restantes no carrinho
    total_price = 0
    for item in CartItems.objects.filter(cart=cart):
        total_price += item.price

    # Atualiza o valor de total_price do carrinho
    cart.total_price = round(total_price, 2)
    cart.save()
