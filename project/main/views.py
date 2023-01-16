'''
# Create your views here.
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItems, Address, CreditCard, EXPIRY_MONTH, EXPIRY_YEAR

def index(request):
  return redirect('/login')


def register(request):
  if request.method == "GET":
    return render(request, "main/register.html", {})
  else:
    cliente_nome = request.POST.get('cliente_nome')
    cliente_email = request.POST.get('cliente_email')
    cliente_senha = request.POST.get('cliente_senha')

    user = User.objects.filter(username=cliente_nome).first()

    if user:
      return HttpResponse('Já existe um usuário com esse username')

    user = User.objects.create_user(
        username=cliente_nome, email=cliente_email, password=cliente_senha)
    user.save()

    return HttpResponse("Usuário cadastrado com sucesso")


def login(request):
  if request.method == "GET":
    return render(request, "main/login.html", {})
  else:
    cliente_nome = request.POST.get('cliente_nome')
    cliente_senha = request.POST.get('cliente_senha')

    user = authenticate(username=cliente_nome, password=cliente_senha)

    if user:
      login_django(request, user)
      return redirect('/home')
    else:
      return HttpResponse('Usuário e/ou senha inválido(s)')



@login_required(login_url="/auth/login/")
def home(request):
  if request.method == "GET": 
    #CURRENT USER
    current_user = request.user

    #PRODUTOS
    produtos=Product.objects.all()

    #CART
    cart=Cart.objects.all()
    cart = cart.filter(user=current_user)

    #CART ITEMS
    cartItems = CartItems.objects.all()
    cartItems = cartItems.filter(user=current_user)

    #FILTROS

    filtros={"Selecione um filtro":0,"Menor Preço":1,"Maior Score":2,"Ordem alfabética":3}
    filtro_selecionado= request.GET.get('filtro_selecionado')
    if filtro_selecionado=="1":
      produtos=produtos.order_by('product_price')
    elif filtro_selecionado=="2":
      produtos=produtos.order_by('-product_score')
    elif filtro_selecionado=="3":
      produtos=produtos.order_by('product_name')


    filtro_nome= request.GET.get('filtro_nome')
    if filtro_nome:
      produtos = produtos.filter(product_name__icontains=filtro_nome)

    formas_pagamento = {"Selecione opção de pagamento":0,"Cartão de Crédito":2,"Pix":3,"Boleto":4}


      
    context = {'produtos': produtos,
                'cart':cart,
                'cartItems':cartItems,
                'filtros':filtros,
                'formas_pagamento':formas_pagamento,}

    return render(request, "main/home.html", context)
  elif request.method == "POST":
    return redirect('/checkout')

def checkout(request):
  if request.method == "GET":

    #CURRENT USER
    current_user = request.user

    #CART
    cart=Cart.objects.all()
    cart = cart.filter(user=current_user)

    #CART ITEMS
    cartItems = CartItems.objects.all()
    cartItems = cartItems.filter(user=current_user)

    address = Address.objects.all().filter(user=current_user).first()

    expiry_year = {0:"Selecione o ano de expiração",'2023':'2023','2024':'2024','2025':'2025','2026':'2026','2027':'2027','2028':'2028'}

    expiry_month = {0:"Selecione o mês de expiração",'1':'Janeiro','2':'Fevereiro','3':'Março','4':'Abril','5':'Maio','6':'Junho','7':'Julho','8':'Agosto','9':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'}

    context = {'cart':cart,
              'cartItems':cartItems,
              'expiry_year':expiry_year,
              'expiry_month':expiry_month}

    return render(request, "main/checkout.html", context)
  elif request.method == "POST":
    # CURRENT USER
    current_user = request.user

    # CART
    cart = Cart.objects.all().filter(user=current_user).first()

    # Atualiza o campo ordered do carrinho
    cart.ordered = True

    # Salva as alterações no carrinho
    cart.save()

    #ADDRESS
    address = Address.objects.create(user=current_user, city=request.POST['city'], street=request.POST['street'], number=request.POST['number'], cep=request.POST['cep'])

    address.save()

    #PAYMENT
    payment = CreditCard.objects.create(user=current_user, card_number=request.POST['card_number'], cvv=request.POST['cvv'], expiry_year=request.POST['expiry_year'], expiry_month=request.POST['expiry_month'], cardholder_name=request.POST['cardholder_name'], document_id=request.POST['document_id'], )

    payment.save()

    return redirect('/home')

def profile(request):
  if request.method == "GET":

    #CURRENT USER
    current_user = request.user

    #ADDRESS
    addresses = Address.objects.all()
    addresses = addresses.filter(user=current_user)

    #CARDS
    cards = CreditCard.objects.all()
    cards=cards.filter(user=current_user)


    #CART
    cart=Cart.objects.all()
    cart = cart.filter(user=current_user, ordered=True)

    cartItems = CartItems.objects.all()
    cartItems = cartItems.filter(user=current_user)

    context = {'cart':cart,
              'cartItems':cartItems,
              'addresses':addresses,
              'cards':cards
              }

    return render(request, "main/profile.html", context)

def create_cartitem(request, pk):
    # Recupera o produto selecionado pelo usuário
    product = Product.objects.get(product_id=pk)

    # Recupera o carrinho do usuário autenticado atual
    user = request.user
    cart = Cart.objects.get(user=user)

    # Verifica se há um item no carrinho com o mesmo produto e usuário
    item = CartItems.objects.filter(product=product, user=user).first()
    if item:
        # Atualiza a quantidade do item existente
        item.quantity += 1
        item.save()
    else:
        # Cria um novo item no carrinho
        cart_item = CartItems(cart=cart, user=user, product=product, quantity=1)
        cart_item.save()

    return redirect('/home')



def addition(request, id):
    product = Product.objects.get(product_id=id)
    cart_item = CartItems.objects.get(user=request.user, product=product.product_id)
    cart_item.quantity = cart_item.quantity + 1
    cart_item.save()
    return redirect('/checkout')

def subtract(request, id):
    product = Product.objects.get(product_id=id)
    cart_item = CartItems.objects.get(user=request.user, product=product.product_id)
    cart_item.quantity = cart_item.quantity - 1
    if cart_item.quantity == 0:
        cart_item.save()
        cart_item.delete()
    else:
        cart_item.save()
    return redirect('/checkout')

def remove(request, id):
    product = Product.objects.get(product_id=id)
    cart_item = CartItems.objects.get(user=request.user, product=product.product_id)
    cart = Cart.objects.all()[0]
    cart.total_price -= round(cart_item.price,2)
    cart.total_price = round(cart.total_price,2)
    cart.save()
    cart_item.delete()
    return redirect('/checkout')

