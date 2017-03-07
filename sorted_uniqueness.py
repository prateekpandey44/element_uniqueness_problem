#sorting technique for haveng a result of unique set of element

def unique_2(S):
  temp=sorted(S)
  for j in range(1,len(temp)):
    if S[j-1]==S[j]:
      return False
  return True
