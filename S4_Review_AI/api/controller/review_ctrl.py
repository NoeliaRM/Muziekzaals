from fastapi import APIRouter, status
from services.send_to_AI import send_to_AI
from services.reviews.get_all_reviews import get_all_reviews
from services.reviews.add_data import add_csv_to_db_use_case
from dto.data import add_csv_to_db_request_dto

router = APIRouter(prefix="/review", tags=["review"])
#to add tada to db
@router.post("/data", status_code=status.HTTP_200_OK)
def post_data(add_csv_to_database_request_dto: add_csv_to_db_request_dto):
    return add_csv_to_db_use_case(add_csv_to_database_request_dto.data)

#download data from db
@router.get("/download", status_code=status.HTTP_200_OK)
def get_data():
    return get_all_reviews()

#sends the data that i got from db to the AI
@router.post("/predict", status_code=status.HTTP_200_OK)
def post_data(add_csv_to_database_request_dto: add_csv_to_db_request_dto):
    return send_to_AI(add_csv_to_database_request_dto.data)
