'''
s1,s2 = input("enter two string:").split()
for i in s1:
    for j in s2:
      if i==j:
       print("palindrome")
      else:
       print(" not a palindrome")
'''


s1,s2 = input("enter two string:").split()
if s1==s2[::-1]:
     print("palindrome")
else:
    print(" not a palindrome")

