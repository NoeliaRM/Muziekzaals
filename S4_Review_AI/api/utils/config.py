import os
from dotenv import load_dotenv

load_dotenv()
email_address: str = os.getenv('email_address')
email_password: str = os.getenv('email_password')

database_name: str = os.getenv('database_name')
database_password: str = os.getenv('database_password')
database_user: str = os.getenv('database_user')
database_host: str = os.getenv('database_host')
database_port: str = os.getenv('database_port')
