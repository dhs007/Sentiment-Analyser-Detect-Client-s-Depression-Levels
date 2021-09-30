import pandas as pd
import numpy as np
import nltk
print("\n\n")
df=pd.read_csv("smallcsvdata.csv")
print("Dataset.................")
print (df)
print("\n\n")
from nltk.tokenize import word_tokenize
from nltk import pos_tag, pos_tag_sents
#stopwords removal////////////////////////
print("lower..............\n\n")
texts = df['Review_Text'].map(lambda Review_Text: Review_Text.lower())#..............................converting to   lower case
print(texts)
df['texts']=texts
print("Tokenisation..............\n\n")
token = df.apply(lambda row: nltk.word_tokenize(row['texts']), axis=1)
df['tokenized_words']=token
print(df['tokenized_words'])
print("stopwords removal///////////////////////")
words=df['tokenized_words']
from nltk.corpus import stopwords
texts = df['Review_Text'].map(lambda Review_Text: Review_Text.lower())#..............................converting to   lower case
print(texts)
df['texts']=texts
print("Tokenisation..............\n\n")
token = df.apply(lambda row: nltk.word_tokenize(row['texts']), axis=1)
df['tokenized_words']=token
print(df['tokenized_words'])
print("stopwords removal///////////////////////")
words=df['tokenized_words']
from nltk.corpus import stopwords
texts = df['Review_Text'].map(lambda Review_Text: Review_Text.lower())#..............................converting to   lower case
print(texts)
df['texts']=texts
print("Tokenisation..............\n\n")
token = df.apply(lambda row: nltk.word_tokenize(row['texts']), axis=1)
df['tokenized_words']=token
print(df['tokenized_words'])
print("stopwords removal///////////////////////")
words=df['tokenized_words']
from nltk.corpus import stopwords
#stop_words = set(stopwords.words('english'))
usertext = token
stop_words=['a', 'able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','by','did','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','may','me','might','my','of','off','on','or','other','our','own','rather','said','say','says','she','should','since','so','than','that','the','their','them','then','there','these','they','this','tis','to','was','us','was','we','were','what','when','where','while','who','whom','why','will','would','yet','you','your','They','Look','Good','A', 'Able','About','Across','After','All','Almost','Also','Am','Among','An','And','Any','Are','As','At','Be','Because','Been','By','Did','Else','Ever','Every','For','From','Get','Got','Had','Has','Have','He','Her','Hers','Him','His','How','However','I','If','In','Into','Is','It','Its','Just','Least','Let','May','Me','Might','My','Of','Off','On','Or','Other','Our','Own','Rather','Said','Say','Says','She','Should','Since','So','Than','That','The','Their','Them','Then','There','These','They','This','Tis','To','Was','Us','Was','We','Were','What','When','Where','While','Who','Whom','Why','Will','Would','Yet','You','Your','!','@','#','"','$','(','.',')']                                                                                               
clean = usertext.apply(lambda x: [word for word in x if word not in stop_words])
df['clean']=clean
print(df['clean'])
print("\n")
print("Pos_Tagging..............\n\n")
df['tagged_texts'] = df.apply(lambda df:nltk.pos_tag(df['clean']),axis=1)
print(df['tagged_texts'])
print("\n\n")
print("Array..............\n\n")
tagged=np.array(df['tagged_texts'])
print(tagged)
pos=neg=obj=count=0
for word, tag in tagged:
    ss_set = None
    if 'NN' in tag and swn.senti_synsets(word):
        ss_set = list(swn.senti_synsets(word))[0]
    elif 'VB' in tag and swn.senti_synsets(word):
        ss_set = list(swn.senti_synsets(word))[0]
    elif 'JJ' in tag and swn.senti_synsets(word):
         ss_set = list(swn.senti_synsets(word))[0]
    elif 'RB' in tag and swn.senti_synsets(word):
         ss_set = list(swn.senti_synsets(word))[0]
    if ss_set:
        pos=pos+synset.pos_score() #check the positive score and verify
        neg=neg+synset.neg_score()
        obj=obj+synset.obj_score()
        count+=1
final_score=pos-neg
print(final_score)
df['final_score']=final_score
df.to_csv('smallcsvdata2.csv')
norm_finalscore= round((final_score) / count, 2)
print(norm_finalscore)
final_sentiment = 'positive' if norm_finalscore >= 0 else 'negative'
print(final_sentiment)


import pandas as pd
import numpy as np
import nltk
print("\n\n")
df=pd.read_csv("smallcsvdata.csv")
print("Dataset.................")
print (df)
print("\n\n")
from nltk.tokenize import word_tokenize
from nltk import pos_tag, pos_tag_sents
#stopwords removal////////////////////////
print("lower..............\n\n")
texts = df['Review_Text'].map(lambda Review_Text: Review_Text.lower())#..............................converting to   lower case
print(texts)
df['texts']=texts
print("Tokenisation..............\n\n")
token = df.apply(lambda row: nltk.word_tokenize(row['texts']), axis=1)
df['tokenized_words']=token
print(df['tokenized_words'])
print("stopwords removal///////////////////////")
words=df['tokenized_words']
from nltk.corpus import stopwords
#stop_words = set(stopwords.words('english'))
usertext = token
stop_words=['a', 'able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','by','did','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','may','me','might','my','of','off','on','or','other','our','own','rather','said','say','says','she','should','since','so','than','that','the','their','them','then','there','these','they','this','tis','to','was','us','was','we','were','what','when','where','while','who','whom','why','will','would','yet','you','your','They','Look','Good','A', 'Able','About','Across','After','All','Almost','Also','Am','Among','An','And','Any','Are','As','At','Be','Because','Been','By','Did','Else','Ever','Every','For','From','Get','Got','Had','Has','Have','He','Her','Hers','Him','His','How','However','I','If','In','Into','Is','It','Its','Just','Least','Let','May','Me','Might','My','Of','Off','On','Or','Other','Our','Own','Rather','Said','Say','Says','She','Should','Since','So','Than','That','The','Their','Them','Then','There','These','They','This','Tis','To','Was','Us','Was','We','Were','What','When','Where','While','Who','Whom','Why','Will','Would','Yet','You','Your','!','@','#','"','$','(','.',')']                                                                                               
clean = usertext.apply(lambda x: [word for word in x if word not in stop_words])
df['clean']=clean
print(df['clean'])
print("\n")
print("Pos_Tagging..............\n\n")
df['tagged_texts'] = df.apply(lambda df:nltk.pos_tag(df['clean']),axis=1)
print(df['tagged_texts'])
print("\n\n")
print("Array..............\n\n")
tagged=np.array(df['tagged_texts'])
print(tagged)
pos=neg=obj=count=0
for word, tag in tagged:
    tagged=np.array(df['tagged_texts'])
print(tagged)
pos=neg=obj=count=0
for word, tag in tagged:
    ss_set = None
    tagged=np.array(df['tagged_texts'])
print(tagged)
pos=neg=obj=count=0
for word, tag in tagged:
    ss_set = None
    ss_set = None
    if 'NN' in tag and swn.senti_synsets(word):
        ss_set = list(swn.senti_synsets(word))[0]
    elif 'VB' in tag and swn.senti_synsets(word):
        ss_set = list(swn.senti_synsets(word))[0]
    elif 'JJ' in tag and swn.senti_synsets(word):
         ss_set = list(swn.senti_synsets(word))[0]
    elif 'RB' in tag and swn.senti_synsets(word):
         ss_set = list(swn.senti_synsets(word))[0]
    if ss_set:
        pos=pos+synset.score() #check the positive score and verify
        neg=neg+synset.neg_score()
        obj=obj+synset.obj_score()
        count+=1
final_score=pos-neg
print(aggregate_score)
df['final_score']=final_score
df.to_csv('smallcsvdata2.csv')
norm_finalscore= round((final_score) / count, 2)
print(norm_finalscore)
final_sentiment = 'positive' if norm_finalscore >= 0 else 'negative'
print(final_sentiment)

