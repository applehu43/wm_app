from app import db
import sqlalchemy as sql
# from werkzeug.security import generate_password_hash, check_password_hash
# 
# # Create your models here.
class WeightRcd(db.Model):
    id = sql.Column(sql.Integer,primary_key=True)
#     user_id = sql.Column(sql.ForeignKey('UserInfo',on_delete=sql.Column(sql.DO_NOTHING)
    user_id = sql.Column(sql.Integer)
    weight_data = sql.Column(sql.DECIMAL(8,2))
    record_date = sql.Column(sql.DateTime)

    def __str__(self):
        return self.user_id+' in '+self.record_date+' \'weight is:'+self.weight_data
    class Meta:
        db_table = "t_weight_rcd"

class UserInfo(db.Model):
    id = sql.Column(sql.Integer,primary_key=True)
    name = sql.Column(sql.String(24))
    password = sql.Column(sql.String(128))
#     password_hash = sql.Column(sql.String(128))
#     @property
#     def password(self):
#         raise AttributeError('password is not a readable attribute')
#     @password.setter
#     def password(self,password):
#         self.password_hash = generate_password_hash(password)
#     def verify_password(self,password):
#         return check_password_hash(self.password_hash,password)
    status = sql.Column(sql.String(2))
    enabled = sql.Column(sql.Integer)
    real_name = sql.Column(sql.String(32))
    qq = sql.Column(sql.String(14))
    email = sql.Column(sql.String(100))
    age = sql.Column(sql.Integer)
    tel = sql.Column(sql.String(20)) 
    address = sql.Column(sql.Text) 
    def __str__(self):
        return 'user id:'+self.id+", user name:"+self.name
     
    class Meta:
        db_table = "t_user_info"
#admin.register(Record)