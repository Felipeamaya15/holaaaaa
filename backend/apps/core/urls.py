from django.urls import path #importa el metodo path
from . import views #improta los metodos de que se implementan en el views,py de este directorio
from apps.core.presentation.views import VarianteProductoListCreateView
'''
En esta sección configuramos las urls que nuestra aplicación usará, si necesitamos renderizar 
una vista o debemos incluirla en el urlpatternes de la app la función path requiere de tres 
parametros el primero indica el como se llamara desde el navegador, se deja en blanco solo para 
la pagina de inicio, el segundo parametro indica que función del views que importamos en la línea 3
usaremos para la url consultada, esta debe existir, el tercer parametro el nombre que le daremos
'''
urlpatterns = [
    # Vistas existentes del módulo
    path('', views.home, name='home'),
    path('check_profile/', views.check_profile, name='check_profile'),
    path('main_admin/', views.main_admin, name='main_admin'),

    # Endpoint para listar y crear variantes de un producto
    path('productos/<int:id_producto>/variantes/', VarianteProductoListCreateView.as_view(), name='variantes-list-create'),
]
