
from django.urls import path
from .views import index,home,SingleMenuItemView,MenuItemsView, msg
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('',home,name="home"),
    path('menu-items/',MenuItemsView.as_view()),
    path('menu-items/<int:pk>',SingleMenuItemView.as_view()),
    #path('booking/',BookingViewSet),
    #path('booking/<int:pk>',SingleBookingView),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token),
]
