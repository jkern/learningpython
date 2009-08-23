#!/usr/bin/python
"""A gentle introduction to Object Oriented Programming

Joseph Kern"""

# PEP 8 me please.

class citation:
	def __init__(self, author, year, title, publisher, city):
		self.author = author
		self.year = year
		self.title = title
		self.publisher = publisher
		self.city = city
	def book(self):
		return self.author,self.year,self.title,self.publisher,self.city


