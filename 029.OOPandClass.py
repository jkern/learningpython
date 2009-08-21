#!/usr/bin/python
"""A gentle introduction to Object Oriented Programming

Joseph Kern"""

# PEP 8 me please.

class robot:
	def __init__(self, mat, legs, weapon):
		self.mat = mat
		self.legs = legs
		self.weapon = weapon
	def statement(self):
		return "I am a robot, I have %i legs, and I am made of %s." % (self.legs, self.mat)
	def weapons(self):
		return self.weapon
	def defense(self): #clean this up.
		if self.mat == "Metal":
			de = 2
		elif self.mat == "Wood":
			de = 1
		else:
			de = 0
		return de

robbie = robot("Metal", 4, 5)
carla = robot("Wood", 2, 4)
