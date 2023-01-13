from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.conf import settings
#from products.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_delete
from django.db.models import Sum
from django.db.models import Count



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

PAYMENT_METHOD = (
    ('CC', 'Cartão de Crédito'),
    ('CD', 'Cartão de Débito'),
    ('B', 'Boleto'),
    ('P', 'PIX')
)

ORDER_STATUS = (
    ('1', 'Aguardando pagamento'),
    ('2', 'Mercadoria à caminho'),
    ('3', 'Entregue'),
)

User = settings.AUTH_USER_MODEL
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)
    fee = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return str(self.total_price)




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
        return f"{str(self.product)} | Quantidade: {str(self.quantity)} | {str(self.price)}"



'''
#CREATE CART ??? IS WORKING?
@receiver(post_save, sender=User)
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:
        # Check if the user already has a Cart object
        try:
            instance.cart
        except Cart.DoesNotExist:
            # If the user does not have a Cart object, create one
            cart = Cart.objects.create(user=instance)
            cart.save()
        else:
            # If the user already has a Cart object, do nothing
            pass
'''



# Update fee and subtotal and total_price
@receiver(post_save, sender=CartItems)
def update_cart_fee_and_subtotal(sender, instance, **kwargs):
    # Get the Cart object associated with the CartItems object
    cart = instance.cart
    # Calculate the total value of all CartItems in the Cart
    subtotal = 0
    for item in cart.cartitems_set.all():
        subtotal += item.product.product_price * item.quantity
    # Update the subtotal field of the Cart object
    cart.subtotal = subtotal
    # Calculate the new fee based on the subtotal of the Cart
    if subtotal >= 250:
        fee = 0
    else:
        fee = 10 * cart.cartitems_set.aggregate(Sum('quantity'))['quantity__sum']
    # Update the fee field of the Cart object
    cart.fee = fee
    # Calculate the total price of the Cart
    total_price = subtotal + fee
    # Update the total_price field of the Cart object
    cart.total_price = total_price
    # Save the changes to the Cart object
    cart.save()

#Update CartItem price
@receiver(pre_save, sender=CartItems)
def update_cart_fee_and_subtotal(sender, instance, **kwargs):
    # Get the Cart object associated with the CartItems object
    cart = instance.cart
    #Update CartItem price
    instance.price = instance.product.product_price * instance.quantity
    # Save the changes to the Cart object
    cart.save()

# Update fee and subtotal and total_price ao deletar item do carrinho
@receiver(post_delete, sender=CartItems)
def update_fee_and_subtotal_on_delete(sender, instance, **kwargs):
    # Recupera o item que está sendo removido e o carrinho ao qual ele pertence
    cart_item = instance
    cart = Cart.objects.get(id=cart_item.cart.id)

    # Calcula o novo valor de subtotal com base nos itens restantes no carrinho
    subtotal = 0
    for item in CartItems.objects.filter(cart=cart):
        subtotal += item.product.product_price * item.quantity

    # Atualiza o valor de subtotal do carrinho
    cart.subtotal = subtotal

    # Calcula o novo valor de fee com base na quantidade de itens restantes no carrinho
    fee = 10 * CartItems.objects.filter(cart=cart).aggregate(Count('quantity'))['quantity__count']
    # Atualiza o valor de fee do carrinho
    cart.fee = fee

    # Calcula o novo valor de total_price com base no subtotal e fee atualizados
    total_price = subtotal + fee
    # Atualiza o valor de total_price do carrinho
    cart.total_price = total_price
    #Update CartItem price
    price_of_product = Product.objects.get(product_id=instance.product.product_id)
    instance.price = float(price_of_product.product_price) * instance.quantity
    # Salva as alterações no carrinho
    cart.save()


'''
#FEE SUBTOTAL
@receiver(post_save, sender=CartItems)
def update_cart_fee_and_subtotal(sender, instance, **kwargs):
    # Get the Cart object associated with the CartItems object
    cart = instance.cart
    # Calculate the new fee based on the number of CartItems and their quantities in the Cart
    fee = 10 * cart.cartitems_set.aggregate(Sum('quantity'))['quantity__sum']
    # Calculate the total value of all CartItems in the Cart
    subtotal = 0
    for item in cart.cartitems_set.all():
        subtotal += item.product.product_price * item.quantity
    # Update the fee and subtotal fields of the Cart object
    cart.fee = fee
    cart.subtotal = subtotal
    # Calculate the total price of the Cart
    total_price = subtotal + fee
    # Update the total_price field of the Cart object
    cart.total_price = total_price
    # Save the changes to the Cart object
    cart.save()

'''
'''
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
'''