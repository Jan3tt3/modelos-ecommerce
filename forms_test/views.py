from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


def register_view(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/accounts/login/')

    else:

        form = UserRegisterForm(initial={
            'username': 'cliente_ecommerce'
        })

    return render(
        request,
        'forms_test/register.html',
        {'form': form}
    )