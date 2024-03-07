from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Register our participants API
router.register('participants', views.ParticipantViewSet, basename='participant')
router.register('participants/(?P<participant_id>[^/.]+)/blacklists', views.BlacklistViewSet, basename='participant-blacklist')
urlpatterns = router.urls
