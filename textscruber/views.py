from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def scrubber(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    numberremover= request.GET.get('numberremover', 'off')

    extraspaceremover = request.GET.get('extraspaceremover', 'on')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        scrubbed = ""
        for char in djtext:
            if char not in punctuations:
                scrubbed = scrubbed + char
        params = {'purpose':'Removed Punctuations', 'scrubbed_text': scrubbed}
        return render(request, 'scrubber.html', params)

    elif(fullcaps=="on"):
        scrubbed = ""
        for char in djtext:
            scrubbed = scrubbed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'scrubbed_text': scrubbed}
        # Analyze the text
        return render(request, 'scrubber.html', params)

    elif(extraspaceremover == "on"):
        scrubbed= ""
        for index, char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index+1]==" "):
                pass
            else:
                scrubbed = scrubbed + char

        params = {'purpose': 'Removed Spaces', 'scrubbed_text': scrubbed}
        # Analyze the text
        return render(request, 'scrubber.html', params)

    elif (newlineremover == "on"):
        scrubbed = ""
        for char in djtext:
            if char != "\n":
                scrubbed = scrubbed+ char

        params = {'purpose': 'Removed NewLines', 'scrubbed_text': scrubbed}
        # Analyze the text

        return render(request, 'scrubber.html', params)
    elif (numberremover == "on"):
        scrubbed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
               scrubbed = scrubbed + char

        params = {'purpose': 'Removed Numbers', 'scrubbed_text': scrubbed}
    else:
        return HttpResponse("Error")

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')





