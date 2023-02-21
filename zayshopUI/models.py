from django.db import models
from django.utils.text import slugify
# Create your models here.


class Prodct(models.Model):
    title = models.CharField(max_length=50,null=False,blank=False)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=False,blank=False)
    brand = models.CharField(max_length=50,default='No Brand')
    description = models.TextField(max_length=500,null=True,blank=True)
    specification = models.TextField(max_length=500,null=True,blank=True)
    color = models.ManyToManyField('Color')
    size = models.ManyToManyField('Size')
    quantite = models.IntegerField()
    img_prdct = models.ImageField(upload_to='prdct_imges/',default='no-img.jpg')
    img_slide1 = models.ImageField(upload_to='img_slide/img1',default='no-img.jpg')
    img_slide2 = models.ImageField(upload_to='img_slide/img2',default='no-img.jpg')
    img_slide3 = models.ImageField(upload_to='img_slide/img3',default='no-img.jpg')
    img_slide4 = models.ImageField(upload_to='img_slide/img4',default='no-img.jpg')
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Prodct,self).save(*args, **kwargs)


    def __str__(self):
        return self.title



class Color(models.Model):
    clr = models.CharField(max_length=50)

    def __str__(self):
        return self.clr


class Size(models.Model):
    siz = models.CharField(max_length=50)

    def __str__(self):
        return self.siz



class ContactUsForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=50)

    class  Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.email
