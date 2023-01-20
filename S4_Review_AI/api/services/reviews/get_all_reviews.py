
from repository.database.review_repo import reviews_repo

reviews_repository = reviews_repo()

def get_all_reviews():
    
    df = reviews_repository.get_all_reviews_from_db()
    
    df_json=df.to_json(orient='records')

    return df_json

