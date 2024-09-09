from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.categoryname

class Products(models.Model):
    categoryid=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    pname=models.CharField(max_length=200,null=True)
    pcode=models.IntegerField()
    pprice=models.FloatField(default=0)

    def __str__(self):
        return self.pname
    class Meta:
        db_table='Products'


    