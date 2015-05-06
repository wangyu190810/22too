# -*-coding:utf-8-*-
__author__ = 'Administrator'

from sqlalchemy.dialects.postgresql import \
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT, \
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR
from sqlalchemy import create_engine
from sqlalchemy.schema import Table,MetaData
from sqlalchemy import Column,Integer
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

metadata = MetaData()


engine = create_engine("postgresql://postgres:2015@localhost/test"
                )

DBSession = scoped_session(sessionmaker(bind=engine))



class Data(Base):
    __tablename__ = "json_data"
    id = Column(Integer, primary_key=True)
    data = Column(JSONB)

#Base.metadata.create_all(engine)

    @classmethod
    def insert_data(cls, connection, value):
        data = Data(id=value[0], data=value[1])
        connection.add(data)
        connection.commit()

    @classmethod
    def add_data(cls, connection ,value):
        data = connection.query(Data).filter(Data.id == value[0]).scalar()
        if data is None:
            data = Data(id=value[0], data=value[1])
            connection.add(data)
            connection.commit()
        else:
            connection.query(Data).filter(Data.id == value[0]).update(
                {
                    Data.data:dict(data.data,**value[1])
                }
            )
            connection.commit()


    @classmethod
    def get_data(cls,connection,data_id):
        return connection.query(Data).filter(Data.id == data_id).scalar()

value = (123,{"1234":"adsadfff"})

#Data.add_data(DBSession,value)

for row in range(100):
    value = (row,{row:str(row)})
    Data.add_data(DBSession,value)
    data_json = Data.get_data(DBSession,row)
    print data_json.data.get(str(row))
