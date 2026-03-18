student_data={"id1":{"name":"summer","class":"grade 9","subject_intigration":"math"},
              "id2":{"name":"henry","class":"grade 8","subject_intigration":"english"},
              "id3":{"name":"timmy","class":"grade 10","subject_intigration":"phisics"}}
result= {}
seen_keys = []
for student_id,details in student_data.items():
    unique= (details["name"],details["class"],details["subject_intigration"])
    if unique not in seen_keys:
        seen_keys.append(unique)
        result[student_id]  = details
for k,v in result.items():
    print(k,":",v)