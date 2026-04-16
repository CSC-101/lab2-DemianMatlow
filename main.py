# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name: str) -> str:
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




def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # first=false, second=true
    if test:                            # its preventing it from providing a value that doesm't exist
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # first=none
second = checked_access([1, 0, 1], 2)    # second=1
print(first,second)


def length_sum(L: list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])  # first is being evaluated
   elif len(L) > 1: # 4+2+3 are being added
      result = len(L[0]) + len(L[1])  # third is being evaluated
   elif len(L) > 0:  # 7+4 are being added
      result = len(L[0])  # second is being evaluated
   else:  # 11 is being added
      result = 0
   return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first, second, third)


def surprising(L: list[str], other: str) -> list[str]:
   L.append(other.upper())
   return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# They are valued as strings in a list
# ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
# the same label for a function described two different things
print(first,second)