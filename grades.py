studentFile = open("grades.txt", "r") 

# CREATE class Student with name, courseworkMark, prelimMark, gradePercent and grade
class Student: 
  name = "" 
  courseworkMark = int
  prelimMark = int 
  gradePercent = int
  grade = ""
  
studentList = [] 

# LOOP through each line in the studentFile 
for line in studentFile: 
  strippedLine = line.strip() 
  lineEl = strippedLine.split() 
  name = lineEl[0] 
  courseworkMark = lineEl[1] 
  prelimMark = lineEl[2]
  gradePercent = ((int(courseworkMark) + int(prelimMark)) *100)/150

  if(gradePercent>70):
    grade = "A"
  elif(gradePercent>60):
    grade = "B"
  elif(gradePercent>50):
    grade = "C"
  elif(gradePercent>45):
    grade = "D"
  else:
    grade = 0
    
    # CREATE newStudent instance with name, courseworkMark, prelimMark, gradePercent and grade
  newStudent = Student() 
  newStudent.name = name 
  newStudent.courseworkMark = courseworkMark
  newStudent.prelimMark = prelimMark
  newStudent.gradePercent = gradePercent
  newStudent.grade = grade

  studentList.append(newStudent) 
  
amountA = 0
# LOOP through studentList
for currStudent in studentList:
  if(currStudent.grade  == "A"):
    amountA += 1   #adding each student with A grade to amount of A students
    
print (amountA, " A passes are in the class")
  
maxStudent = studentList[0] 
# LOOP through studentList
for currStudent in studentList[1:]: 
  if(currStudent.gradePercent > maxStudent.gradePercent): 
    maxStudent = currStudent 
  
print (maxStudent.name, " has the best percentage in the class")


