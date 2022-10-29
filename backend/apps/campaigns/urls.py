from django.urls import path
from .views import CampaignListAPIView, CampaignDetailAPIView

urlpatterns = [
    path('campaigns/', CampaignListAPIView.as_view(), name="api_campaigns_path"),
    path('campaigns/<str:slug>/', CampaignDetailAPIView.as_view(), name="api_campaign_path")
]
