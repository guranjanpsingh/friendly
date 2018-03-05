from rest_framework.routers import DefaultRouter
from rest_framework_extensions import NestedRouterMixin


class NestedDefaultRouter(DefaultRouter, NestedRouterMixin):
    pass