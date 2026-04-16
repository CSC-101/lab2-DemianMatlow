# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("dmatlow@calpoly.edu")
print(message)


def smallest(n: float, m: float) -> float:
   if n < m:
      return n  # It is not evaluated for either
   else:
      return m


first = smallest(3, 2)  # First=2
second = smallest(2, 2)  # Second=2. Not reasonable because neither are smaller, n and m are equal.
print(first,second)


def function2(a: int, b: int, c: int) -> int:
   if a > b and a > c:
      return a - b  # When a>b and a>c
   elif b > c:
      return b + c  # When a<=b or a<=c, and b>c
   else:
      return 2 * c  # When a<=b or a<=c, and b<=c


answer1 = function2(3, 2, 1)  # answer1=1
answer2 = function2(2, 3, 1)  # answer2=4
answer3 = function2(2, 1, 3)  # answer3=6
print(answer1,answer2,answer3)