from django.shortcuts import render, redirect

from .forms import UserRegisterForm


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