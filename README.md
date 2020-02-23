# Natural Language Processing on Online Reviews Data - BigView Idea

#### Goal: Simplifying Daily life decisions by getting insights from online reviews faster.


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



BackStory: Shopping online is part of our daily life and looking at online reviews to make a decision to buy that product or not is always overwhemling. That's why we came up with an Idea to bring insights from textual data. Whether you want to read Google Reviews before going to a Restaurant or choosing a product online on Amazon.com, reading reviews either make our mind or change it. But most of the time online ratings can not tell the whole story of "how a product is doing". 


Technical Points: We are using NLP library to bring insights from Textual reviews data. Python as backbone coding language, pandas for data cleaning and transforming. WordCloud library to generate wordclouds. Matplotlib and Seaborn for data visualizations.

Solution: We are implementing this idea on "Cheesecake Factory" yelp reviews. Number of reviews are 465 and you can see the output of our implementation in python code. 
1. Fetch only cheesecake reviews from huge yelp dataset. Performing data cleaning and transforming data using pandas. 
2. Text Cleaning, Normalization, Tokenization, Stopword removal, Bag of Words etc.
3. Generating Word Clouds on textual reviews, Barplots on Bag of Words and overall timeline of average ratings.

Data: Yelp 2018 Dataset from [Kaggle](https://www.kaggle.com/yelp-dataset/yelp-dataset)


