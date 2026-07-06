# from django.shortcuts import render,redirect
# from .models import Course
# from .forms import Courseform
# # Create your views here.

# def home(request):
#     courses=Course.objects.all()
#     return render(request,"home.html",{"courses":courses})

# def course_add(request):
#     if request.method == 'POST':

#         form=Courseform(request.POST)
#         form.save()
#         return redirect('/')

#     else:
#         form=Courseform()
#     return render(request,'course_add.html',{'form':form})

# def course_details(request,id):
#     form=Course.objects.get(id=id)
#     return render(request,'course_details.html',{'Course':Course})

# def course_update(request,id):
#     course=Course.objects.get(id=id)
#     if request.method=='POST':
#         form = Courseform(request.POST,instance=course)
#         form.save()
#         return redirect('/')
#     else:
#         form = Courseform(instance=course)
#     return render(request,'course_update.html',{'form':form}) 
    
# def course_delete(request,id):
#     course=Course.objects.get(id=id)
#     course.delete()
#     return redirect('/')


from django.shortcuts import render, redirect
from .models import Course
from .forms import Courseform

def home(request):
    courses = Course.objects.all()
    return render(request, "home.html", {"courses": courses})

def course_add(request):
    if request.method == 'POST':
        form = Courseform(request.POST)
        if form.is_valid():  # Added basic form validation
            form.save()
            return redirect('/')
    else:
        form = Courseform()
    return render(request, 'course_add.html', {'form': form})

def course_details(request, id):
    # FIX: Fetch the actual record and store it in a distinct variable name
    course_instance = Course.objects.get(id=id)
    # Pass 'course_instance' as the value, matching the template key 'Course'
    return render(request, 'course_details.html', {'Course': course_instance})

def course_update(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = Courseform(request.POST, instance=course)
        if form.is_valid():  # Added basic form validation
            form.save()
            return redirect('/')
    else:
        form = Courseform(instance=course)
    return render(request, 'course_update.html', {'form': form}) 
    
def course_delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')
