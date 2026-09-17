class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sit(self):
    return f"{self.name} is now sitting"

  def roll_over(self):
    return f"{self.name} rolled over!"
