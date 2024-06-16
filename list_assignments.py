# Sort the grades in descending order and display the sorted list
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93] 
sorted_grades = sorted(grades)
print("Printing Sorted Grades in ascending order now: ")
print(sorted_grades)
print()
print("Printing Sorted Grades in descending order now: ")
sorted_grades.reverse()
print(sorted_grades)

#Calculate the average grade from the list above and display it
# (reminder: The average is calculated by dividing the sum of all grades 
# by the length of the grades list).
print("Now here's the total: ")
sum_grades = sum(grades)
print(sum_grades)
print()
print("And the average is:  ")
average_grade = sum_grades // len(grades) 
print(average_grade)

# Extract the temperatures for the second week (7 days) of the month.
# Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])

# Extract all the temperatures above 100 
# (reminder: when slicing to the end of a list you don't need a stop index).

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print()
print("Here are the temperatures we observed in Villanville:  ")
print(temperatures)
print()

sorted_temp = sorted(temperatures)
print("There are", len(temperatures), "temperatures in the list, but only the following  are above 100 degrees:   ")
print(temperatures[24:])

# extract temperatures from the 5th to the 10th.
print()
print("Also, here are the temperatures we observed from the 5th to the 10th:   ")
print(temperatures[5:11])
