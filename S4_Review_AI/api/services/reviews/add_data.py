from io import StringIO
import pandas as pd
import base64
from textblob import TextBlob
from repository.database.review_repo import reviews_repo

#data manipulation
from datetime import datetime
import pandas as pd 
import numpy as np
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk


analyser = SentimentIntensityAnalyzer()
review_repository = reviews_repo()
blacklist= stopwords.words('english')

def add_csv_to_db_use_case(base64: base64):
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
    # df_stfy_gp['Review_topic']= df_stfy_gp['Review'].apply(lambda x: ' '.join(x.lower() for x in x.split())) #

    # df_stfy_gp['Review_topic'] = df_stfy_gp['Review_topic'].str.replace('[^a-z ]*', '')

    # #tokenize and blackwords
    # df_stfy_gp['Review_topic']= df_stfy_gp['Review_topic'].str.split(expand=False) 
    # df_stfy_gp['Review_topic'] = df_stfy_gp['Review_topic'].apply(RemovefromBlacklist)

    # #filtering only nouns and adjetives
    # df_stfy_gp['Review_topic'] = df_stfy_gp['Review_topic'].apply(lambda x: extract_adj_noun(x))
    
    # #TODO: I should be able to apply  spell correction here but it takes hours...
    
    # #convert back to string
    # df_stfy_gp['Review_topic']= df_stfy_gp['Review_topic'].apply(lambda x: listToString(x))
        

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
    df_stfy_gp['sentiment_analyser'] = df_stfy_gp['sentiment_analyser'].apply(lambda x : str(x))

    df_stfy_gp = df_stfy_gp.drop('sentiment', axis=1)

    # get all data already in database
    df_in_repo = review_repository.get_all_reviews_from_db()

    # remove duplicates
    df_stfy_gp= pd.concat([df_stfy_gp,df_in_repo])
    df_stfy_gp =df_stfy_gp.drop_duplicates()

    # save remaning data in df
    review_repository.add_data(df_stfy_gp)



    return True
    


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

#prediction methods
def calculate_sentiment(input):
    return TextBlob(input).sentiment

def calculate_sentiment_analyser(input):    
    return analyser.polarity_scores(input)