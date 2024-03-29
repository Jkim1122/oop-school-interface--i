from classes.school import School 

school = School('Ridgemont High') 

while True:
    choice = input("""What would you like to do?
    Options:
        1. List All Students
        2. View Individual Student: <student_id>
        3. Add a Student
        4. Remove a Student: <student_id>
        5. Quit
""")
    if choice == '1':
        school.list_students()
    elif choice == '2':
        student_id = input('Enter STUDENT ID:')
        student = school.find_student_by_id(student_id)
        print(str(student))
        # runner.py
    elif choice == '3':
        student_data = {'role':'student'}
        student_data['name']      = input('Enter student name:\n')
        student_data['age']       = input('Enter student age: \n')
        student_data['school_id'] = input('Enter student school id: \n')
        student_data['password']  = input('Enter student password: \n')
        #student_data = {"role:'student', "name":'francisco', "age":'15', "school_id": '123000', "password": 'password'}
        school.add_student(student_data)
    elif choice == '4':
        student_id = input('Enter STUDENT ID:')
        student = school.find_student_by_id(student_id)
        if student:
            school.students.remove(student)
            print("Student DELETED!")
    if choice == '5':
        print("Goodbye!")
        break