from django.shortcuts import render

# Create your views here.
def home(request):
   
    return render(request,"home.html")
def about(request):
    # name = "A"
#----------------------------------------------------------------------
    # std_id=[1,2,3,4,5]
    # std_name=['A','B','C','D','E']
    # data ={
    #     'std_id' :std_id,
    #     'std_name':std_name
    # }
#----------------------------------------------------------------------
     data={
        'cname':"python",
        'duration':'2 months',
        'cfees':5000,
        'result':90
     }
#----------------------------------------------------------------------
    # return render(request,"about.html",{'nm':name})
#---------------------------------------------------------
    # return render(request,"about.html",data)
#--------------------------------------------------------------------    
     return render(request,"about.html",{'data':data})


def course(request):
    # result=60

    data={
        'cname':['python','php','java','css'],
        'cfees':[1000,2000,3000,4000]
    }
    return render(request,"course.html",{'data':data})

