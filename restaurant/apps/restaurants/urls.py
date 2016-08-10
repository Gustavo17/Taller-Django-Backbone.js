from django.conf.urls import url, include
from rest_framework import routers
from .views import IndexView
from .viewSets import RestaurantViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
	url(r'^$', IndexView.as_view(), name="index"),

	url(r'^api/', include(router.urls)),    
]