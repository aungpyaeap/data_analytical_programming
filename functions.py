from tkinter import *
import re,nltk
import pandas as pd


# Enter full screen mode
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

# functions
def donothing():
    for i in range(1):
        gridframe = Frame(window)
        Label(gridframe, text="FREQUENCY DISTRIBUTION: 000", font='arial 12', fg="blue4").pack(side=TOP)
        Label(gridframe, text="TOKEN LENGTH: 000", font='arial 12', fg="blue4").pack(side=TOP)
        Label(gridframe, text="WORD LENGTH: 000", font='arial 12', fg="blue4").pack(side=TOP)
        gridframe.grid(row=1, column=2, sticky= E)

def exit():
    window.destroy()

print("True")  

import re,nltk
f = open('essay.txt')
bigram_sentence = f.read()
from nltk.tokenize import sent_tokenize, word_tokenize
bigram_tokens = word_tokenize(bigram_sentence)
bigram_tokens = [word.lower() for word in bigram_tokens]
bigram_words = [word for word in bigram_tokens if word.isalpha()]

from nltk.tokenize.treebank import TreebankWordDetokenizer
bigram_sentence = TreebankWordDetokenizer().detokenize(bigram_words)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer(ngram_range=(2,2),use_idf=False)

corpus = [bigram_sentence]

matrix = vec.fit_transform(corpus).toarray()
vocabulary = vec.get_feature_names()

all_bigrams = []
all_frequencies = []
false_inputs = []
auto_words = []


print("OK")

#------------------------------------------------- HIGHLIGHT TEXT
def color_text(textbox2, tag, word, fg_color='black', bg_color='white'):
    # add a space to the end of the word
    word = word + " "
    textbox2.insert('end', word)
    end_index = textbox2.index('end')
    begin_index = "%s-%sc" % (end_index, len(word) + 1)
    textbox2.tag_add(tag, begin_index, end_index)
    textbox2.tag_config(tag, foreground=fg_color, background=bg_color)

#------------------------------------------------- CLEAR
def clear_all_values():
    false_inputs.clear()
    auto_words.clear()
    textbox2.delete('1.0', END)

#------------------------------------------------- START BUTTON INSTRUCTIONS
def start():
    sentence = textbox1.get('1.0', END)
    clear_all_values()
    #suggestion_array.clear()
    #min_words.clear()
   
    from nltk.tokenize import sent_tokenize, word_tokenize
    tokens = word_tokenize(sentence)
    if not tokens:
        messagebox.showinfo("Error","Please put character in textarea")
    else:
        tokens = [word.lower() for word in tokens]
        words = [word for word in tokens if word.isalpha()]

        for word in words:
            auto_words.append(word)
            for bigram in vocabulary:
                if word in bigram:
                    index = vocabulary.index(bigram)
                    tuple_bigram = tuple(bigram.split(' '))
                    frequency = matrix[:,index].sum()
                    all_bigrams.append(tuple_bigram)
                    all_frequencies.append(frequency)
        
        for i in range(1):
            gridframe = Frame(window)
            Label(gridframe, text="TOKEN LENGTH\n" + str(len(tokens)), font='arial 12', fg="blue4").pack(side=TOP)
            Label(gridframe, text="WORD LENGTH\n" + str(len(words)), font='arial 12', fg="blue4").pack(side=TOP)
            gridframe.grid(row=1, column=2, sticky= E)
            #textbox2.insert('end', words)
            
            for f_word in words:   # detecting non words
                if f_word not in bigram_tokens:
                    false_inputs.append(f_word)
                    print(false_inputs)

        false_words = false_inputs
        list_false_words = StringVar(value=false_words)
        Listbox(window, listvariable=list_false_words, width=30, height=8, font='arial 10', fg='black', bg='white').grid(row=4, column=2, sticky=E)
            
        sentenct_words = sentence.split()
        tags = ["tg" + str(k) for k in range(len(sentenct_words))]
        for ix, word in enumerate(sentenct_words):
            
            for h_word in false_inputs:
                if word[:len(h_word)] == word:
                    color_text(textbox2, tags[ix], word, 'red', 'yellow')
                else:
                    color_text(textbox2, tags[ix], word)

#------ show bigram
def show_bigram():
    x=0
#    
#    import sys 
#    window = Tk()
#    t1 =Text(window)
#    t1.grid(row=0, column=0)
#    t1.pack()
#    
    for word in auto_words:
        for bigram in vocabulary:
            if word in bigram:
                index = vocabulary.index(bigram)
                tuple_bigram = tuple(bigram.split(' '))
                frequency = matrix[:,index].sum()
                all_bigrams.append(tuple_bigram)
                all_frequencies.append(frequency)
    
    df = pd.DataFrame({'bigram':all_bigrams,'frequency':all_frequencies})
    df.sort_values('frequency',inplace=True)
    
    bigram_list = (df[['bigram','frequency']])
    
    list_bigram_words = StringVar(value=bigram_list)
    
    Listbox(window, listvariable=list_bigram_words, width=30, height=8, font='arial 10', fg='black', bg='white').grid(row=7, column=4, sticky=E)
    
    #for item in bigram_list:
        #listbox1 = Listbox(window, width=30, height=8, font='arial 10', fg='black', bg='white').grid(row=7, column=4)
        #listbox1.insert(end, item)

#    class PrintToT1(object): 
#        def write(self, s): 
#            t1.insert(END, s) 
#
#    sys.stdout = PrintToT1() 
#
#    print ('Bigram with frequencies') 
#    print (df)
#    
#    window.mainloop()

############## Minimum edit distace == 2
import re
from collections import Counter

def key_words(text): return re.findall(r'\w+', text.lower())

DICT_WORDS = Counter(key_words(open('essay.txt').read()))

def P(word, N=sum(DICT_WORDS.values())): 
    "Probability of `word`."
    return DICT_WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(key_words): 
    "The subset of `key_words` that appear in the dictionary of DICT_WORDS."
    return set(w for w in key_words if w in DICT_WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def auto_nlp():
    textbox3.delete('1.0', END)
    from nltk.tokenize.treebank import TreebankWordDetokenizer
    final_sentence = TreebankWordDetokenizer().detokenize(auto_words)

    for s_word in false_inputs:
        final_sentence = final_sentence.replace(s_word,correction(s_word))

    textbox3.insert('end', final_sentence)
    