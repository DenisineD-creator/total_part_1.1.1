grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steven','Khendrik','Aaron'}
student_sort = sorted(students)
print(student_sort)
grades_m = sum(grades[0])/len(grades[0]),
grades_m1 = sum(grades[1])/len(grades[1]),
grades_m2 = sum(grades[2])/len(grades[2]),
grades_m3 = sum(grades[3])/len(grades[3]),
grades_m4 = sum(grades[4])/len(grades[4])
print(grades_m,grades_m1,grades_m2,grades_m3,grades_m4)
grades_m = []
for num in grades:
    s = sum(num)/len(num)
    grades_m.append(s)
#s = sum(num)/len(num)
#student_sort = sorted(students)
#print(student_sort)
dict1 = (zip(student_sort,grades_m))
print(dict1)