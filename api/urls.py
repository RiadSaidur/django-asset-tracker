from django.urls import path, include


urlpatterns = [
  path('company/', include('company.urls')),
  path('employee/', include('employee.urls')),
  path('asset/', include('asset.urls')),
]