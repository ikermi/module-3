# Starter code
class Garage:
  def __init__(self, size):
    self.size = size
    self.cars = ["Ram", "Model 3"]

  def open_door(self):
    return "The door opens"
    
home = Garage(2)
# End of starter code
home.cars = []
# Setter goes here

get_cars = home.cars