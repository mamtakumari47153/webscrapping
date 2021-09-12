text1 = {1: "geeks", 2: "for"}
text2 = text1
  
# Using clear makes both text1 and text2
# empty.
text2.clear()
  
print('After removing items using clear()')
print('text1 =', text1)
print('text2 =', text2)
  
text1 = {1: "one", 2: "two"}
text2 = text1
  
# This makes only text1 empty.
text1 = {}
  
print('After removing items by assigning {}')
print('text1 =', text1)
print('text2 =', text2)