import nltk 
import re
import random
import language_tool_python as lang


class PyGrammar:
    def __init__(self, text: str):
        self.text = text
        self.lang = lang.LanguageToolPublicAPI('en-US')

        if nltk.data.find('tokenizers/punkt') is None:
            nltk.download('punkt')
        else:
            pass

        # Check if 'averaged_perceptron_tagger' is downloaded
        if nltk.data.find('taggers/averaged_perceptron_tagger') is None:
            nltk.download('averaged_perceptron_tagger')
        else:
            pass

        if nltk.data.find('taggers/maxent_ne_chunker') is None:
            nltk.download('maxent_ne_chunker')
        else:
            pass

        # Check if 'words' is downloaded
        if nltk.data.find('corpora/words') is None:
            nltk.download('words')
        else:
            pass
    
    def getPartsOfSpeech(self):
        POS = []
        for t in self.text:
            POS.append(nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(t))))
            
        return POS
    
    def correct(self):
        self.lang.enable_spellchecking()
        getPOS = self.getPartsOfSpeech()
        
        sentences: list = self.text.split(".")
        
        correctedText = ""
        for s in sentences:
            words = str(s).split(" ")
            for _, t in enumerate(words):
                try:
                    if str(t).islower() and getPOS[_] == "NNP" or getPOS[_] == "NNPS":
                        correctedText += str(t).capitalize() + " "
                    else:
                        correctedText += t + " "
                except Exception:
                    correctedText += t + "."
                    
            correctedText = str(re.sub(r'\b(\w+)\s+\1\b', r'\1', correctedText))
            
        correctedText.replace(" .", ".").replace("\'", "")
            
        return self.lang.correct(correctedText)
