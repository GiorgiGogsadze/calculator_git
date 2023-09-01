print("the Best calculator ever!")

x = int(input("x: "))
y = int(input("y: "))

print(f"sum: {x + y}")
print(f"subtract: {x - y}")
print(f"mult: {x * y}")

if y == 0:
  print("can't divide with 0")
else:
  print(f"div: {x / y}")
