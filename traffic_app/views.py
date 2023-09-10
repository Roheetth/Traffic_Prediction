from django.shortcuts import render
from .models import predict

# Create your views here.
# Create your views here.  
def home(request):
	return render(request,'index.html')

def input(request):
	return render(request,'input.html')

class_names = ["Normal","Move On","Busy","Heavy","Worst"]

def output(request):
	algo=request.POST.get('algo')
	row=int(request.POST.get('row'))
	#print(row)
	out=predict(algo,row)
	#classes = class_names[int(out)]
	print(out)
	out_put = class_names[int(out-1)]
	
	#print(class_name)
	return render(request,'output.html',{'out':out_put})