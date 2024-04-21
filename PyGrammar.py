import nltk 
import language_tool_python as lang


class PyGrammar:
    def __init__(self, text: str):
        self.text = text
        self.lang = lang.LanguageToolPublicAPI('en-US')
        nltk.download('punkt'), nltk.download('averaged_perceptron_tagger'), nltk.download('maxent_ne_chunker'), nltk.download('words')

    def getPartsOfSpeech(self):
        POS = []
        for t in self.text:
            POS.append(nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(t))))
            
        return POS
    
    def correct(self):
        getPOS = self.getPartsOfSpeech()
        
        sentences: list = self.text.split(".")
        
        correctedText = ""
        for s in sentences:
            words = str(s).split(" ")
            for _, t in enumerate(words):
                try:
                    nextValue = s[_+1]
                    if t == nextValue:
                        correctedText += t + " "
                        s.remove(nextValue), getPOS.remove(getPOS[_+1])
                    elif str(t).islower() and getPOS[_] == "NNP" or getPOS[_] == "NNPS":
                        correctedText += str(t).capitalize() + " "
                    else:
                        correctedText += t + " "
                except Exception:
                    correctedText += t + "."
            
        return self.lang.correct(correctedText.replace(" .", "."))