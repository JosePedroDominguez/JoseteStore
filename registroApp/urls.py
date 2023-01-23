from django.urls import path

from registroApp.views import registro

urlpatterns = [
    ###############URLS de store###############
    path('registro/', registro,name="registro"),
    #####################################
]

