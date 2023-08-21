# Your code goes here:
def render_person(name, birthdate, eye_color, age, sex):
    return name +" is a "+ str(age) +" years old " + sex +" born in " + birthdate + " with "+eye_color +" eyes"

#def render_person(param1, param2, param3, param4, param5):
    #return param1 + " is a " + param4 + " years old " + param5 + " born in " + param2 + " whit " + param3 + " eyes"
# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))