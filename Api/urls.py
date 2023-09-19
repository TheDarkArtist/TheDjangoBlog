from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

from . import views

router = SimpleRouter()
router.register('v1/users', views.UsersViewSet, basename='users')
router.register('v1/blogs', views.BlogViewSet, basename='blogs')


urlpatterns = [
    path('', views.APIHome.as_view(), name='apihome'),
    path('v1/', SpectacularSwaggerView.as_view(url_name='schema'), name='apibloglist' ),
    path('v1/auth/', include('dj_rest_auth.urls')),
    path('v1/auth/signup/', include('dj_rest_auth.registration.urls')),
    path('auth/', include('rest_framework.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='schema_redoc'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='schema_swagger'),
] + router.urls
