from utils.config import database_name, database_password, database_user, database_host, database_port
import mysql.connector
from fastapi import HTTPException, status
from sqlalchemy import create_engine
from urllib.parse import quote

import pandas as pd
import pymysql

def get_connection():
    try:
        #delete and insert
        mysql_db = mysql.connector.connect(host=database_host, user=database_user, passwd=database_password, database=database_name, port=database_port)

        return mysql_db, mysql_db.cursor() # get and select and 
    except Exception as e:
        print(e)
        #returns an exception
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="could not connect to database!")

def close_database_connection(mysql_db, cursor):
    mysql_db.close()
    cursor.close()


def db_conn():

    sqlEngine = create_engine(f"mysql+pymysql://noelia:{database_password}@db-mysql-s4-review-ai-do-user-13304489-0.b.db.ondigitalocean.com:25060/S4_Review_AI")

    dbConnection = sqlEngine.connect()

    return dbConnection
