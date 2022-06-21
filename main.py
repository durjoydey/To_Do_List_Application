ToDoList={}
filename='todolist.txt'
z=0
description = []
date = []
place = []
time = []

flag=0;
def display_ToDoList():
    i=len(description)
    y=i-z
    print("Description\t\tDate\t\tPlace\t\tTime")
    for x in range(y):
        print(description[x],"\t\t",date[x],"\t\t",place[x],"\t\t",time[x])

while True:
 choice= int(input("1.Add Functionality\n 2.Check Functionality\n 3.Display Functionality\n 4.Update Functionality\n 5.Delete Functionality\n 6.Conflicting Functionality\n 7.File Open\n 8.Exit\n Enter Your Choice:"))
 
 if choice ==1:
     description.append(str(input("Enter Description: ")))
     date.append(str(input("Enter Date: ")))
     place.append(str(input("Enter  place: ")))
     time.append(str(input("Enter Time: ")))
     
 elif choice == 2:
     check_date= input("Enter the date:")
     i=len(date)
     for x in range(i):
         if date[x] == check_date:
             print(check_date,"has",description[x], "at",place[x])
             flag=1
     if flag == 0:
         print("Invalid Date")
             
 elif choice==3:
    
          display_ToDoList()
          
 elif choice==4:
    n= int(input("1.Edit Description\n 2.Edit Date \n 3.Edit Place\n 4.Edit Time\n Enter Your Choice:"))
    if n == 1: 
       edit_date=input("Enter the date of description you want to edit:")
       i=len(date)
       for x in range(i):
          if date[x] == edit_date:
             description[x]=str(input("Enter new description:"))
             flag=1
             display_ToDoList()
       if flag == 0:
          print("Description isn't found in your ToDoList")
    elif n == 2: 
       edit_date=input("Enter the date you want to edit:")
       i=len(date)
       for x in range(i):
          if date[x] == edit_date:
             date[x]=str(input("Enter new date:"))
             flag=1
             display_ToDoList()
       if flag == 0:
          print("date isn't found in your ToDoList")
    elif n == 3: 
       edit_date=input("Enter the date of place you want to edit:")
       i=len(date)
       for x in range(i):
          if date[x] == edit_date:
             place[x]=str(input("Enter new place:"))
             flag=1
             display_ToDoList()
       if flag == 0:
          print("Place isn't found in your ToDoList")
    elif n == 4: 
       edit_date=input("Enter the date of time you want to edit:")
       i=len(date)
       for x in range(i):
          if date[x] == edit_date:
             time[x]=str(input("Enter new time:"))
             flag=1
             display_ToDoList()
       if flag == 0:
          print("Time isn't found in your ToDoList")      
   
 elif choice==5:
        ToDoList = str(input("Enter the ToDoList you want to delete:"))
        i=len(date)
        for x in range(i):
            if date[x] == ToDoList:
                if x == i-1:
                    z+=1
                else:       
                    date[x]=date[x+1]
                    place[x]=place[x+1]
                    description[x]=description[x+1]                  
                    z+=1

   

 elif choice==7:
        with open(filename,'a') as file_object:
             file_object.write("Wedding Ceremony in Dhanmondi at 18 September 2022 9:00pm.")

 else:
    break