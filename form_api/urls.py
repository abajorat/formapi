"""form_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from products import views
from django.conf.urls.static import static
from django.conf import settings
from graphene_file_upload.django import FileUploadGraphQLView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", FileUploadGraphQLView.as_view(graphiql=True, schema=schema)),
    path('', views.ProductList.as_view(), name='product_list'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('create', views.ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>', views.ProductUpdate.as_view(), name='product_edit'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
