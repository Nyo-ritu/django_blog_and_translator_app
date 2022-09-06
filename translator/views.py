from django.shortcuts import render
from .import translate

# Create your views here.

def translator_view(request):
    if request.method =='POST':
        original_text = request.POST['my_textarea']
        output = translate.translate(original_text)
        output_french = translate.translate_french(original_text)
        output_spanish= translate.translate_spanish(original_text)
        output_german= translate.translate_german(original_text)
        output_italian= translate.translate_italian(original_text)
        output_swahili= translate.translate_swahili(original_text)
        output_viet= translate.translate_viet(original_text)
        return render(request, 'translator.html', {'output_text':output, 
        'output_french_text':output_french, 'output_german_text':output_german,
        'output_italian_text':output_italian, 'output_swahili_text':output_swahili,
        'output_viet_text': output_viet,
        'output_spanish_text':output_spanish, 'original_text':original_text})
    else:
        return render(request, 'translator.html')