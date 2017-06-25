from django.conf.urls import url
from products import views

urlpatterns = [
    # url(r'^landing123/', views.landing, name='landing'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]