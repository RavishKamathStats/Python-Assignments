###########################################
# EECS1015 - Final exam (utilities.py)
# Name: Ravish Kamath
# Student ID: 213893664
# email:  ravish96@my.yorku.ca
# Section B
###########################################

from random import randint

# variables needed for task 3
students = ['Juhong', 'Sasha', 'Solar', 'Ali', 'Amy', 'Gopi', 'Anton', 'Hakki', 'Mario', 'Jason', 'Ted', 'Vladen', 'Jean-Yves',
            'Artyom', 'Weng-Fai', 'Niko', 'Eli', 'Pavel', 'Yunjo', 'Kwabena', 'Kyros', 'Hoang', 'Roland', 'Shayan', 'Anna',
            'Sophie', 'Marid', 'Anne-Marie', 'Ursula', 'Rang', 'Chris', 'Javier', 'Roman', 'Carlo', 'Mahsa', 'Matt', 'Ajay',
            'Wen', 'Abisai', 'Yasu', 'Alexi', 'Leonid', 'Moshe', 'Yuki', 'Calista', 'Mahmoud', 'Rutha']




studentsInfo = {
  'Year 1': [42, 24, 12, 37, 35, 23, 32, 5, 34, 19],
  'Year 2': [1, 28, 36, 46, 30, 15, 6, 33, 13, 7, 18, 44],
  'Year 3': [26, 11, 21, 3, 2, 14, 31, 27],
  'Year 4': [25, 4, 20, 0, 16, 17, 40, 39, 29, 22, 41, 9, 8, 10, 38, 43, 45],
  'CS': [24, 1, 33, 12, 2, 30, 23, 34, 3, 45, 6, 22, 39, 11, 14, 28, 15, 26, 21, 7],
  'DM': [44, 18, 16, 40, 29, 13, 46], 'BZ': [10, 5, 9, 31, 41, 20, 8, 25, 17, 42, 35, 43, 38, 0],
  'SE': [4, 19, 27, 32, 36, 37],
  'On Campus': [24, 13, 6, 3, 22, 4, 23, 12, 15, 7, 38, 19, 42, 14, 34, 27, 11, 21, 26, 46, 39, 10, 33, 40, 43, 35, 8, 45],
  'Off Campus': [30, 1, 37, 36, 41, 16, 9, 25, 29, 17, 0, 18, 31, 44, 5, 32, 2, 20, 28]
  }

# class with class variables needed for task 4
class SeaLife:
  category = ["fish1", "fish2", "jelly", "crab"]
  draw = {"fish1":["><>", "<><"],"fish2":[">()", "()<"], "jelly":["~>)", "(<~"], "crab":["^_^", "^_^"]}
  speed_range = {"fish1":(5,10), "fish2":(1,10), "jelly":(1,5), "crab":(10,20)}

  def __init__(self, direction, pos):
    assert direction == 0 or direction == 1, "direction must be 0 or 1"
    assert pos > 0 and pos < 39, "pos must be between 1 and 38"
    self. pos = pos
    self.direction = direction
    self.cat = SeaLife.category[randint(0,3)]
    for items in SeaLife.category:
      if items == "fish1":
        self.speed = randint(5,10)/10
      elif items == "fish2":
        self.speed = randint(1,10)/10
      elif items == "jelly":
        self.speed = randint(1,5)/10
      elif items == "crab":
        self.speed = randint(10,20)/10

  def move(self):
    if self.direction == 0:
      self.pos = self.pos + self.speed
    else:
      self.pos = self.pos - self.speed
    if self.pos > 40:
      self.direction = 1
    elif self.pos < 1:
      self.direction = 0
    else:
      self.direction = self.direction

  def getStr(self):
    pos = int(self.pos)
    return " " * pos + SeaLife.draw[self.cat][self.direction] + " " * (42 - pos) + self.cat








