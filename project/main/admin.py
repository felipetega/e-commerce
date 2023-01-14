from django.contrib import admin
from .models import Cart, Product, CartItems, Address, Payment

admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(CartItems)
'''
from .models import Cliente, Produto, Venda, Carrinho
from . forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
  model = Cliente
  add_form = CustomUserCreationForm

  fieldsets = (
    *UserAdmin.fieldsets,
      ('Informações adicionais', {
          "fields": (
            'cliente_telefone',  
          ),
      }),
  )
  
  
  
  

admin.site.register(Cliente, CustomUserAdmin)
admin.site.register(Carrinho)
admin.site.register(Produto)
admin.site.register(Venda)
'''