p=input("Enter Password:")
if len(p)>=8:
    print("Length is good")
else:
    print("Password must contain atleast 8 characters")
contains_digit=False
contains_special=False
contains_upper=False
contains_lower=False
special="!@#$%^&*"
for k in p:
    if k in special:
        contains_special=True
    if k.isdigit():
        contains_digit=True
    if k.isupper():
        contains_upper=True
    if k.islower():
        contains_lower=True
c=0
if not contains_special:
    print("Must contain a special character")
if not contains_digit:
    print("Must contain a digit")
if not contains_upper:
    print("Must contain uppercase alphabet")
if not contains_lower:
    print("Must contain lowercase alphabet")
if contains_special:
    c=c+1 
if contains_digit:
    c=c+1 
if contains_upper:
    c=c+1 
if contains_lower:
    c=c+1
if len(p)>=8:
    c=c+1 
if c<=2:
    print("Password Strength:Weak")
elif c>=3 and c<=4:
    print("Password Strength:Medium")
else:
    print("Password Strength:Strong")
else:
    print("Password Strength:Strong")

