def lgrades(m):
    if m>=70:
        return "A+"
    elif m>=65:
        return "A"
    elif m>=60:
        return "B"
    elif m>=55:
        return "C"
    elif m>=50:
        return "D"
    elif m>=45:
        return "E"
    elif m<40:
        return "F"

def grades(m):
    if m>=90:
        return "A+"
    elif m>=80:
        return "A"
    elif m>=70:
        return "B"
    elif m>=60:
        return "C"
    elif m>=50:
        return "D"
    elif m>=40:
        return "E"
    elif m<40:
        return "F"

print("Enter Marks of the subjects: ")
sub1=int(input("Enter Python Marks: "))
sub2=int(input("Enter DLD Marks: "))
sub3=int(input("Enter Control system Marks:  "))
lab1=int(input("Enter marks of Python Lab: "))
lab2=int(input("Enter marks of DLD lab: "))
print("Grades")
print(f"PYTHON      {grades(sub1)}")
print(f"DLD         {grades(sub2)}")
print(f"CS          {grades(sub3)}")
print(f"PYTHON LAB  {lgrades(lab1)}")
print(f"DLD LAB     {lgrades(lab2)}")
if (grades(sub1) == "F" or grades(sub2) == "F" or grades(sub3) == "F" or lgrades(lab1) == "F" or lgrades(lab2) == "F"):
    print("\n      Fail")
else:
    print("\n      Pass")
    sgpa_points = {'A+': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 0}
    total_points = sgpa_points[grades(sub1)] + sgpa_points[grades(sub2)] + sgpa_points[grades(sub3)] + sgpa_points[
        lgrades(lab1)] + sgpa_points[lgrades(lab2)]
    sgpa = total_points / 5
    print(f"The SGPA points are {sgpa}")