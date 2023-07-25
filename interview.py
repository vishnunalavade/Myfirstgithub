def isPalindrome(s):
    return s == s[::-1]
s = "madam"
ans = isPalindrome(s) 
if ans:
    print("Yes")
else:
    print("No")


s = "Vishnu"
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
print(reverse(s))


n = 1234
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
print(rev)


d=[10,20,30,40,50,60,70,80,90,100]
d.sort(reverse=True)
print(d)

v = {"address": "karjat", "mobile": 9011286173,"state":"Maharashtra"}
for i in v:
    print('keys',[i],'val',v[i])
v.update({'key': 101,'values':'student of the year'})
print(v.keys())
print(list(v.values()))    


vishnu_dict = {'vishnu':1, 'arvind':2, 'saurbhu':3, 'Manoj':4, 'Sanket':5, 'sujit':6}
for value in vishnu_dict.values():
    print(value)

vishnu_dict = {'vishnu':1, 'arvind':2, 'saurbhu':3, 'Manoj':4, 'Sanket':5, 'sujit':6}
for keys in vishnu_dict.keys():
    print(keys)    