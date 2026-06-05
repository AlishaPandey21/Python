from django.shortcuts import render

def home(request):
    vehicles = [
        {'id' : 1 , 'name' : "Tesla Model S" , 'price' : 9000000 , 'premium':True},
        {'id' : 2 , 'name' : "Honda City" , 'price' : 1500000 , 'premium':False},
        {'id' : 3 , 'name' : "BMW X5" , 'price' : 9500000 , 'premium':True}
    ]
    context = {
        'title' : "Vehicle List",
        'vehicles' : vehicles , 
        'user_name' : 'Rahul'
    }
    return render(request , 'vehicleapp/home.html',context)

def contact(request):
    message = ""
    if request.method == "POST":
        message = request.POST.get("name")
    return render(request , "vehicleapp/contact.html",{"message":message})