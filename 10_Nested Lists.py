'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

records=[['chi',20.0],['beta',50.0],['alpha',50.0]]
The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

    2 <=N<=5
    There will always be one or more students having the second lowest grade.
'''


if __name__=='__main__':
   #marks_list contains a list of marks
   #score_card contains a list of (name, marks) 
    marks_list=[]
    score_card=[]
    return_name_list=[]
    for i in range(int(input())):
        #Input for Name
        name=input()
        #Input for Marks
        marks=float(input())
        marks_list.append(marks)
        score_card.append([name, marks])
    
    #Re-assigning the marks_list with a unique list of sorted marks
    marks_list=sorted(list(set(marks_list)))
    second_lowest=marks_list[1]
    #return_name_list contains a list of Students with Second Lowest Grades
    for name, marks in score_card:
        if second_lowest==marks:
            return_name_list.append(name) 
    #Print the name of Students in Alphabetical order
    for names in sorted(return_name_list):
        print(names)