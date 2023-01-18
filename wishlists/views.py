from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serialize import Wishlistserializer
from .models import Wishlist


class Wishlists(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serialize = Wishlistserializer(
            all_wishlists,
            many=True,
            context={"request": request},
        )

        return Response(serialize.data)

    def post(self, request):
        serializer = Wishlistserializer(data=request.data)
        if serializer.is_valid():
            wishlist = serializer.save(
                user=request.user,
            )
            serializer = Wishlistserializer(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
