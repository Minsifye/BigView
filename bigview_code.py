#!/bin/bash

# Author : This code is written by Monika Bagyal on Pearl Hack at UNC Chapel Hill Feb 22, 2020
# Usage : This code creates wordcloud and visualizations using pandas and seaborn


import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk
import numpy as np
from wordcloud import WordCloud


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

from nltk.stem.wordnet import WordNetLemmatizer


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)

def show_wordcloud(data, title, f_name):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=50,
        max_font_size=40, 
        scale=4,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.savefig(f_name, bbox_inches = 'tight');
    #plt.show()
    plt.close(fig)


#Data Cleaning

def clean_reviewtext(mytext):
    review_text = str(list(mytext)).lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", review_text) 
    return text


# Create Cloud
def create_cloud(df, title, f_name):
    text = clean_reviewtext(df['text'])
    show_wordcloud(text, title, f_name)
    #plt.savefig('a_cloud.png', bbox_inches = 'tight');




# Loading Cheesecake factory data file
df_ccf = pd.read_csv('CCF_Reviews.csv')

df_positive = df_ccf[df_ccf['stars'] >= 3]
df_negative = df_ccf[df_ccf['stars'] < 3]
print("Positive review counts:",df_positive.shape[0])
print("Negative review counts:",df_negative.shape[0])


create_cloud(df_positive, 'Positive Reviews WordCloud', 'pos_cloud.png')
create_cloud(df_negative,'Negative Reviews WordCloud', 'neg_cloud.png')

negative_reviews = df_ccf[df_ccf['stars'].isin([1,3])]
positive_reviews = df_ccf[df_ccf['stars'].isin([4,5])]



negative_vectorizer = TfidfVectorizer(stop_words=STOPWORDS, ngram_range=(3, 3), 
                       max_df=1.0, min_df=1, max_features=3000,use_idf=False)
negative_vectorized = negative_vectorizer.fit_transform(negative_reviews.text)

positive_vectorizer = TfidfVectorizer(stop_words=STOPWORDS, ngram_range=(3, 3), 
                       max_df=1.0, min_df=1, max_features=3000,use_idf=False)
positive_vectorized = positive_vectorizer.fit_transform(positive_reviews.text)

print("negative_vectorized", negative_vectorized.shape)
print("positive_vectorized", positive_vectorized.shape)

#Most Common Comments from Positive Reviews

positive_vocab = positive_vectorizer.get_feature_names()
positive_vectorized_df = pd.DataFrame(positive_vectorized.todense(),columns=[positive_vocab]).sum()
positive_term_f = positive_vectorized_df.sort_values(ascending=False)
print("positive_term_frequency", positive_term_f.head(15))

#Most Common Comments from Negative Reviews

negative_vocab = negative_vectorizer.get_feature_names()
negative_vectorized_df = pd.DataFrame(negative_vectorized.todense(),columns=[negative_vocab]).sum()
negative_term_f = negative_vectorized_df.sort_values(ascending=False)
print("negative_term_frequency", negative_term_f.head(15))



#Create Visualizations

df_pos = pd.DataFrame(positive_term_f)
df_neg = pd.DataFrame(negative_term_f)

#df_pos.head(10).plot(kind='bar', title='Positive Reviews', );
#df_neg.head(10).plot(kind='bar', title='Negative Reviews', );

#fig = plt.figure(figsize=(9, 11));




#df_neg.head(7).plot(kind='barh', title='Negative Reviews', figsize=(6,4))
#plt.savefig('plot2.png', bbox_inches = 'tight');
#plt.close(fig)

df_pos_top = df_pos.reset_index().head(7)
df_pos_top.columns = ['content', 'value']
df_pos_top.plot(x='content', kind='barh', title='Positive Reviews', figsize=(6,4), color='green')
plt.xlabel('Frequency')
plt.ylabel('Most Frequent Context')
plt.savefig('plot1.png', bbox_inches = 'tight');
#plt.close(fig)



df_neg_top = df_neg.reset_index().head(7)
df_neg_top.columns = ['content', 'value']
df_neg_top.plot(x='content', kind='barh', title='Negative Reviews', figsize=(6,4), color='red')
plt.xlabel('Frequency')
plt.ylabel('Most Frequent Context')
plt.savefig('plot2.png', bbox_inches = 'tight');



df_ccf['year'] = df_ccf['date'].apply(lambda x: int(str(x).strip().split('-')[0]))

df_timeline = df_ccf[['stars', 'year']].groupby('year').mean()
df_timeline.reset_index(inplace = True)

fig = plt.figure(figsize=(11, 6));
sns.lineplot(x='year', y='stars',data=df_timeline, color='purple');
plt.title('Average Ratings out of 5')
plt.xlabel('Years')
plt.ylabel('Average Rating')
plt.savefig('plot3.png', bbox_inches='tight');
#plt.close(fig);

print("Script Completed")











