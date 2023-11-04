# importing mysql connector modules
import mysql.connector

# creating a connection object 
mydb = mysql.connector.connect(host='localhost', user='root',password='1234')

# to print connection object
#print(mydb)

# creating an instance of cursor class, which we will use to execute the 'SQL statement in Python'
mycursor = mydb.cursor()

# execute() is used to compile a SQL statement. We are executing " USE database_name " statement statement
mycursor.execute("USE assignment2")

# to show all existing databases
#def show_database():

#    mycursor = mydb.cursor()
#    mycursor.execute("SHOW DATABASES")
#    for x in mycursor:
#        print(x)

# to create new databases        
#def create_database():

#    mycursor = mydb.cursor()
#    name=input("Enter the database name : \n")
#    mycursor.execute("CREATE DATABASE " +name)
#    for x in mycursor:
#        print(x)
    
# to list all tables present in database
def show_tables():
   
    mycursor.execute("SHOW TABLES FROM assignment2")
    print("Existing tables from assignment2 Database are :  \n")
    t=()
    print("----TABLE NAME----")
    for y in mycursor:
        t=t+y
    for items in t:
        print(items.capitalize())

# this function helps user to select a table name from given database and list its content
def display_tables():
    
    print("Please enter the required table name for above list to dispaly its content\n")
    show_tables()
    table=input("Enter the table name\n")
    #print(type(table))
    my_cursor = mydb.cursor()
    my_cursor.execute("Select * from %s" %table)
    # to display field name
    columns = [column[0] for column in my_cursor.description]
    t=(tuple(columns))
    print(t)
    myresult = my_cursor.fetchall()
    l=[]
    for y in myresult:
        #print(y)
        l.append(list(map(str,list(y))))
    for z in l :
        print(z)
    print("\n")
    main()

# this function helps us to insert the records
# Now this function completely work for instructor table
def insert_records():

    print("Please enter the table name for new record insertion\n")
    show_tables()
    table_field=input("Please Enter the table name\n")
    my_cursor = mydb.cursor()
    # to get the column name present in given table
    my_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'assignment2' AND TABLE_NAME = '%s' " %table_field)
    lst=[]
    # for each column field user need to enter the value
    for x in my_cursor:
        #print(x)
        if x != ('dept_name',):
            ele=input("Please enter the value for %s : " %x )
        else :
            print("Please choose/enter the department from the below mentioned list\n ")
            print("1.Comp. Sci.\n2.Biology\n3.Elec. Eng.\n4.Finance\n5.History\n6.Music\n7.Physics\n")
            ele=input("Please enter the value for %s : " %x )
        # we are appending it to the list
        lst.append(ele)
    #print(lst)
    my_cursor1 = mydb.cursor()
    # executing "INSERT STATEMENT"
    my_cursor1.execute("INSERT INTO %s VALUES %s" %(table_field,tuple(lst)))
    # to commit the insert query
    mydb.commit()
    print("Record got inserted\n")
    # to print the column names
    my_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'assignment2' AND TABLE_NAME = '%s' " %table_field)
    title=[]
    for x in my_cursor:
        for t in x:
        #print(x)
            title.append(t)
    print(title)
    my_cursor.execute("SELECT * FROM %s "%table_field)
    l=[]
    for x1 in my_cursor:
        l.append(list(map(str,list(x1))))
    for z in l :
        print(z)
    
    print("\n")
    main()

# helps us to gather the instructor details ( class taught by instructor )
def instructor_details():

    id=int(input("Please enter the instructor id to display the classes of the instructor \n "))
    #print(type(id))
    # displaying all the classes taught by the professor
    print("\nDisplaying the classes of the instructor\n")
    mycursor.execute("SELECT TITLE,COURSE_ID FROM course WHERE COURSE_ID IN ( SELECT COURSE_ID FROM teaches WHERE ID = %i )" %id)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(list(x))
    # displaying the details taught by instructor in semester=FALL and year =2022
    print("\nDisplaying the current semester classes taught by the professor(Semester= FALL and Year=2022)\n")
    mycursor.execute("SELECT COURSE.TITLE,COURSE.COURSE_ID,TEACHES.SEMESTER,TEACHES.YEAR FROM course JOIN teaches ON COURSE.COURSE_ID=TEACHES.COURSE_ID WHERE TEACHES.ID = %i AND TEACHES.semester='fall' AND TEACHES.year=2022" %id)
    myresult = mycursor.fetchall()
    lst=[]
    i=[]
    for x in myresult:
        #print(x)
        lst.append(list(map(str,list(x))))
    for i in lst :
        print(i)

    if i!=[] :
        print(i)
    else :
        print("Currently there were no classes taught by professor \n")
    # displaying the details taught in fall semester
    print("\nDisplaying the fall semester classes taught by the professor\n")
    mycursor.execute("SELECT COURSE.TITLE,COURSE.COURSE_ID,TEACHES.SEMESTER,TEACHES.YEAR FROM course JOIN teaches ON COURSE.COURSE_ID=TEACHES.COURSE_ID WHERE TEACHES.ID = %i AND TEACHES.semester='fall'" %id)
    myresult = mycursor.fetchall()
    l=[]
    z=[]
    for x in myresult:
        #print(x)
       l.append(list(map(str,list(x))))
    for z in l :
        print(z)

    if z!=[] :
        print(z)
    else :
        print(" Currently there were no classes taught by professor \n")
        
    main()

def add_class():

    inst_id=int(input("Please enter the instructor id you want to assign class "))
    class_id=input("Please enter the course id you want to assign ")
    # checking if instructor id and course id are exists or not
    mycursor.execute("SELECT id,course_id from teaches where id=%i AND course_id='%s'" %(inst_id,class_id) )
    lst=[]
    for x in mycursor:
        print(x)
        lst.append(x)
    #print(lst)
    # if exists no need to assign classes
    if lst !=[] :
        print("The class is already assigned\n")
    # if not we will assign classes
    else :
        my_cursor = mydb.cursor()
        # requesting for details
        print(" Please enter the requested details to assign class for an instructor \n")
        # taking section details
        my_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'assignment2' AND TABLE_NAME = 'section'")
        l=[]
        for x1 in my_cursor:
            if x1 == ('building',):
                print("Please choose the building name from the below mentioned list\n ")
                print("1.Packard\n2.Painter\n3.Taylor\n4.Watson\n")
                ele=input("Please enter the value for %s : " %x1 )
            elif x1 == ('room_number',):
                print("Please choose the room number for respective building from the below mentioned list\n ")
                print("1.Packard-101\n2.Painter-514\n3.Taylor-3128\n4.Watson-100 or 120\n")
                ele=input("Please enter the value for %s : " %x1 )
            else :
                ele=input("Please enter the details for %s : " %x1 )
            l.append(ele)
        # taking course details
        my_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'assignment2' AND TABLE_NAME = 'course'")
        l1=[]
        for x2 in my_cursor:
            if x2 != ('dept_name',):
                ele=input("Please enter the value for %s : " %x2 )
            else :
                print("Please choose/enter the department from the below mentioned list\n ")
                print("1.Comp. Sci.\n2.Biology\n3.Elec. Eng.\n4.Finance\n5.History\n6.Music\n7.Physics\n")
                ele=input("Please enter the details for %s : " %x2 )
            l1.append(ele)
        query="INSERT INTO course VALUES {}" .format(tuple(l1))
        my_cursor1 = mydb.cursor()
        my_cursor1.execute(query)
        #mydb.commit()
        query1="INSERT INTO SECTION VALUES {}" .format(tuple(l))
        #print(query1)
        my_cursor2 = mydb.cursor()
        my_cursor2.execute(query1)
        mydb.commit()
        l2=[]
        l2.append(inst_id)
        l2.extend(l[0:4])
        #print(l2)
        # inserting into teaches table
        query2="INSERT INTO Teaches VALUES {}" .format(tuple(l2))
        my_cursor2.execute(query2)
        mydb.commit()
        my_cursor2.execute("select * FROM Teaches")
        for x in my_cursor2:
            #print(x)
            l.append(list(map(str,list(x))))
        for z in l :
            print(z)
        main()
        

def main():
    
    print("Please select the option from given menu:")
    choice=(input("A : Display tables\nB : Insert Record\nC : Instructor Details\nD : Add Class\nE : Exit\n"))
    if choice=="A" or choice=="a" :
        display_tables()
    elif choice=="B" or choice=="b" :
        insert_records()
    elif choice=="C" or choice=="c" :
        instructor_details()
    elif choice=="D" or choice=="d" :    
        add_class()
    elif choice=="E" or choice=="e" :
        # closing the connection class
        print("Exiting.....!\n")
        mydb.close()
    else :
        print("\nInvalid option! Please select the correct option")
    return choice

#___main__
print("Welcome to MYSQL Menu page\n")
main()
    
