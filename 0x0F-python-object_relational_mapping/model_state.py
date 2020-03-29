#!/usr/bin/python3
"""
state class
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
	"""
	state representation
	"""

id = Column(Integer, primary_key=True)
name = Columns(String(128), nullable=False)
