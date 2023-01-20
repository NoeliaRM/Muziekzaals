from datetime import datetime, timedelta
from fastapi import HTTPException, status
import pandas as pd
from repository.database.db_conn import get_connection, close_database_connection, db_conn


class reviews_repo:
    #def _init_(self):
        #self.get_all_reviews_from_db_query = "SELECT * FROM spotify_google_play_reviews"
        
    #get data from database
    def get_all_reviews_from_db(self):
        mysql_db, cursor = get_connection()

        try:
            cursor.execute("SELECT Review, Rating, Total_thumbsup, Reply, Date, Time, Classification, Review_sentim, sentiment_analyser, Sentim_score, Sentim_label FROM spotify_google_play_reviews")
            df = pd.DataFrame(cursor.fetchall(), columns=['Review', 'Rating', 'Total_thumbsup', 'Reply', 'Date', 'Time', 'Classification', 'Review_sentim', 'sentiment_analyser', 'Sentim_score', 'Sentim_label'])

            return df
        except Exception as e:
            print(e)
        finally:
            close_database_connection(mysql_db, cursor)

    #adds data to database
    def add_data(self, df: pd.DataFrame):
        mysql_db, cursor = get_connection()
        db_con = db_conn()

        try:
            res = df.to_sql('spotify_google_play_reviews', db_con, if_exists='append', index=False)

            return res
        except Exception as e:
            print(e)
        finally:
            close_database_connection(mysql_db, cursor)

