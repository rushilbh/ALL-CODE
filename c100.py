class Car(object):
  """
    blueprint for car
  """

  def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print("Hello the gear is changed ")

  def stop(self):
    print("speed is crossing limit")

  def accelarate(self):
    print("accelarating...")
    "accelarator functionality here"

  def change_gear(self, gear_type):
    print("gear changed")
    " gear related functionality here"


audi = Car("A6", "red", "audi", 80)

print(audi.start())
print(audi.stop())
print(audi.accelarate())
print(audi.change_gear())
