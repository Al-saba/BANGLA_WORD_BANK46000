from django.shortcuts import render, redirect
from .forms import WordForm
from .models import Word

def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordForm()
    return render(request, 'vocabulary/add_word.html', {'form': form})

def word_list(request):
    words = Word.objects.all()
    return render(request, 'vocabulary/word_list.html', {'words': words})