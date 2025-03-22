from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse

from ratings.models import Rating
from ratings.forms import RatingForm



def home(request):
    ratings = Rating.objects.all()  #  Load all ratings
    return render(request, 'ratings/home.html', {'ratings': ratings})
#def home(request):
#    """ Show the entry point to the ratings app
#    :param request: Django request object
#    :return: rendered homepage
#    """
#    context = {'ratings': Rating.objects.all()}
#    return render(request, 'home.html', context)
#    
def delete_rating(request, row_id):
    rating = get_object_or_404(Rating, id=row_id)
    rating.delete()
    return redirect('rating-home')

def delete(request, row_id):
    rating = get_object_or_404(Rating, pk=row_id)
    rating.delete()
    context = {'ratings': Rating.objects.all()}
    return redirect('rating-home')

def edit_rating(request, row_id):
    rating = get_object_or_404(Rating, id=row_id)
    form = RatingForm(instance=rating)  # Pre-fill form with data

    if request.method == "POST":
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            return redirect('rating-home')  # Ensure this matches `urls.py`

    return render(request, 'ratings/edit.html', {'form': form})

def edit(request, row_id):
    rating = get_object_or_404(Rating, pk=row_id)
    form = RatingForm(request.POST or None, instance=rating)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('rating-home')
        else:
            return HttpResponse("Invalid entry.")
    else:
        context = {'form': form}
        form = RatingForm(instance=rating)
        return render(
            request,
            'ratings/entry_def.html',
             context
        )

def add_new(request, row_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            beer_name = form.cleaned_data['beer_name']
            score = form.cleaned_data['score']
            notes = form.cleaned_data['notes']
            brewer = form.cleaned_data['brewer']
            return redirect('rating-home')
    else:
        form = RatingForm()

    return render(request, 'rating-home', {'form': form})

def add(request):
    if request.method == "POST":
        print(request.POST)
        form = RatingForm(request.POST)
        print( form )
        if form.is_valid():
            form.save()
            return redirect('rating-home')
        else:
            return HttpResponse("Invalid entry.")
    else:
        context = {'form': form}
        form = RatingForm(instance=rating)
        return render(
            request,
            'ratings/entry_def.html',
             context
        )


class RatingCreate(View):
    """ Create a new Rating """
    form_class = RatingForm
    template_name = 'ratings/home.html'

    def get(self, request):
        form = self.form_class()
        context = {'ratings': Rating.objects.all(), 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            _ = form.save()
            return redirect('rating-home')
        return render(request, self.template_name, {'form: form'})
        
def add_rating(request):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rating-home')  # ✅ Redirect back to home

    else:
        form = RatingForm()

    return render(request, 'ratings/add.html', {'form': form})
