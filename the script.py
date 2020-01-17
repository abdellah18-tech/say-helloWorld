# Let's edit the script
def sayHello(people_name):
  print("hello " + people_name)
  print("How are you doing ? ")
  answer = str(input(">>> "))
  if answer == "I'm fine" or answer == "Fine" or answer == "Good":
    print("So you have a nice day!")
  elif answer == "I am not good":
    print("Oh come on make a smile !")
  else:
    pass
