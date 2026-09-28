from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Market(models.Model):
    image0=models.ImageField(upload_to='image',blank=True)
    name=models.CharField(max_length=30)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    email=models.EmailField()
    number=models.CharField(max_length=11)
    
    def __str__(self):
        return self.name

class Mahsol(models.Model):
    image0=models.ImageField(upload_to='image',blank=True)
    image1=models.ImageField(upload_to='image',blank=True)
    image2=models.ImageField(upload_to='image',blank=True)
    image3=models.ImageField(upload_to='image',blank=True)
    image4=models.ImageField(upload_to='image',blank=True)
    image5=models.ImageField(upload_to='image',blank=True)
    image6=models.ImageField(upload_to='image',blank=True)
    image7=models.ImageField(upload_to='image',blank=True)
    image8=models.ImageField(upload_to='image',blank=True)
    image9=models.ImageField(upload_to='image',blank=True)
    image10=models.ImageField(upload_to='image',blank=True)
    image11=models.ImageField(upload_to='image',blank=True)
    image12=models.ImageField(upload_to='image',blank=True)
    image13=models.ImageField(upload_to='image',blank=True)
    image14=models.ImageField(upload_to='image',blank=True)   
    image15=models.ImageField(upload_to='image',blank=True)
    image16=models.ImageField(upload_to='image',blank=True)
    image17=models.ImageField(upload_to='image',blank=True)
    image18=models.ImageField(upload_to='image',blank=True)
    image19=models.ImageField(upload_to='image',blank=True)
    image20=models.ImageField(upload_to='image',blank=True)                              
    name=models.CharField(max_length=30)
    moshakhasat=models.TextField()
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    deccriptions=models.TextField()
    market=models.ForeignKey(Market,on_delete=models.CASCADE)
    
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.name
                                                                                                                             

class Rate(models.Model):
    mahsol = models.ForeignKey(Mahsol, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    staur = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'mahsol')

    def __str__(self):
        return str(self.staur)


class Like(models.Model):
    mahsol=models.ForeignKey(Mahsol,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together=('mahsol','user')


class Camment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    mahsol=models.ForeignKey(Mahsol,on_delete=models.CASCADE,related_name='camments')
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        User_display=self.user.email if self.user else"Anonymous"
        return f"{User_display} - {self.text}"
        
class Sabadkharid(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return f"سبد خرید {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Sabadkharid,on_delete=models.CASCADE,related_name='items',verbose_name="سبد خرید")
    product = models.ForeignKey('Mahsol',on_delete=models.CASCADE,verbose_name="محصول")
    quantity = models.PositiveIntegerField(default=1,verbose_name="تعداد")

    def __str__(self):
        return f"{self.quantity} عدد از {self.product.name}"                