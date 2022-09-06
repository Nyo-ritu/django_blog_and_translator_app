from googletrans import Translator

def translate(text):
    translator = Translator()
    translation = translator.translate(text=text, dest='zh-CN' )
    return translation.text

def translate_french(text):
    translator = Translator()
    translation_french = translator.translate(text=text, dest='fr' )
    return translation_french.text

def translate_spanish(text):
    translator = Translator()
    translation_spanish = translator.translate(text=text, dest='es' )
    return translation_spanish.text

def translate_german(text):
    translator = Translator()
    translation_to_german = translator.translate(text=text, dest='de' )
    return translation_to_german.text

def translate_italian(text):
    translator = Translator()
    translation_to_italian = translator.translate(text=text, dest='it' )
    return translation_to_italian.text

def translate_swahili(text):
    translator = Translator()
    translation_to_swahili = translator.translate(text=text, dest='sw' )
    return translation_to_swahili.text

def translate_viet(text):
    translator = Translator()
    translation_to_viet = translator.translate(text=text, dest='vi' )
    return translation_to_viet.text