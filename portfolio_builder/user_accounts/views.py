from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
	registered=False
	if(request.method=="POST"):
		user_form=UserForm(data=request.POST)
		if user_form.is_valid:
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			registered=True
			return render(request,'index.html')
	else:
		user_form=UserForm()
	return render(request,'register.html',{'form':user_form})

