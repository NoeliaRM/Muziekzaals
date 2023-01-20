import base64
#data manipulation
from datetime import datetime
from io import StringIO

import nltk
import numpy as np
import pandas as pd
#ML algorithms
#plotting 
import plotly as plotly
from nltk.corpus import stopwords
from pandasql import sqldf
#modelling
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
#preprocessing
from sklearn.model_selection import train_test_split
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from repository.database.review_repo import reviews_repo

from services.reviews.add_data import base_64_to_df



analyser = SentimentIntensityAnalyzer()
blacklist= stopwords.words('english')
review_repository = reviews_repo() #to get the training data from db

def send_to_AI(base64: base64):
    df_stfy_gp = base_64_to_df(base64)

    # clean the df
    date =[]
    time =[]

    for i, row in df_stfy_gp['Time_submitted'].items():
        Time_submitted = datetime.strptime(row, '%Y-%m-%d %H:%M:%S') 
        date.append(Time_submitted.date())
        time.append(Time_submitted.time())
    df_stfy_gp['Date'] = date
    df_stfy_gp['Time'] = time
    df_stfy_gp = df_stfy_gp.drop('Time_submitted', axis=1)
    df_stfy_gp['Reply'] = df_stfy_gp['Reply'].replace(np.NaN,'null')
    #rating
    df_stfy_gp['Classification'] = df_stfy_gp['Rating'].replace({5: 'Positive', 4: 'Positive', 3: 'Negative', 2: 'Negative', 1: 'Negative'})
    #clean text
    df_stfy_gp['Review_sentim']= df_stfy_gp['Review']
    df_stfy_gp['Review_sentim']= df_stfy_gp['Review'].apply(lambda x: ' '.join(x.lower() for x in x.split())) #

    df_stfy_gp['Review_sentim'] = df_stfy_gp['Review_sentim'].str.replace('[^a-z ]*', '')
    #tokenize and blackwords
    df_stfy_gp['Review_sentim']= df_stfy_gp['Review_sentim'].str.split(expand=False) 
    df_stfy_gp['Review_sentim'] = df_stfy_gp['Review_sentim'].apply(RemovefromBlacklist)
    #filtering only nouns and adjetives
    # nltk.download('averaged_perceptron_tagger')
    #df_stfy_gp['Review_sentim'] = df_stfy_gp['Review_sentim'].apply(lambda x: extract_adj_noun(x))
    
    #TODO: I should be able to apply  spell correction here but it takes hours...
    
    #convert back to string
    df_stfy_gp['Review_sentim']= df_stfy_gp['Review_sentim'].apply(lambda x: listToString(x))
       

    #TODO: remove neutral words from positive and negative?

    ##PREDICTIONS:
    
    df_stfy_gp['sentiment']=df_stfy_gp['Review_sentim'].apply(calculate_sentiment)
    df_stfy_gp['sentiment_analyser']=df_stfy_gp['Review_sentim'].apply(calculate_sentiment_analyser)
    
    df_score_sentiment = pd.DataFrame(index = range(0,len(df_stfy_gp)),columns= ['Sentim_score','Sentim_label'])

    for i in range(0,len(df_stfy_gp)): 
        df_score_sentiment['Sentim_score'][i] = df_stfy_gp['sentiment_analyser'][i]['compound']
  
        if (df_stfy_gp['sentiment_analyser'][i]['compound'] <= -0.05):
            df_score_sentiment['Sentim_label'][i] = 'Negative'    
        if (df_stfy_gp['sentiment_analyser'][i]['compound'] >= 0.05):
         df_score_sentiment['Sentim_label'][i] = 'Positive'
        if ((df_stfy_gp['sentiment_analyser'][i]['compound'] >= -0.05) & (df_stfy_gp['sentiment_analyser'][i]['compound'] <= 0.05)):
         df_score_sentiment['Sentim_label'][i] = 'Neutral'
    
    df_stfy_gp['Sentim_score'] = df_score_sentiment['Sentim_score']
    df_stfy_gp['Sentim_label'] = df_score_sentiment['Sentim_label']

    #get data from database for training the model
    matrixCreator = TfidfVectorizer()

    df_train = review_repository.get_all_reviews_from_db()
    matrix_train = matrixCreator.fit_transform(df_train['Sentim_label']) #for clustering text of reviews

    #preprocessing
    matrix_predict = matrixCreator.fit_transform(df_stfy_gp['Sentim_label']) #for clustering text of reviews

    #modelling
    km = KMeans(n_clusters=3)
    km.fit(matrix_train) 
    km.fit_predict(matrix_predict) 
    KMclusters = km.labels_.tolist() # ordered clusters
    MI_reviews_clusters = {'Review': df_stfy_gp['Review_sentim'].tolist(), 'Cluster': KMclusters}
    df_cluster = pd.DataFrame(MI_reviews_clusters, index = [KMclusters])
    df_stfy_gp['Cluster_score'] = KMclusters

    return df_stfy_gp.to_json(orient='records')


#prediction methods
def calculate_sentiment(input):
    return TextBlob(input).sentiment

def calculate_sentiment_analyser(input):    
    return analyser.polarity_scores(input)


#methods    

#conversor to string
def csv_base_64_to_string(base64_string: base64):
    data = base64.b64decode(base64_string)
    return data

#string to df
def base_64_to_df(base64_code: str):
    csv_as_string = csv_base_64_to_string(base64_code).decode()
    string = StringIO(str(csv_as_string))
    csv_as_dataframe = pd.read_csv(string, sep=',').fillna('')
    return csv_as_dataframe


def RemovefromBlacklist(input):
    return [item for item in input if item not in blacklist]

def listToString(input):
    s = " "
    return (s.join(input))

def extract_adj_noun(text):
    tagged_words = nltk.pos_tag(text)
    adj_noun = [word for word, pos in tagged_words if pos in ['JJ', 'NN']]
    return ' '.join(adj_noun)

#sets

def get_difference(t1, t2):
    return list(set(t1).difference(set(t2)))    
    
def get_intersection(t1, t2):
    return list(set(t1).intersection(set(t2)))
    
def get_set(t1):
    return list(set(t1))  