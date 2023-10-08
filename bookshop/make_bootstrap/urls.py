from django.urls import path
from . import views as make_bootstrap

urlpatterns = [
    path("bootstrap/", make_bootstrap.BootstrapView.as_view(), name='bootstrap_page_handler'),
    path("bootstrap/index/", make_bootstrap.get_index, name='get_index'),
]
