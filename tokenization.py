# %%
from nltk.tokenize import word_tokenize
print(word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
# Separate based on whitespace and signs - 'Do', "n't"

# %%
from nltk.tokenize import WordPunctTokenizer  
print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
# Separate based on whitespace and signs - 'Don', "'", 't'

# %%
from tensorflow.keras.preprocessing.text import text_to_word_sequence
print(text_to_word_sequence("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
# Separate based on whitespace but keep apostrophes - "don't"

# %%
from nltk.tokenize import TreebankWordTokenizer
tokenizer=TreebankWordTokenizer()
text="Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
print(tokenizer.tokenize(text))
# Keep hyphenated words and separate apostrophes - 'does', "n't"

# %%
from nltk.tokenize import sent_tokenize
text="His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."
print(sent_tokenize(text))
# Separate into sentences

# %%
from nltk.tokenize import sent_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D student."
print(sent_tokenize(text))
# Separate into sentences regardless of periods within the sentence

# %%
import kss
text='딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어려워요. 농담아니에요. 이제 해보면 알걸요?'
print(kss.split_sentences(text))
# Separate Korean sentences

# %%
from nltk.tokenize import word_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D. student."
print(word_tokenize(text))

# %%
import nltk
nltk.download('averaged_perceptron_tagger')

from nltk.tag import pos_tag
text="I am actively looking for Ph.D. students. and you are a Ph.D. student."
x=word_tokenize(text)
pos_tag(x)
# parts of speach, refer to Penn Treebank POG Tags

# %%
from konlpy.tag import Okt  
okt=Okt()  
print(okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# Separate based on morpheme (형태소)
print(okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# Tag parts of speach on morpheme
print(okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# print nouns

# %%
from konlpy.tag import Kkma  
kkma=Kkma()  
print(kkma.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# Separate based on morpheme (형태소)
print(kkma.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# Tag parts of speach on morpheme
print(kkma.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# print nouns

# %%
