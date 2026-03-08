p=input("Enter Password:")
if len(p)>=8:
    print("Length is good")
else:
    print("Password must contain atleast 8 characters")
contains_digit=False
contains_special=False
contains_upper=False
special="!@#$%^&*"
for k in p:
    if k in special:
        contains_special=True
    if k.isdigit():
        contains_digit=True
    if k.isupper():
        contains_upper=True
c=0
if contains_special:
    print("Contains special character")
else:
    print("Must contain a special character")
if contains_digit:
    print("Contains digit")
else:
    print("Must contain a digit")
if contains_upper:
    print("Contains uppercase")
else:
    print("Must contain uppercase alphabet")
if contains_special:
    c=c+1 
if contains_digit:
    c=c+1 
if contains_upper:
    c=c+1 
if len(p)>=8:
    c=c+1 
if c<=1:
    print("Password Strength:Weak")
elif c>=2 and c<=3:
    print("Password Strength:Medium")
else:
    print("Password Strength:Strong")