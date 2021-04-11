from django.shortcuts import render,redirect
import numpy as np
from django.core.files.storage import FileSystemStorage
from PIL import Image as Img
from pathlib import Path
import os
import matplotlib.pyplot as plt
from .models import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def uploadPage_aerial(request):
	url=""
	print("\n12121212212121")
	if request.method=="POST":
		img=request.FILES['image']
		fs=FileSystemStorage()
		filename=fs.save('input',img)
		Image.objects.create(input_loc=filename,output_loc=filename)
		img=Image.objects.all()
		if len(img)>1:
			os.remove(os.path.join(BASE_DIR,'test\\'+img[0].input_loc))
			img.filter(id=img[0].id).delete()
		print((list(Image.objects.all()))[-1])	
		return redirect('display_output')
	
	context={'loc': url,'flag':False}
	#print(request.method)	
	return render(request,'uploadPage_Aerial.html')

def uploadPage_sketch(request):
	url=""
	print("\n12121212212121")
	if request.method=="POST":
		img=request.FILES['image']
		fs=FileSystemStorage()
		filename=fs.save('input',img)
		Image.objects.create(input_loc=filename,output_loc=filename)
		img=Image.objects.all()
		if len(img)>1:
			os.remove(os.path.join(BASE_DIR,'test\\'+img[0].input_loc))
			img.filter(id=img[0].id).delete()
		print((list(Image.objects.all()))[-1])	
		return redirect('display_output')
	
	context={'loc': url,'flag':False}
	#print(request.method)	

	return render(request,'uploadPage_Sketch.html',context)

def uploadPage_semantic(request):
	url=""
	print("\n12121212212121")
	if request.method=="POST":
		img=request.FILES['image']
		fs=FileSystemStorage()
		filename=fs.save('input',img)
		Image.objects.create(input_loc=filename,output_loc=filename)
		img=Image.objects.all()
		if len(img)>1:
			os.remove(os.path.join(BASE_DIR,'test\\'+img[0].input_loc))
			img.filter(id=img[0].id).delete()
		print((list(Image.objects.all()))[-1])	
		return redirect('display_output')
	
	context={'loc': url,'flag':False}
	#print(request.method)	
	return render(request,'uploadPage_Semantic.html')	

def display_output(request):
	img=Image.objects.all()
	l=len(img)
	k=img[l-1]
	s1,s2=k.input_loc,k.output_loc	
	s1='/test/'+s1	
	s2='/test/'+s2		
	print(k.input_loc)
	#print(np.array(Img.open(k.input_loc)))
	context={'inp':s1,'out':s2}
	return render(request,'display_output.html',context)		
