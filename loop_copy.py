subjects = ['DB','DC','DS']
for i in subjects :
    spoint = 0
    for j in range(3):
        point = int(input(f"คะแนนวิชา {i} ครั้งที่ {j+1}: "))
        spoint+=point
    print(f"คะแนนรวมของวิชา {i} = {spoint}")

  
 
