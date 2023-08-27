from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

from . import views

urlpatterns = [
    path('', views.APIHome.as_view(), name='apihome'),
    path('v1/', views.BlogViewSet.as_view({'get':'list'}),name='apibloglist' ),
    path('v1/users/', views.UsersViewSet.as_view({'get': 'list'}), name='apiusers'),
    path('v1/auth/', include('dj_rest_auth.urls')),
    path('v1/auth/signup/', include('dj_rest_auth.registration.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='schema_redoc'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='schema_swagger'),
]
