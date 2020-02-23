# Natural Language Processing on Online Reviews Data - BigView Idea

#### Goal: Simplifying Daily life buying decisions by getting insights from online reviews faster.

Example: You are in a mood to eat Butter Chicken from an Indian Restaurant but that restaurant rating is 4.1. People have given some bad reviews recently on some vegetarian menu about taste. In that moment you only care about butter chicken reviews, Now imagine instead of going through all the reviews you can use this functionality where you can see whether butter chicken is in positive reviews category or negative and what people exactly saying about it. This is what we are trying to achieve through this BigView idea, "Making Decision Faster" for everyone.


### [The Cheesecake Fatory Reviews](https://www.yelp.com/biz/the-cheesecake-factory-charlotte?osq=Restaurants+Cheese+Cake+Factory)


<p align="center">
  <img src="https://github.com/Minsifye/BigView/blob/master/cheesecake-factory-logo.png?raw=true" width="350" title="logo">
</p>


## Positive Reviews WordCloud and Most Frequently used Positive Terms: 
<p align="center">
  <img src="https://github.com/Minsifye/BigView/blob/master/pos_cloud.png?raw=true" width="600" title="logo">
  <img src="https://github.com/Minsifye/BigView/blob/master/plot1.png?raw=true" width="600" title="Frequent Positive Terms">
</p>


## Negative Reviews WordCloud and Most Frequently used Critical Terms: 

<p align="center">
  <img src="https://github.com/Minsifye/BigView/blob/master/neg_cloud.png?raw=true" width="600" title="neg">
  <img src="https://github.com/Minsifye/BigView/blob/master/plot2.png?raw=true" width="600" alt="Frequent Negative Terms">
</p>


## Average Overall Ratings - Timeline :

<p align="center">
  <img src="https://github.com/Minsifye/BigView/blob/master/plot3.png?raw=true" width="600" title="neg">
</p>



### BackStory: 
Shopping online is part of our daily life and looking at online reviews to make a decision to buy that product or not is always overwhemling. That's why we came up with an Idea to bring insights from textual data. Whether you want to read Google Reviews before going to a Restaurant or choosing a product online on Amazon.com, reading reviews either make our mind or change it. But most of the time online ratings can not tell the whole story of "how a product is doing". 
Adding a new functionality called BigView where a user would be able to see insights from reviews and make a decision faster rather than going through hundreds of reviews.
### Solution: 
We are implementing this idea on "Cheesecake Factory" yelp reviews. Number of reviews are 465 and you can see the output of our implementation in python code. 
1. Fetch only cheesecake reviews from huge yelp dataset. Performing data cleaning and transforming data using pandas. 
2. Text Cleaning, Normalization, Tokenization, Stopword removal, Bag of Words etc.
3. Generating Word Clouds on textual reviews, Barplots on Bag of Words and overall timeline of average ratings.

### Challenges : 
1. Getting real reviews data. Picking a sample dataset with enough reviews from huge yelp dataset.
2. Cleaning and transforming text using NLP. 
3. Creating a front-end to bring insights from text.

Technical Points: 
We are using NLP library to bring insights from Textual reviews data. Python as backbone coding language, pandas for data cleaning and transforming. WordCloud library to generate wordclouds. Matplotlib and Seaborn for data visualizations.

Future Work:
Implementing Sentiment Analysis to show "how happy customers are?"

Tips:
This Idea can be used for any website who has reviews/ratings system.



Data: 
Yelp 2018 Dataset from [Kaggle](https://www.kaggle.com/yelp-dataset/yelp-dataset)


