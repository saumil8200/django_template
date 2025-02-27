from django.shortcuts import render

# Create your views here.
def app(request, pk=None):
    context = {'pk': pk}
    return render(request, "app/app.html", context)