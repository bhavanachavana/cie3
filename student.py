import  student

def student_details(name, id, usn,course ,academic_year):
    result = (
        f"student Name : {name}\n"
        f"student ID  : {id}\n"
        f"usn  : {usn}\n"
        f"course  : {course}\n"
        f"academic_year :{academic_year}\n"
    )
    return result


if __name__=="__main__":
    name ="bhavana"
    id ="013"
    usn ="01fe24bca015"
    course ="bca"
    academic_year="2025-2027"
    print(student_details(name,id,usn,course,academic_year))
