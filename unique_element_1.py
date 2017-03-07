def unique_1(S):
  for j in range (len(S)):
    for k in range(j+1),len(S)):
      if S[j]==S[k]:
        return False
  return True   
  #this is again O(n^2) notation as we are looping in a loop for searching other element
