from django.urls import path
from clothingsite import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),   
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('activate/<uid64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('contact/', views.contact, name='contact'),
    path('men_topwear/', views.men_topwear, name='men_topwear'),
    path('men_tshirt/', views.men_tshirt, name='men_tshirt'),
    path('men_casualshirt/', views.men_casualshirt, name='men_casualshirt'),
    path('men_formalshirt/', views.men_formalshirt, name='men_formalshirt'),
    path('men_sweatshirt/', views.men_sweatshirt, name='men_sweetshirt'),
    path('men_sweater/', views.men_sweater, name='men_sweater'),
    path('men_jacket/', views.men_jacket, name='men_jacket'),
    path('men_blazer/', views.men_blazer, name='men_blazer'),
    path('men_suit/', views.men_suit, name='men_suit'),
    path('boys_clothing/', views.boys_clothing, name='boys_clothing'),
    path('boys_kurta/', views.boys_kurta, name='boys_kurta'),
    path('boys_indowestern/', views.boys_indowestern, name='boys_indowestern'),
    path('boys_sherwani/', views.boys_sherwani, name='boys_sherwani'),
    path('boys_dhotikurta/', views.boys_dhotikurta, name='boys_dhotikurta'),
    path('boys_jacket/', views.boys_jacket, name='boys_jacket'),
    path('girls_clothing/', views.girls_clothing, name='girls_clothing'),
    path('girls_lehenga/', views.girls_lehenga, name='girls_lehenga'),
    path('girls_salwar/', views.girls_salwar, name='girls_salwar'),
    path('girls_gowns/', views.girls_gowns, name='girls_gowns'),
    path('girls_sarees/', views.girls_sarees, name='girls_sarees'),
    path('girls_frocks/', views.girls_frocks, name='girls_frocks'),
    path('girls_dresses/', views.girls_dresses, name='girls_dresses'),
    path('men_bottomwear/', views.men_bottomwear, name='men_bottomwear'),
    path('men_jeans/', views.men_jeans, name='men_jeans'),
    path('men_casualtrouser/', views.men_casualtrouser, name='men_casualtrouser'),
    path('men_formaltrouser/', views.men_formaltrouser, name='men_formaltrouser'),
    path('men_shorts/', views.men_shorts, name='men_shorts'),
    path('men_trackpant/', views.men_trackpant, name='men_trackpant'),
    path('men_footwear/', views.men_footwear, name='men_footwear'),
    path('men_casualshoes/', views.men_casualshoes, name='men_casualshoes'),
    path('men_sportshoes/', views.men_sportshoes, name='men_sportshoes'),
    path('men_formalshoes/', views.men_formalshoes, name='men_formalshoes'),
    path('men_sneakers/', views.men_sneakers, name='men_sneakers'),
    path('men_sandals/', views.men_sandals, name='men_sandals'),
    path('men_flipflop/', views.men_flipflop, name='men_flipflop'),
    path('men_socks/', views.men_socks, name='men_socks'),
    path('fusion_wear/', views.fusion_wear, name='fusion_wear'),
    path('women_kurtas/', views.women_kurtas, name='women_suit'),
    path('women_kurtis/', views.women_kurtis, name='women_kurtis'),
    path('women_sarees/', views.women_sarees, name='women_sarees'),
    path('women_ethnicwear/', views.women_ethnicwear, name='women_ethnicwear'),
    path('women_salwar/', views.women_salwar, name='women_salwar'),
    path('women_plazzos/', views.women_plazzos, name='women_plazzos'),
    path('women_dupatta/', views.women_dupatta, name='women_dupatta'),
    path('women_jacket/', views.women_jacket, name='women_jacket'),
    path('western_wear/', views.western_wear, name='western_wear'),
    path('women_dresses/', views.women_dresses, name='women_dresses'),
    path('women_tops/', views.women_tops, name='women_tops'),
    path('women_tshirt/', views.women_tshirt, name='women_tshirt'),
    path('women_jeans/', views.women_jeans, name='women_jeans'),
    path('women_trouser/', views.women_trouser, name='women_trouser'),
    path('women_skirt/', views.women_skirt, name='women_skirt'),
    path('women_coat/', views.women_coat, name='women_coat'),
    path('women_blazer/', views.women_blazer, name='women_blazer'),
    path('women_sweater/', views.women_sweater, name='women_sweater'),
    path('women_footwear/', views.women_footwear, name='women_footwear'),
    path('women_flat/', views.women_flat, name='women_flat'),
    path('women_casualshoes/', views.women_casualshoes, name='women_casualshoes'),
    path('women_heels/', views.women_heels, name='women_heels'),
    path('women_boots/', views.women_boots, name='women_boots'),
    path('women_sportshoes/', views.women_sportshoes, name='women_sportshoes'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('products/<int:myid>/', views.productView, name='productView'),
    path('profile/', views.profile, name='profile'),
    path('remove_order/<str:payment_id>/', views.remove_order, name='remove_order'),

    #Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='clothingsite/password_reset.html'), name='reset_password'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='clothingsite/password_reset_sent.html'), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='clothingsite/password_reset_form.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='clothingsite/password_reset_done.html'), name='password_reset_complete'),
    #End Password Reset
    path('faqs/', views.faqs, name='faqs'),
    path('privacy_policy/', views.privacypolicy, name='privacy_policy'),
]
