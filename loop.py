subjects = ['DB','DC','DS']
scredit = 0
spoint = 0
for i in subjects :
    credit = float(input(f"หน่วยกิตของ {i} : "))
    grade = float(input(f"ได้เกรด {i} : "))
    point=grade*credit
    scredit+=credit
    spoint+=point
GPA = spoint/scredit 
print(f"GPA = {GPA}")

  
 
    
