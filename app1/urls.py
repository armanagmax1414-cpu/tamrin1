from django.urls import path,include
from .views import MahsolDetailView,ToggleLikeView,CreatCammentView,MahsolList2,MahsolListAPIView,MahsolViewSet,MarketViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'forosh', MahsolViewSet, basename='mahsol')
router.register(r'market',MarketViewSet,basename='market')

urlpatterns = [
    path('', include(router.urls)),
    path('mahsol/',MahsolListAPIView.as_view()),
    path('mahsol/<int:mahsol_id>/', MahsolDetailView.as_view(), name='mahsol-detail'),
    path('mahsol2/',MahsolList2.as_view()),
    path('mahsol/<int:mahsol_id>/like/',ToggleLikeView.as_view()),
    path('mahsol/<int:mahsol_id>/camment/',CreatCammentView.as_view())

]
