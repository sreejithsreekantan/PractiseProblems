Given a list of grades of a student. Calculate his average score, variance and standard deviation.

# student_grade_book.py

import math

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(grades, average):
    variance = 0
    for grade in grades:
        variance += ((grade-average)**2)
    return variance/len(grades)
    
def grades_std_deviation(variance):
    return math.sqrt(variance)
    
def print_detailed_report(grades):
    for grade in grades:
        print grade
    print grades_sum(grades)
    average = grades_average(grades)
    print average
    variance = grades_variance(grades, average)
    print variance
    print  grades_std_deviation( variance )
    
print_detailed_report(grades)
