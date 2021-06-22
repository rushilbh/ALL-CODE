class ATM(object):
  """
    blueprint for ATM
  """

  def __init__(pin,card_no):
    self.pin = pin
    self.card_no=card_no

  def start(self):
    print("THIS IS HDFC BANK ")
    input_1=input("Pls enter your card number:-")

  def amount(self):
      input_3=input("enter amount for transaction:-")
      input_2=input("enter your pin:-")
      print("Pin correct")
  def proceed(self):
      print("Transaction complete!")


print(ATM.start('self'))
print(ATM.amount('self'))
print(ATM.proceed('self'))
