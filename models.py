# Author: Cameron Brown

import os, sys
import enum

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy import Enum
from sqlalchemy import PickleType
from sqlalchemy import Sequence

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer(), 
        Sequence('article_aid_seq', start=10000, increment=1), primary_key=True)
    company_name = Column(String(256))
    apprenticeships = relationship("ApprenticeshipProgramme")


class ApprenticeshipProgramme(Base):
    __tablename__ = 'apprenticeshipprogramme'
    id = Column(Integer(), 
        Sequence('article_aid_seq', start=10000, increment=1), primary_key=True)
    title = Column(String(256))
    description = Column(String(256))
    location = Column(String(256))
    role = Column(String(256))
    company = Column(Integer(), ForeignKey('company.id'))
    buddies = relationship("Buddy")


class Buddy(Base):
    __tablename__ = 'buddy'
    id = Column(Integer(), 
        Sequence('article_aid_seq', start=10000, increment=1), primary_key=True)
    name = Column(String(256))
    description = Column(String(256))
    photo_url = Column(String(256))
    apprenticeship = Column(Integer(), ForeignKey('apprenticeshipprogramme.id'))
