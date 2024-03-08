from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.
def upload_file(request):
    def handle(file, word):
            words = open(file).read()
            return words.count(word)
        
    def handle_uploaded_file(f, request_word):
        with open(f"C:/Users/bnn30/Downloads/uploads/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
                
        return handle(f"C:/Users/bnn30/Downloads/uploads/{f.name}", request_word)
                
    
        
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            res = handle_uploaded_file(form.cleaned_data['file'], request.POST.get('word'))
            return render(request, 'index.html', {'count':res})
    else:
        form = UploadFileForm()
        
    return render(request, 'form.html', {'form': form})