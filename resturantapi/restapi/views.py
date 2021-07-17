from rest_framework.response import Response
from restapi.serializers import FoodSerializers
from django.shortcuts import render
from django.http import HttpResponse
from .forms import FoodForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Menu

from .serializers import FoodSerializers
# Create your views here.
class FoodList(APIView):
    def get(self,request,format=None):
        foodlist=Menu.objects.all()
        serializer=FoodSerializers(foodlist,many=True)
        return Response(serializer.data)


def home(request):
    return HttpResponse("Welcome,home")


def formpanel(request):
    if request.method=='POST':
        form=FoodForm(request.POST)
        if form.is_valid():
            form=form.save()
            #return HttpResponse('thanks')
        else:
            print(form.errors)
    else:
        form=FoodForm()


    return render(request,'form.html',{'form':FoodForm})