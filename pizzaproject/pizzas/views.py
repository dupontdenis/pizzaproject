from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pizza
from .serializers import PizzaSerializer

class PizzaListApi(APIView):
    def get(self, request):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)


class PizzaDetailByNameApi(APIView):
    def get(self, request, name):
        try:
            pizza = Pizza.objects.get(name=name)
        except Pizza.DoesNotExist:
            return Response({"error": "Pizza not found"}, status=404)

        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)

