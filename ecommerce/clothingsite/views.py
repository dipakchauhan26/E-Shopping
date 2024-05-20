from django.shortcuts import render, redirect,HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from clothingsite.models import Contact,Product,Orders,OrderUpdate, Size
import json
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
# Create your views here.


def home(request):
    return render(request, 'clothingsite/index.html')


def register(request):
    if request.method=="POST":
        email = request.POST['Email']
        password = request.POST['Password']
        confirm_password = request.POST['ConfirmPassword']

        if password != confirm_password:
           messages.warning(request,"Password is not matching!")
           return render(request,'clothingsite/register.html')

        try:
            if User.objects.get(username=email):
                messages.info(request,"Email already exist!")
                return  render(request,'clothingsite/register.html')

        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.is_active = False
        user.save()

        email_subject = "Activate Your Account"
        message = render_to_string('clothingsite/activate.html',{
            'user' : user,
            'domain' : '127.0.0.1:8000',
            'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
            'token' : generate_token.make_token(user)
        })

        email_message = EmailMessage(
                                    email_subject,
                                    message,
                                    settings.EMAIL_HOST_USER,
                                    [email],
                                    )
        email_message.send()
        messages.success(request,"Activate your account by clicking the link in your gmail")
        return redirect('/login/')
    return render(request, 'clothingsite/register.html')
   
class ActivateAccountView(View):
    def get(self, request, uid64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uid64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user,token):
            user.is_active = True
            user.save()
            messages.info(request,"Account Activated Successfully Now You Can Login With Your Email And Password")
            return redirect('/login/')
        return render(request,'clothingsite/activatefail.html')



def user_login(request):
    if request.method == "POST":
        username = request.POST['Email']
        userpassword = request.POST['Password']
        myuser = authenticate(username=username, password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login/')
        
    return render(request, 'clothingsite/login.html')



def user_logout(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect('/login/')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        pnumber = request.POST.get("pnumber")
        myquery = Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"We Will Get Back To You Soon...")
        return render(request, 'clothingsite/contact.html')
    return render(request, 'clothingsite/contact.html')



def men_topwear(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_topwear_products = Product.objects.filter(subcategory = 'men-topwear')

    if ordering:
        men_topwear_products = men_topwear_products.order_by(ordering)

    if price:
        men_topwear_products = men_topwear_products.filter(price__lt = price)

    return render(request,'clothingsite/men_topwear.html', {'men_topwear_products' : men_topwear_products})


def men_tshirt(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_tshirt_products = Product.objects.filter(subcategory = 'men-tshirt')

    if ordering:
        men_tshirt_products = men_tshirt_products.order_by(ordering)

    if price:
        men_tshirt_products = men_tshirt_products.filter(price__lt = price)

    return render(request,'clothingsite/men_tshirt.html', {'men_tshirt_products' : men_tshirt_products})

def men_casualshirt(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_casualshirt_products = Product.objects.filter(subcategory = 'men-casualshirt')

    if ordering:
        men_casualshirt_products = men_casualshirt_products.order_by(ordering)

    if price:
        men_casualshirt_products = men_casualshirt_products.filter(price__lt = price)

    return render(request,'clothingsite/men_casualshirt.html', {'men_casualshirt_products' : men_casualshirt_products})

def men_formalshirt(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_formalshirt_products = Product.objects.filter(subcategory = 'men-formalshirt')

    if ordering:
        men_formalshirt_products = men_formalshirt_products.order_by(ordering)

    if price:
        men_formalshirt_products = men_formalshirt_products.filter(price__lt = price)
    
    return render(request,'clothingsite/men_formalshirt.html', {'men_formalshirt_products' : men_formalshirt_products})

def men_sweatshirt(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_sweatshirt_products = Product.objects.filter(subcategory = 'men-sweatshirt')

    if ordering:
        men_sweatshirt_products = men_sweatshirt_products.order_by(ordering)

    if price:
        men_sweatshirt_products = men_sweatshirt_products.filter(price__lt = price)

    return render(request,'clothingsite/men_sweatshirt.html', {'men_sweatshirt_products' : men_sweatshirt_products})

def men_sweater(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_sweater_products = Product.objects.filter(subcategory = 'men-sweater')

    if ordering:
        men_sweater_products = men_sweater_products.order_by(ordering)

    if price:
        men_sweater_products = men_sweater_products.filter(price__lt = price)

    return render(request,'clothingsite/men_sweater.html', {'men_sweater_products' : men_sweater_products})

def men_jacket(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_jacket_products = Product.objects.filter(subcategory = 'men-jacket')

    if ordering:
        men_jacket_products = men_jacket_products.order_by(ordering)

    if price:
        men_jacket_products = men_jacket_products.filter(price__lt = price)

    return render(request,'clothingsite/men_jacket.html', {'men_jacket_products' : men_jacket_products})

def men_blazer(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_blazer_products = Product.objects.filter(subcategory = 'men-blazer')

    if ordering:
        men_blazer_products = men_blazer_products.order_by(ordering)

    if price:
        men_blazer_products = men_blazer_products.filter(price__lt = price)

    return render(request,'clothingsite/men_blazer.html', {'men_blazer_products' : men_blazer_products})

def men_suit(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_suit_products = Product.objects.filter(subcategory = 'men-suit')

    if ordering:
        men_suit_products = men_suit_products.order_by(ordering)

    if price:
        men_suit_products = men_suit_products.filter(price__lt = price)

    return render(request,'clothingsite/men_suit.html', {'men_suit_products' : men_suit_products})

def boys_clothing(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    boys_clothing_products = Product.objects.filter(subcategory = 'boys_clothing')

    if ordering:
        boys_clothing_products = boys_clothing_products.order_by(ordering)

    if price:
        boys_clothing_products = boys_clothing_products.filter(price__lt = price)

    return render(request,'clothingsite/boys_clothing.html', {'boys_clothing_products' : boys_clothing_products})


def boys_kurta(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    boys_kurta_products = Product.objects.filter(subcategory = 'boys-kurta')

    if ordering:
        boys_kurta_products = boys_kurta_products.order_by(ordering)

    if price:
        boys_kurta_products = boys_kurta_products.filter(price__lt = price)

    return render(request,'clothingsite/boys_kurta.html', {'boys_kurta_products' : boys_kurta_products})

def boys_indowestern(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    boys_indowestern_products = Product.objects.filter(subcategory = 'boys-indowestern')

    if ordering:
        boys_indowestern_products = boys_indowestern_products.order_by(ordering)

    if price:
        boys_indowestern_products = boys_indowestern_products.filter(price__lt = price)

    return render(request,'clothingsite/boys_indowestern.html', {'boys_indowestern_products' : boys_indowestern_products})

def boys_sherwani(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    boys_sherwani_products = Product.objects.filter(subcategory = 'boys-sherwani')

    if ordering:
        boys_sherwani_products = boys_sherwani_products.order_by(ordering)

    if price:
        boys_sherwani_products = boys_sherwani_products.filter(price__lt = price)

    return render(request,'clothingsite/boys_sherwani.html', {'boys_sherwani_products' : boys_sherwani_products})

def boys_dhotikurta(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    boys_dhotikurta_products = Product.objects.filter(subcategory = 'boys-dhotikurta')

    if ordering:
        boys_dhotikurta_products = boys_dhotikurta_products.order_by(ordering)

    if price:
        boys_dhotikurta_products = boys_dhotikurta_products.filter(price__lt = price)

    return render(request,'clothingsite/boys_dhotikurta.html', {'boys_dhotikurta_products' : boys_dhotikurta_products})

def boys_jacket(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    boys_jacket_products = Product.objects.filter(subcategory = 'boys-jacket')

    if ordering:
        boys_jacket_products = boys_jacket_products.order_by(ordering)

    if price:
        boys_jacket_products = boys_jacket_products.filter(price__lt = price)

    return render(request,'clothingsite/boys_jacket.html', {'boys_jacket_products' : boys_jacket_products})

def girls_clothing(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    girls_clothing_products = Product.objects.filter(subcategory = 'girls_clothing')

    if ordering:
        girls_clothing_products = girls_clothing_products.order_by(ordering)

    if price:
        girls_clothing_products = girls_clothing_products.filter(price__lt = price)

    return render(request,'clothingsite/girls_clothing.html', {'girls_clothing_products' : girls_clothing_products})

def girls_lehenga(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    girls_lehenga_products = Product.objects.filter(subcategory = 'girls-lehenga')

    if ordering:
        girls_lehenga_products = girls_lehenga_products.order_by(ordering)

    if price:
        girls_lehenga_products = girls_lehenga_products.filter(price__lt = price)

    return render(request,'clothingsite/girls_lehenga.html', {'girls_lehenga_products' : girls_lehenga_products})

def girls_salwar(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    girls_salwar_products = Product.objects.filter(subcategory = 'girls-salwar')

    if ordering:
        girls_salwar_products = girls_salwar_products.order_by(ordering)

    if price:
        girls_salwar_products = girls_salwar_products.filter(price__lt = price)

    return render(request,'clothingsite/girls_salwar.html', {'girls_salwar_products' : girls_salwar_products})

def girls_gowns(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    girls_gowns_products = Product.objects.filter(subcategory = 'girls-gowns')

    if ordering:
        girls_gowns_products = girls_gowns_products.order_by(ordering)

    if price:
        girls_gowns_products = girls_gowns_products.filter(price__lt = price)

    return render(request,'clothingsite/girls_gowns.html', {'girls_gowns_products' : girls_gowns_products})

def girls_sarees(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    girls_sarees_products = Product.objects.filter(subcategory = 'girls-sarees')

    if ordering:
        girls_sarees_products = girls_sarees_products.order_by(ordering)

    if price:
        girls_sarees_products = girls_sarees_products.filter(price__lt = price)

    return render(request,'clothingsite/girls_sarees.html', {'girls_sarees_products' : girls_sarees_products})

def girls_frocks(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    girls_frocks_products = Product.objects.filter(subcategory = 'girls-frocks')

    if ordering:
        girls_frocks_products = girls_frocks_products.order_by(ordering)

    if price:
        girls_frocks_products = girls_frocks_products.filter(price__lt = price)

    return render(request,'clothingsite/girls_frocks.html', {'girls_frocks_products' : girls_frocks_products})

def girls_dresses(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    girls_dresses_products = Product.objects.filter(subcategory = 'girls-dresses')

    if ordering:
        girls_dresses_products = girls_dresses_products.order_by(ordering)

    if price:
        girls_dresses_products = girls_dresses_products.filter(price__lt = price)

    return render(request,'clothingsite/girls_dresses.html', {'girls_dresses_products' : girls_dresses_products})

def men_bottomwear(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_bottomwear_products = Product.objects.filter(subcategory = 'men-bottomwear')

    if ordering:
        men_bottomwear_products = men_bottomwear_products.order_by(ordering)

    if price:
        men_bottomwear_products = men_bottomwear_products.filter(price__lt = price)

    return render(request,'clothingsite/men_bottomwear.html', {'men_bottomwear_products' : men_bottomwear_products})


def men_jeans(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_jeans_products = Product.objects.filter(subcategory = 'men-jeans')

    if ordering:
        men_jeans_products = men_jeans_products.order_by(ordering)

    if price:
        men_jeans_products = men_jeans_products.filter(price__lt = price)

    return render(request,'clothingsite/men_jeans.html', {'men_jeans_products' : men_jeans_products})

def men_casualtrouser(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_casualtrouser_products = Product.objects.filter(subcategory = 'men-casualtrouser')

    if ordering:
        men_casualshirt_products = men_casualshirt_products.order_by(ordering)

    if price:
        men_casualshirt_products = men_casualshirt_products.filter(price__lt = price)

    return render(request,'clothingsite/men_casualtrouser.html', {'men_casualtrouser_products' : men_casualtrouser_products})

def men_formaltrouser(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_formaltrouser_products = Product.objects.filter(subcategory = 'men-formaltrouser')

    if ordering:
        men_formaltrouser_products = men_formaltrouser_products.order_by(ordering)

    if price:
        men_formaltrouser_products = men_formaltrouser_products.filter(price__lt = price)

    return render(request,'clothingsite/men_formaltrouser.html', {'men_formaltrouser_products' : men_formaltrouser_products})

def men_shorts(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_shorts_products = Product.objects.filter(subcategory = 'men-shorts')

    if ordering:
        men_shorts_products = men_shorts_products.order_by(ordering)

    if price:
        men_shorts_products = men_shorts_products.filter(price__lt = price)

    return render(request,'clothingsite/men_shorts.html', {'men_shorts_products' : men_shorts_products})

def men_trackpant(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_trackpant_products = Product.objects.filter(subcategory = 'men-trackpant')

    if ordering:
        men_trackpant_products = men_trackpant_products.order_by(ordering)

    if price:
        men_trackpant_products = men_trackpant_products.filter(price__lt = price)

    return render(request,'clothingsite/men_trackpant.html', {'men_trackpant_products' : men_trackpant_products})

def men_footwear(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_footwear_products = Product.objects.filter(subcategory = 'men-footwear')

    if ordering:
        men_footwear_products = men_footwear_products.order_by(ordering)

    if price:
        men_footwear_products = men_footwear_products.filter(price__lt = price)

    return render(request,'clothingsite/men_footwear.html', {'men_footwear_products' : men_footwear_products})

def men_casualshoes(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_casualshoes_products = Product.objects.filter(subcategory = 'men-casual shoes')

    if ordering:
        men_casualshoes_products = men_casualshoes_products.order_by(ordering)

    if price:
        men_casualshoes_products = men_casualshoes_products.filter(price__lt = price)

    return render(request,'clothingsite/men_casualshoes.html', {'men_casualshoes_products' : men_casualshoes_products})

def men_sportshoes(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_sportshoes_products = Product.objects.filter(subcategory = 'men-sport shoes')

    if ordering:
        men_sportshoes_products = men_sportshoes_products.order_by(ordering)

    if price:
        men_sportshoes_products = men_sportshoes_products.filter(price__lt = price)

    return render(request,'clothingsite/men_sportshoes.html', {'men_sportshoes_products' : men_sportshoes_products})

def men_formalshoes(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_formalshoes_products = Product.objects.filter(subcategory = 'men-formal shoes')

    if ordering:
        men_formalshoes_products = men_formalshoes_products.order_by(ordering)

    if price:
        men_formalshoes_products = men_formalshoes_products.filter(price__lt = price)

    return render(request,'clothingsite/men_formalshoes.html', {'men_formalshoes_products' : men_formalshoes_products})

def men_sneakers(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_sneakers_products = Product.objects.filter(subcategory = 'men-sneakers')

    if ordering:
        men_sneakers_products = men_sneakers_products.order_by(ordering)

    if price:
        men_sneakers_products = men_sneakers_products.filter(price__lt = price)

    return render(request,'clothingsite/men_sneakers.html', {'men_sneakers_products' : men_sneakers_products})

def men_sandals(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_sandals_products = Product.objects.filter(subcategory = 'men-sandals')

    if ordering:
        men_sandals_products = men_sandals_products.order_by(ordering)

    if price:
        men_sandals_products = men_sandals_products.filter(price__lt = price)

    return render(request,'clothingsite/men_sandals.html', {'men_sandals_products' : men_sandals_products})

def men_flipflop(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_flipflop_products = Product.objects.filter(subcategory = 'men-flipflop')

    if ordering:
        men_flipflop_products = men_flipflop_products.order_by(ordering)

    if price:
        men_flipflop_products = men_flipflop_products.filter(price__lt = price)

    return render(request,'clothingsite/men_flipflop.html', {'men_flipflop_products' : men_flipflop_products})

def men_socks(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    men_socks_products = Product.objects.filter(subcategory = 'men-socks')

    if ordering:
        men_socks_products = men_socks_products.order_by(ordering)

    if price:
        men_socks_products = men_socks_products.filter(price__lt = price)

    return render(request,'clothingsite/men_socks.html', {'men_socks_products' : men_socks_products})

def fusion_wear(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    fusion_wear_products = Product.objects.filter(subcategory = 'fusion-wear')

    if ordering:
        fusion_wear_products = fusion_wear_products.order_by(ordering)

    if price:
        fusion_wear_products = fusion_wear_products.filter(price__lt = price)

    return render(request,'clothingsite/fusion_wear.html', {'fusion_wear_products' : fusion_wear_products})

def women_kurtas(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_kurtas_products = Product.objects.filter(subcategory = 'women-suit')

    if ordering:
        women_kurtas_products = women_kurtas_products.order_by(ordering)

    if price:
        women_kurtas_products = women_kurtas_products.filter(price__lt = price)

    return render(request,'clothingsite/women_suit.html', {'women_suit_products' : women_kurtas_products})

def women_kurtis(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_kurtis_products = Product.objects.filter(subcategory = 'women-kurtis')

    if ordering:
        women_kurtis_products = women_kurtis_products.order_by(ordering)

    if price:
        women_kurtis_products = women_kurtis_products.filter(price__lt = price)

    return render(request,'clothingsite/women_kurtis.html', {'women_kurtis_products' : women_kurtis_products})

def women_sarees(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_sarees_products = Product.objects.filter(subcategory = 'women-sarees')

    if ordering:
        women_sarees_products = women_sarees_products.order_by(ordering)

    if price:
        women_sarees_products = women_sarees_products.filter(price__lt = price)

    return render(request,'clothingsite/women_sarees.html', {'women_sarees_products' : women_sarees_products})

def women_ethnicwear(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_ethnicwear_products = Product.objects.filter(subcategory = 'women-ethnicwear')

    if ordering:
        women_ethnicwear_products = women_ethnicwear_products.order_by(ordering)

    if price:
        women_ethnicwear_products = women_ethnicwear_products.filter(price__lt = price)

    return render(request,'clothingsite/women_ethnicwear.html', {'women_ethnicwear_products' : women_ethnicwear_products})

def women_salwar(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_salwar_products = Product.objects.filter(subcategory = 'women-salwar')

    if ordering:
        women_salwar_products = women_salwar_products.order_by(ordering)

    if price:
        women_salwar_products = women_salwar_products.filter(price__lt = price)

    return render(request,'clothingsite/women_salwar.html', {'women_salwar_products' : women_salwar_products})

def women_plazzos(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_plazzos_products = Product.objects.filter(subcategory = 'women-plazzos')

    if ordering:
        women_plazzos_products = women_plazzos_products.order_by(ordering)

    if price:
        women_plazzos_products = women_plazzos_products.filter(price__lt = price)

    return render(request,'clothingsite/women_plazzos.html', {'women_plazzos_products' : women_plazzos_products})

def women_dupatta(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_dupatta_products = Product.objects.filter(subcategory = 'women-dupatta')

    if ordering:
        women_dupatta_products = women_dupatta_products.order_by(ordering)

    if price:
        women_dupatta_products = women_dupatta_products.filter(price__lt = price)

    return render(request,'clothingsite/women_dupatta.html', {'women_dupatta_products' : women_dupatta_products})

def women_jacket(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_jacket_products = Product.objects.filter(subcategory = 'women-jacket')

    if ordering:
        women_jacket_products = women_jacket_products.order_by(ordering)

    if price:
        women_jacket_products = women_jacket_products.filter(price__lt = price)

    return render(request,'clothingsite/women_jacket.html', {'women_jacket_products' : women_jacket_products})

def western_wear(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    western_wear_products = Product.objects.filter(subcategory = 'western-wear')

    if ordering:
        western_wear_products = western_wear_products.order_by(ordering)

    if price:
        western_wear_products = western_wear_products.filter(price__lt = price)

    return render(request,'clothingsite/western_wear.html', {'western_wear_products' : western_wear_products})

def women_dresses(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_dresses_products = Product.objects.filter(subcategory = 'women-dresses')

    if ordering:
        women_dresses_products = women_dresses_products.order_by(ordering)

    if price:
        women_dresses_products = women_dresses_products.filter(price__lt = price)

    return render(request,'clothingsite/women_dresses.html', {'women_dresses_products' : women_dresses_products})

def women_tops(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_tops_products = Product.objects.filter(subcategory = 'women-tops')

    if ordering:
        women_tops_products = women_tops_products.order_by(ordering)

    if price:
        women_tops_products = women_tops_products.filter(price__lt = price)

    return render(request,'clothingsite/women_tops.html', {'women_tops_products' : women_tops_products})

def women_tshirt(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_tshirt_products = Product.objects.filter(subcategory = 'women-tshirt')

    if ordering:
        women_tshirt_products = women_tshirt_products.order_by(ordering)

    if price:
        women_tshirt_products = women_tshirt_products.filter(price__lt = price)

    return render(request,'clothingsite/women_tshirt.html', {'women_tshirt_products' : women_tshirt_products})

def women_jeans(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_jeans_products = Product.objects.filter(subcategory = 'women-jeans')

    if ordering:
        women_jeans_products = women_jeans_products.order_by(ordering)

    if price:
        women_jeans_products = women_jeans_products.filter(price__lt = price)

    return render(request,'clothingsite/women_jeans.html', {'women_jeans_products' : women_jeans_products})

def women_trouser(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_trouser_products = Product.objects.filter(subcategory = 'women-trouser')

    if ordering:
        women_trouser_products = women_trouser_products.order_by(ordering)

    if price:
        women_trouser_products = women_trouser_products.filter(price__lt = price)

    return render(request,'clothingsite/women_trouser.html', {'women_trouser_products' : women_trouser_products})

def women_skirt(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_skirt_products = Product.objects.filter(subcategory = 'women-skirt')

    if ordering:
        women_skirt_products = women_skirt_products.order_by(ordering)

    if price:
        women_skirt_products = women_skirt_products.filter(price__lt = price)

    return render(request,'clothingsite/women_skirt.html', {'women_skirt_products' : women_skirt_products})

def women_coat(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_coat_products = Product.objects.filter(subcategory = 'women-coat')

    if ordering:
        women_coat_products = women_coat_products.order_by(ordering)

    if price:
        women_coat_products = women_coat_products.filter(price__lt = price)

    return render(request,'clothingsite/women_coat.html', {'women_coat_products' : women_coat_products})

def women_blazer(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_blazer_products = Product.objects.filter(subcategory = 'women-blazer')
    
    if ordering:
        women_blazer_products = women_blazer_products.order_by(ordering)

    if price:
        women_blazer_products = women_blazer_products.filter(price__lt = price)

    return render(request,'clothingsite/women_blazer.html', {'women_blazer_products' : women_blazer_products})

def women_sweater(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_sweater_products = Product.objects.filter(subcategory = 'women-sweater')

    if ordering:
        women_sweater_products = women_sweater_products.order_by(ordering)

    if price:
        women_sweater_products = women_sweater_products.filter(price__lt = price)

    return render(request,'clothingsite/women_sweater.html', {'women_sweater_products' : women_sweater_products})

def women_footwear(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_footwear_products = Product.objects.filter(subcategory = 'women-footwear')

    if ordering:
        women_footwear_products = women_footwear_products.order_by(ordering)

    if price:
        women_footwear_products = women_footwear_products.filter(price__lt = price)

    return render(request,'clothingsite/women_footwear.html', {'women_footwear_products' : women_footwear_products})

def women_flat(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_flat_products = Product.objects.filter(subcategory = 'women-flat')

    if ordering:
        women_flat_products = women_flat_products.order_by(ordering)

    if price:
        women_flat_products = women_flat_products.filter(price__lt = price)

    return render(request,'clothingsite/women_flat.html', {'women_flat_products' : women_flat_products})

def women_casualshoes(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_casualshoes_products = Product.objects.filter(subcategory = 'women-casualshoes')

    if ordering:
        women_casualshoes_products = women_casualshoes_products.order_by(ordering)

    if price:
        women_casualshoes_products = women_casualshoes_products.filter(price__lt = price)

    return render(request,'clothingsite/women_casualshoes.html', {'women_casualshoes_products' : women_casualshoes_products})

def women_heels(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_heels_products = Product.objects.filter(subcategory = 'women-heels')

    if ordering:
        women_heels_products = women_heels_products.order_by(ordering)

    if price:
        women_heels_products = women_heels_products.filter(price__lt = price)

    return render(request,'clothingsite/women_heels.html', {'women_heels_products' : women_heels_products})

def women_boots(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_boots_products = Product.objects.filter(subcategory = 'women-boots')

    if ordering:
        women_boots_products = women_boots_products.order_by(ordering)

    if price:
        women_boots_products = women_boots_products.filter(price__lt = price)

    return render(request,'clothingsite/women_boots.html', {'women_boots_products' : women_boots_products})

def women_sportshoes(request):
    ordering = request.GET.get('ordering', '')
    price = request.GET.get('price', '')
    women_sportshoes_products = Product.objects.filter(subcategory = 'women-sportshoes')

    if ordering:
       women_sportshoes_products = women_sportshoes_products.order_by(ordering)

    if price:
        women_sportshoes_products = women_sportshoes_products.filter(price__lt = price)

    return render(request,'clothingsite/women_sportshoes.html', {'women_sportshoes_products' : women_sportshoes_products})


def faqs(request):
    return render(request, 'clothingsite/faqs.html')

def privacypolicy(request):
    return render(request, 'clothingsite/privacy-policy.html')


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/login/')
    
    if request.method == "POST":
        items_json = request.POST.get('itemsJson')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        amount = int(request.POST.get('amt')) * 100
        client = razorpay.Client(auth =("rzp_test_z0jwFP9KaXp7wo", "belwb5rziYqumz9lnt1ZY9Bq"))
        payment = client.order.create({'amount' : amount, 'currency' : 'INR', 'payment_capture' : '1'})
        print(amount)

        Order = Orders(items_json=items_json, name=name, email=email, address=address, city=city, state=state, pincode=pincode, phone=phone, amount=amount, payment_id=payment['id'])
        Order.save()
        update = OrderUpdate(order_id=Order.payment_id,update_desc="The order has been placed",email=Order.email)
        update.save()
        return render(request,'clothingsite/checkout.html', {'payment' : payment, 'Order' : Order})
    
    return render(request,'clothingsite/checkout.html') 
    
@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        print(a)
        order_id = ""
        for key , val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Orders.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()

    return render(request, 'clothingsite/success.html')

def calculate_final_price(base_price, size_price_adjustment):
    if size_price_adjustment is None:
        return base_price   
    return base_price + size_price_adjustment



def productView(request , myid):
    p = Product.objects.get(id=myid)
    final_price = None
    if request.method == 'POST':
        selected_size_id = request.POST.get('size_id')
        selected_size = Size.objects.get(pk=selected_size_id)
        final_price = calculate_final_price(p.price, selected_size.price_adjustment)
    return render(request,'clothingsite/product_view.html', {'p' : p, 'final_price' : final_price}) 


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/login/')
    
    currentuser = None
    if request.user.is_staff:
        currentuser = "Staff User"
    else:
        currentuser = request.user.username
    
    items = Orders.objects.filter(email=currentuser)
    print(items)
    oid = ''
    for i in items:
        myid = i.payment_id
        oid = myid

    status = OrderUpdate.objects.filter(order_id=oid)#mapping the payment_id field in Orders table with the order_id field in Orders_Update table
    context = {"items":items, "status":status, 'currentuser':currentuser}
    return render(request, 'clothingsite/profile.html', context)

def remove_order(request, payment_id):
    order = get_object_or_404(Orders, payment_id=payment_id)
    order_update = get_object_or_404(OrderUpdate, order_id=payment_id)

    order.delete()
    order_update.delete()

    messages.success(request, "Order removed successfully.")
    return redirect('profile')