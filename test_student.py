from student import  student_details

def test_student_details():
    expected_output = (
        "student Name:  bhavana\n"
        "student ID:  013\n"
        "usn: 01fe24bc015"
        "course:  bca\n"
        "academic_year:2025-2027"
    )
    actual_output = student_details("bhavana", "013", "01fe24bca015", "bca","2025-2027")
    assert actual_output == expected_output

test_student_details()
