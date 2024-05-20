from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    phonenumber = models.IntegerField()

    def __str__(self):
        return self.name
    
class Size(models.Model):
    title = models.CharField(max_length=100)
    price_adjustment = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 150)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    old_price = models.IntegerField(blank=True, null=True)
    size = models.ManyToManyField(Size)
    description = models.CharField(max_length = 1500)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_2 = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_3 = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_4 = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_5 = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_5 = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_6 = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_7 = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_8 = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_9 = models.ImageField(upload_to='clothingsite/images', blank=True)
    image_10 = models.ImageField(upload_to='clothingsite/images', blank=True)

    # class Meta:
    #     ordering = ['-price']
    
    def __str__(self):
        return f"{self.id} - {self.subcategory}"
    


    
class Orders(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    pincode = models.CharField(max_length=100) 
    phone = models.CharField(max_length=100, default="")
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    items_json =  models.CharField(max_length=5000, default="")
    def __str__(self):
       return self.email
    
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    update_desc = models.CharField(max_length=5000)
    delivered=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    
# class ProductAttribute(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     size = models.ForeignKey(Size, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.product.product_name