from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.
def upload_file(request):
    
    def handle(file, word):
            words = open(file).read()
            return words.count(word)
        
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            r = handle(request.FILES['file'], request.word)
            return HttpResponse(f'{r}')
    else:
        form = UploadFileForm()
    return render(request, 'form.html', {'form': form})