from django.conf import settings
from django.urls import path
from . import views
#from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static

app_name="proyect"

urlpatterns = [
     path('', views.login, name="login"),

     path('crear/', views.crear.as_view(), name="crear"),
     path('portafolio/', views.portafolio, name="portafolio2"),
     path('registro/', views.registro.as_view(), name="registro"),

     path('cerrar_sesion/', views.cerrar_sesion, name="cerrar_sesion"),

     path('portafolio_general/', views.portafolio_general, name="portafolio_general"),

      path('delete/<int:id>', views.delete, name="delete"),
      path('edit/<int:id>', views.edit.as_view(), name="edit"),

 
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

