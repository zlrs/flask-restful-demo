# coding: utf-8
"""
world 数据库的 model
"""
from sqlalchemy import CHAR, Column, Enum, Float, ForeignKey, text
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+pymysql://root:admin@localhost/world')
DBSession = sessionmaker(bind=engine)


class Country(Base):
    __tablename__ = 'country'

    Code = Column(CHAR(3), primary_key=True, server_default=text("''"))
    Name = Column(CHAR(52), nullable=False, server_default=text("''"))
    Continent = Column(Enum('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America'), nullable=False, server_default=text("'Asia'"))
    Region = Column(CHAR(26), nullable=False, server_default=text("''"))
    SurfaceArea = Column(Float(10), nullable=False, server_default=text("'0.00'"))
    IndepYear = Column(SMALLINT(6))
    Population = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    LifeExpectancy = Column(Float(3))
    GNP = Column(Float(10))
    GNPOld = Column(Float(10))
    LocalName = Column(CHAR(45), nullable=False, server_default=text("''"))
    GovernmentForm = Column(CHAR(45), nullable=False, server_default=text("''"))
    HeadOfState = Column(CHAR(60))
    Capital = Column(INTEGER(11))
    Code2 = Column(CHAR(2), nullable=False, server_default=text("''"))


class City(Base):
    __tablename__ = 'city'

    ID = Column(INTEGER(11), primary_key=True)
    Name = Column(CHAR(35), nullable=False, server_default=text("''"))
    CountryCode = Column(ForeignKey('country.Code'), nullable=False, index=True, server_default=text("''"))
    District = Column(CHAR(20), nullable=False, server_default=text("''"))
    Population = Column(INTEGER(11), nullable=False, server_default=text("'0'"))

    country = relationship('Country')


class Countrylanguage(Base):
    __tablename__ = 'countrylanguage'

    CountryCode = Column(ForeignKey('country.Code'), primary_key=True, nullable=False, index=True, server_default=text("''"))
    Language = Column(CHAR(30), primary_key=True, nullable=False, server_default=text("''"))
    IsOfficial = Column(Enum('T', 'F'), nullable=False, server_default=text("'F'"))
    Percentage = Column(Float(4), nullable=False, server_default=text("'0.0'"))

    country = relationship('Country')
