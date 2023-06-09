from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from health import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('equipment/',include('equipment.urls')),
    path('lowerbody/',include('lowerbody.urls')),
    path('upperbody/',include('upperbody.urls')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('meaning/',views.meaningPage,name="meaningPage"),
    path('effect/',views.effectPage,name='effectPage'),
    path('caution/',views.cautionPage,name="cautionPage"),
    path('contact/',views.contactPage,name="contactPage"),
    path('recommend/',views.recommendPage,name="recommendPage"),
    path('authaccounts/', include('allauth.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)