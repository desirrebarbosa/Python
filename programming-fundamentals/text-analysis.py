given_string = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
          
    def process_text(self):
        formatted_text = self.text.replace('.','').replace('!','').replace('?','').replace(',','')
        formatted_text = formatted_text.lower()

        self.ftext = formatted_text

    def count_freq(self):
        word_list = self.ftext.split(' ')

        freq_dict = {}
        for word in set(word_list):
            freq_dict[word] = word_list.count(word)
        self.f_dict = freq_dict
        return freq_dict
    
    def freq_of(self, word):
        return self.f_dict[word]
    
text_analyze = TextAnalyzer(given_string)
text_analyze.process_text()
freq = text_analyze.count_freq()
print(freq)
lorem = text_analyze.freq_of('lorem')
print(lorem)
