from django.urls import path
from .views import OrganizationCreateView, OrganizationDetailView

urlpatterns = [
    path('', OrganizationCreateView.as_view(), name='organization-create'),
    path('<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
]