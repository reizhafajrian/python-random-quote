import random
def primary():
  print("Keep it logically awesome.")

  f = open("/home/reizha/python-random-quote/quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[13])
  last =13
  rnd=random.randint(0,last)

  print(quotes[rnd])
if __name__== "__main__":
  primary()
