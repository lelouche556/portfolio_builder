from django.db import models
from user_accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Personal_detail(models.Model):
	user= models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	professional_title=models.CharField(max_length=300)
	summary=models.TextField()
	def __str__(self):
		return user.first_name




class Skill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=200)
    skill_rating=models.IntegerField(default=50,validators=[MaxValueValidator(100), MinValueValidator(1)])
    class Meta:
    	unique_together=(("user","skill_name"),)

    def __str__(self):
        return user.first_name+' '+skill_name

class Project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    link=models.URLField()
    class Meta:
    	unique_together=(("user","title"),)
    def __str__(self):
        return title




