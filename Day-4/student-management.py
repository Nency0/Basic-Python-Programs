


print("Build a simple school which allows for :: 3.1 Adding a new student to a class with a Name & (unique) ID 3.2 Showing total number of students in a class 3.3 Removing the name of a student from a class 3.4 Promoting a student to the next grade")

school={}
def add_student():
    num=int(input("\n Enter number of students do you want to add : "))
    for i in range(1,num+1):
        Student_name=input("\n Enter name of student : ")
        student_id = int(input("\n Enter student id : "))
        class_of_Student = int(input("\n enter grade of student : "))
        for key in school.items():
            if student_id==key:
                print("student with id {} is already exists. ".format(key))
        school[student_id]=[Student_name,class_of_Student]
    print("\n Students data added successfully. ")

def total_number_of_students():
    print("Total number of students in your school is : ",len(school))

def remove_student(id):
    
    for key in school.keys():
        
        if key == id :
            
            school.pop(key)
            break

def promote_student(id):
    for key in school.keys():
        
        if key==id:
            school[key][1]=school[key][1]+1
            break


if __name__ =="__main__":
    while True:
        print("\n Welcome to school managment tool")
        a=int(input("Enter your choice : \n 1. Add Student \n 2. Find Total number of Students \n 3. Remove Students \n 4. Promote Student \n 5. Show All students Data \n "))
        match a :
            case 1:
                add_student()

            case 2:
                total_number_of_students()

            case 3:
                id = int(input("\n Enter student id: "))
                remove_student(id)
            case 4:
                id = int(input("\n Enter student id: "))
                promote_student(id)

            case 5:
                print(school)
        n=int(input("Do you want to continue ? (0-no/1-yes) : "))
        if n == 0:
            break





    


