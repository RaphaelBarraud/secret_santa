from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Register our participants API
router.register('draws', views.DrawViewSet, basename='draw')
router.register('draws/(?P<draw_id>[^/.]+)/draw_results', views.DrawResultViewSet, basename='draw-draw_result')
urlpatterns = router.urls
