from django.db import models


# Create your models here.
class carousel(models.Model):
    heading=models.CharField(max_length=50,null=True)
    des=models.CharField(max_length=200,null=True)
    Img=models.ImageField(upload_to='img/carousel',null=True)
    submitted_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'carousel'

    def __str__(self):
        return self.heading

class services(models.Model):
    title=models.CharField(max_length=50,null=True)
    content=models.CharField(max_length=200,null=True)
    Img=models.ImageField(upload_to='img/services',null=True)
    submitted_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'services'

    def __str__(self):
        return self.title

class clients(models.Model):
    img=models.ImageField(upload_to='img/clients',null=True)
    link=models.CharField(max_length=500,null=True)
    submitted_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table:'clients'

    def __str__(self):
        return self.link

class about(models.Model):
    heading=models.CharField(max_length=50,null=True)
    desc1=models.CharField(max_length=300,null=True)
    desc2=models.CharField(max_length=300,null=True)
    desc3=models.CharField(max_length=300,null=True)

    content=models.CharField(max_length=200,null=True)
    img=models.ImageField(upload_to='img/about',null=True)

    class Meta:
        db_table:'about'

    def __str__(self):
        return self.heading
    

