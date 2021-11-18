from django.urls import path
from .views import (leads_list, lead_details, create_lead,
                    lead_update, lead_delete, LeadListView, LeadDetailView, LeadDeleteView, LeadCreateView)

app_name = 'leads'
urlpatterns = [
    path('', LeadListView.as_view(), name='leads-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-details'),
    path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
]
