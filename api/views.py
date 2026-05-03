from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import Product


class ProductApiView(APIView):

    # CONSULTAR / LISTAR
    def get(self, request, *args, **kwargs):

        product_id = request.GET.get("id", None)

        # CONSULTAR UN PRODUCTO
        if product_id is not None:

            try:
                product = Product.objects.get(id=product_id)

                data = model_to_dict(product)

                return Response(data)

            except Product.DoesNotExist:

                return Response({
                    "error": "Producto no encontrado"
                }, status=404)

        # LISTAR TODOS LOS PRODUCTOS
        queryset = Product.objects.all()

        data = []

        for product in queryset:

            item = model_to_dict(product)

            data.append(item)

        return Response(data)

    # CREAR PRODUCTO
    def post(self, request, *args, **kwargs):

        data = request.data

        print("POST DATA:", data)

        product = Product.objects.create(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price")
        )

        return Response({
            "message": "Producto creado correctamente",
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price
        })

    # ACTUALIZAR PRODUCTO
    def put(self, request, *args, **kwargs):

        data = request.data

        print("PUT DATA:", data)

        product_id = data.get("id")

        try:

            product = Product.objects.get(id=product_id)

            product.name = data.get("name", product.name)
            product.description = data.get(
                "description",
                product.description
            )
            product.price = data.get("price", product.price)

            product.save()

            return Response({
                "message": "Producto actualizado correctamente"
            })

        except Product.DoesNotExist:

            return Response({
                "error": "Producto no encontrado"
            }, status=404)

    # ELIMINAR PRODUCTO
    def delete(self, request, *args, **kwargs):

        data = request.data

        print("DELETE DATA:", data)

        product_id = data.get("id")

        try:

            product = Product.objects.get(id=product_id)

            product.delete()

            return Response({
                "message": "Producto eliminado correctamente"
            })

        except Product.DoesNotExist:

            return Response({
                "error": "Producto no encontrado"
            }, status=404)