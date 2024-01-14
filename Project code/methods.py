from googletrans import Translator,LANGUAGES


class MyTranslator:
    langs =LANGUAGES
    languages={ j:i for i,j in LANGUAGES.items()}
    def run(self,txt='Type text here',src='en',dest='hi'):
          translator = Translator() 
          translated_text = translator.translate(txt, src=src, dest=dest).text
          return translated_text

