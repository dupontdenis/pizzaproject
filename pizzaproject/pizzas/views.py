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

# class PizzaByIngredientApi(APIView):
#     def get(self, request, ingredient):
#         pizzas = Pizza.objects.filter(ingredients__contains=[ingredient])
#         serializer = PizzaSerializer(pizzas, many=True)
#         return Response(serializer.data)

class PizzaByIngredientApi(APIView):
    def get(self, request, ingredient):
        pizzas = Pizza.objects.all()
        pizzas = [p for p in pizzas if ingredient in p.ingredients]
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

class PizzaByIngredientsApi(APIView):
    print(">>> PizzaByIngredientsApi LOADED")
    def get(self, request):
        raw = request.GET.get("ingredients")
        pizzas = Pizza.objects.all()

        if raw:
            ingredients = raw.split(",")
            pizzas = [
                p for p in pizzas
                if all(ing in p.ingredients for ing in ingredients)
            ]

        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)   
