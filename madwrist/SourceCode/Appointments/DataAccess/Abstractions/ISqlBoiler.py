import os
import psycopg2
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from CrossCutting.Response import Response


class ISqlBoiler():
    def __init__(self, url: str):
        load_dotenv()
        self._url = os.getenv(url)
        self._engine = create_engine(self._url)
        # self._Session = sessionmaker(self._url)
        self._Session = sessionmaker(bind=self._engine)
        self._session = self._Session()
        self.response = Response()

    def add_query(self, query):
        try:
            self._session.add(query)
            self._session.commit()
            self.response.is_successful = True
            self.response.message = 'Successful'
            return self.response
        except:
            self.response.is_successful = False
            self.response.message = 'Insert Fail'
            return self.response
