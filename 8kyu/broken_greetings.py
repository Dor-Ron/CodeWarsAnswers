class Person:
  def __init__(self, name):
    self.name = name

  def greet(self, other_name):
    return "Hi {0}, my name is {1}".format(other_name, self.name) #need to add self, since it is an attribute of the object class instance
