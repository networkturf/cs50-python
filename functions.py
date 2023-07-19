def main1():
  name = input("What's your name? ")
  hello(name)


def hello(to="world"):    # If the function call doesn't have an agrument, it will print "world" 
  print("Hello", to)

main1()