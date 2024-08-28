y = (input())
if y == "*":
  x = int(input()) * int(input())
  print(x)

if y == "/":
  x = int(input()) / int(input())
  print(x)
    
if y == "+":
  x = int(input()) + int(input())
  print(x)

if y == "-":
  x = int(input()) - int(input())
  print(x)

if y == "^":
  x = pow(int(input()), int(input()))
  print(x)

if y == "mogus" or y == "Mogus":
  print("Amogus Sus")





if y == "fibbanacci":
  z = 0
  y = 0
  x = 1
  numberOfTimes = int(input())
  while z < numberOfTimes:
    z = z + 2
    y = y + x 
    print(y)
    x = y + x
    print(x)

  