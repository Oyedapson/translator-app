from googletrans import Translator
from googletrans.constants import LANGUAGES

translator = Translator()

def translate(data, search_lang):
    status = False
    lang = LANGUAGES
    for key in lang.keys():
        print(lang[key].lower(), search_lang, search_lang == lang[key].lower())
        if search_lang == lang[key].lower():
            status = True
            res = translator.translate(data, dest=key).text
            print(res)
            return res, key 
    if status == False:
        return "Desired Language not found", False
    else:
        return "Try again", False

def languages():
    return LANGUAGES.values()
