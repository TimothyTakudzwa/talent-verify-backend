from django.urls import path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from company.views import CompanyViewSet, DepartmentViewSet, EmployeeRolesViewSet, EmployeeViewSet
from user.views import UserViewSet

# Create a router and register the viewsets
router = routers.DefaultRouter()
router.register('company', CompanyViewSet)
router.register('employees', EmployeeViewSet)
router.register('departments', DepartmentViewSet)
router.register('employeeRoles', EmployeeRolesViewSet)
router.register('user', UserViewSet)


# Swagger/OpenAPI schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Talent Verify API",
        default_version='v1',
        description="Talent Verify API Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="Timothy Ngorima License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # API documentation endpoints
    path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # JWT token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Include router URLs
    path('', include(router.urls)),
]
