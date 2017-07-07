#1
{k: v for k,v in [("name", "Elie"), ("job", "Instructor")]}
# {'name': 'Elie', 'job': 'Instructor'}


#2
a = ["CA", "NJ", "RI"]
b = ["California", "New Jersey", "Rhode Island"]
{a[i]:b[i] for i in range(0,3)} # {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

# theirs - using zip
dict(zip(a,b))

#3
