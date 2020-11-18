import graphene
from graphene_django.types import DjangoObjectType
from .models import Product
from graphene_file_upload.scalars import Upload


class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class Query(object):
    all_products = graphene.List(ProductType)

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all().order_by('position')

class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)
    class Arguments:
        code = graphene.String()
        position = graphene.Int()
        quantity = graphene.Int()
        price = graphene.Float()
        description = graphene.String()
        image = Upload()
    success = graphene.Boolean()

    def mutate(self, info, code, position, quantity, price, description, image):
        product = Product(code=code, position=position, quantity=quantity, price=price, description=description, image=image)
        product.save()
        return CreateProduct(product=product)

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()