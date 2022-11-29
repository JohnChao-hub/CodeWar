## Reverse word
a = ("abcde")
def reverse_words(str):
  strList = []
  for word in str.split(' '):
      strList.append(word[::-1])
  return ' '.join(strList)

reverse_words(a)

# second sol
def solution(str):
  return str[::-1]
solution('world')


print('test for untracked')