from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'homepage/index.html')
    
def test_base(request):
    return render(request, "base.html")
