import statistics as s

admins = {'Python':'Pass123'}
students = {'Jeff':[78,76,93],'Alex':[92,76,88],'Sam':[66,77,88]}

def enterGrades():
            sname = input('Student Name: ')
            

            if sname in students:
                print('Adding Grade...')
                grade = input('Grade: ')
                students[sname].append(int(grade))
            else:
                print('Student does not exist')

            print(students)

def removestu():
    nameremove = input('Enter the name of the student you want to remove:  ')
    if nameremove in students:
        print('Removing Student:')
        del students[nameremove]
    else:
        print('Student does not exist')

    print(students)

def stuavg():
    for eachStudent in students:
        grades = students[eachStudent]
        avgGrade = s.mean(grades)
        print(eachStudent,'has an average grade of: ',avgGrade)
    
            
def main():
    
    print('''
    Welcome to Grade Central

     
    [1] - Enter Grade
    [2] - Remove Student
    [3] - Student Average Grade
    [4] - Exit

    ''')

    options = input('What would you like to do today? (Enter a number) ')

    if options == '1':
        enterGrades()
    elif options == '2':
        removestu()
    elif options == '3':
        stuavg()
    elif options == '4':
        Exit()
    else:
        print('Not a valid choice! please try again')

login = input('Uname:  ')
pwd = input('Password: ')

if login in admins:
    if admins[login] == pwd:
        print('Welcome',login)
        while True:
            main()
    else:
        print('Invalid Password, will detonate in 5 seconds!')
else:
    print('Inavlid Usename')

#Just for Git testing
