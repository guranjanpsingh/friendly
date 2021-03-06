from .views import UserLocationsViewSet, UsersView
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import api

#
router = api.NestedDefaultRouter()
users_router = router.register("users", UsersView)
users_router.register("locations", UserLocationsViewSet, base_name="user-locations", parents_query_lookups=['user'])
router.register("users", UsersView)

#
# router = DefaultRouter()
# router.register("userlocations", UserLocationsViewSet)
# router.register("users", UsersView)

urlpatterns = router.urls