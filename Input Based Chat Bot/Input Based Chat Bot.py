import time,sys,os

def Textprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.08)
  
def Textinput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.08)
  value = input()  
  return value
 
def clearScreen():
  os.system("clear")

Textprint("Hi my name is Masud \n")

a=Textinput("What's your name?? \n")

Textprint(f"Hello {a} how are you?? \n")