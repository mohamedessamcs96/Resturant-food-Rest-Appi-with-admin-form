
from django.urls import path
import restapi
from . import views
urlpatterns = [
    path('',views.home),
    path('formpanel/',views.formpanel),
    path('foodlist/',views.FoodList.as_view()),

]
