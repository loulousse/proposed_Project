from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View
from . forms import *
from . models import *

# Create your views here.

def home(request):
    users = User.objects.all()
    routes = Route.objects.all()
    beepjeeps = BeepJeep.objects.all()
    tickets = Ticket.objects.all()
    context = {
        'users': users,
        'routes': routes,
        'beepjeeps': beepjeeps,
        'tickets': tickets
    }
    return render(request, 'beep/home.html', context)

def features(request):
    return render(request, 'beep/features.html')

def about(request):
    return render(request, 'beep/about.html')

def contact(request):
    return render(request, 'beep/contact.html')

class  dashboard(View):
    def get(self, request):
        user = User.objects.all()
        routes = Route.objects.all()
        beepjeeps = BeepJeep.objects.all()
        tickets = Ticket.objects.all()
        context = {
            'users': user,
            'routes': routes,
            'beepjeeps': beepjeeps,
            'tickets': tickets
       }
        return render(request,'beep/dashboard.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                uid=request.POST.get("user-Id")
                fname=request.POST.get("u-fname")
                lname=request.POST.get("u-lname")
                update_user = User.objects.filter(userId=uid).update(fname=fname, lname=lname)
                print(update_user)

                rid=request.POST.get("route-Id")
                route_from=request.POST.get("r-route_from")
                route_to=request.POST.get("r-route_to")
                fare=request.POST.get("r-fare")
                update_route = Route.objects.filter(routeId=rid).update(route_from=route_from, route_to=route_to,fare=fare)
                print(update_route)

                bid=request.POST.get("beep-Id")
                color=request.POST.get("bj-color")
                capacity=request.POST.get("bj-capacity")
                beepStatus=request.POST.get("bj-beepStatus")
                update_beep = BeepJeep.objects.filter(beepId=bid).update(color=color, capacity=capacity, beepStatus=beepStatus)
                print(update_beep)

                tid=request.POST.get("ticket-Id")
                modeOfPayment=request.POST.get("t-modeOfPayment")
                validTime=request.POST.get("t-validTime")
                update_ticket = Ticket.objects.filter(ticketId=tid).update(modeOfPayment=modeOfPayment, validTime=validTime)
                print(update_ticket)

                print('profile updated')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                uid=request.POST.get("uuser-Id")
                user=User.objects.filter(userId=uid).delete()
                print('recorded deleted')

                print('delete button clicked')
                rid=request.POST.get("rroute-Id")
                route=Route.objects.filter(routeId=rid).delete()
                print('recorded deleted')

                print('delete button clicked')
                bid=request.POST.get("bbeep-Id")
                beepjeeps=BeepJeep.objects.filter(beepId=bid).delete()
                print('recorded deleted')

                print('delete button clicked')
                tid=request.POST.get("tticket-Id")
                tickets=Ticket.objects.filter(ticketId=tid).delete()
                print('recorded deleted')
        return redirect('dashboard_info')



class signin(View):
    def get(self, request):
        return render(request, 'beep/signin.html')
    
    def post(self, request):
        form1 = UserForm(request.POST)
        firstn = request.POST.get("firstname")
        print(firstn)
        lastn = request.POST.get("lastname")
        print(lastn)

        form2 = RouteForm(request.POST)
        location = request.POST.get("location")
        print(location)
        destination = request.POST.get("destination")
        print(destination)

        form3 = BeepJeepForm(request.POST)
        color = request.POST.get("color")
        print(color)
      #   capacity = request.POST.get("capacity")
      #   print(capacity)
     #    status = request.POST.get("status")
     #    print(status)

        form4 = TicketForm(request.POST)
        modeOfPayment = request.POST.get("modeOfPayment")
        print(modeOfPayment)
                
        if form1.is_valid():
            firstn = request.POST.get("firstname")
            lastn = request.POST.get("lastname")

        if form2.is_valid():
            location = request.POST.get("location")
            destination = request.POST.get("destination")
        
        if (location.lower()=='talisay' or location.lower()=='tabunok') and (destination.lower()=='tabuan' or destination.lower()=='n.bacalso'):
            fare=13
        elif (location.lower()=='pardo' or location.lower()=='bulacao') and (destination.lower()=='tabuan' or destination.lower()=='n.bacalso'):
            fare=12
        elif (location.lower()=='tabunok' or location.lower()=='talisay') and (destination.lower()=='minglanilla' or destination.lower()=='shopwise'):
            fare=10 
        elif (location.lower()=='tabunok' or location.lower()=='talisay') and (destination.lower()=='pardo' or destination.lower()=='basak'):
            fare=9
        elif (location.lower()=='tabunok' or location.lower()=='talisay') and (destination.lower()=='bulacao' or destination.lower()=='tabunok'):
            fare=8

        if form3.is_valid():
            color = request.POST.get("color")       
        #     capacity = request.POST.get("capacity")
        #     status = request.POST.get("status")
        if color == 'blue':
            capacity = 'available'
            beepStatus = 33       
        elif color == 'white':
            capacity = 'available'
            beepStatus = 31

        if form4.is_valid():
            modeOfPayment = request.POST.get("modeOfPayment")

        if modeOfPayment == 'paymaya':
            validTime = 24 
        elif modeOfPayment == 'gcash':
            validTime = 24

        #User.objects.filter(fname = firstn, lname = lastn)
        #User.objects.get(userId)
        form1 = User(fname = firstn, lname = lastn)
        #form1.save()
        #userId = User.objects.get(userId = form1.userId)

        
        form2 = Route(route_from = location, route_to = destination, fare = fare)
        
        form3 = BeepJeep(color = color, capacity = capacity, beepStatus = beepStatus)
        form4 = Ticket(modeOfPayment = modeOfPayment, validTime = validTime)
      
        form1.save()
        form2.save()
        form3.save()
        form4.save()

        return redirect('dashboard_info')

def signup(request):
    context ={}
    form = ColorForm()
    context['form']= form
    if request.GET:
        temp = request.GET['color_field']
        print(temp)
    return render(request, 'beep/signup.html', context) 


    
    

#class DashboardView(View):
#    def get(self, request):
#        users = User.objects.all()
#        context = {
#            'users': users
#        }
#        return render(request, 'dashboard.html', context)


