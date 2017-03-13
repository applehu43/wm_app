from django.db import models
#from django.contrib import admin

# Create your models here.
class WeightRcd(models.Model):
    id = models.IntegerField(primary_key=True)
#     user_id = models.ForeignKey('UserInfo',on_delete=models.DO_NOTHING)
    user_id = models.IntegerField()
    weight_data = models.DecimalField(max_digits=8,decimal_places=2)
    record_date = models.DateTimeField()
    
    def __str__(self):
        return self.user_id+' in '+self.record_date+' \'weight is:'+self.weight_data
    class Meta:
        db_table = "t_weight_rcd"
      
class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=24)
    password = models.CharField(max_length=24)
    status = models.CharField(max_length=2)
    enabled = models.IntegerField(2)
    real_name = models.CharField(max_length=32)
    qq = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    age = models.IntegerField(4)
    tel = models.CharField(max_length=20) 
    address = models.TextField() 
    def __str__(self):
        return 'user id:'+self.id+", user name:"+self.name
    
    class Meta:
        db_table = "t_user_info"
#admin.register(Record)