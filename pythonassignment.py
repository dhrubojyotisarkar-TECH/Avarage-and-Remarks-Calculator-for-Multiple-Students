allstudent=int(input("Enter the number of students :"))
student=[allstudent]
f=[]
name=0
rollnumber=0
est=[]
total=0
n=1
studentdetails = {
        "Name":name,
        "Roll number":rollnumber,
        "Marks":est,
        "Total marks":total,
        "Percentage":total/n
        }


for x in range(0,allstudent):
    
    #f=dict("studentdetails[x]")

    #student.append(studentdetails)

    student.insert(0,'studentdetails')
    name=input("Enter the student name :")
    rollnumber=input("Enter the student roll number :")
    n=int(input("Enter the number of subject:"))
    est=[]
    for i in range(0, n):
        ele = int(input("Enter the marks one by one:"))
        est.append(ele)
    total=0
    for j in range(0,n):
        total=total+est[j]

    studentdetails = {
        "Name":name,
        "Roll number":rollnumber,
        "Marks":est,
        "Total marks":total,
        "Percentage":total/n
        }
    print(studentdetails)

