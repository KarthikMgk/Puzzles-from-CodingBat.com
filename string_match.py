QN: 

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

------------------------------------------------------------------------------------------------------------------------------------------
def string_match(a, b):
  count = 0
  string_a = list(a)
  string_b = list(b)
  
  try:
    for i in range(len(string_a)):
      if (string_a[i] == string_b[i]) & (string_a[i+1] == string_b[i+1]):
        count +=1
  except:
    pass
  
  return count
------------------------------------------------------------------------------------------------------------------------------------------
def string_match(a, b):
  count = 0
  string_a = list(a)
  string_b = list(b)
  
  try:
    for i in range(len(string_a)):
      val_a1 = string_a[i]
      val_a2 = string_a[i+1]
      val_b1 = string_b[i]
      val_b2 = string_b[i+1]
      
      if (val_a1 == val_b1) & (val_a2 == val_b2):
        count +=1
  
  except:
    pass
  
  return count
  
    
