#Beh Vin Ze, Lee Hao Ming
#TP074210, TP074709

#To run this programme smoothly, kindly save all the files in a folder and run the entire folder in a source code editor

import datetime
current_datetime = datetime.datetime.now()
current_datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")


abc = []

def login():
    uid = input('Enter User ID: ')
    pwd = input('Enter Password: ')
    flg = False
    userType = ''
    with open('users.txt', 'r') as fh:
        for line in fh:
            rec = line.strip().split("|")
            if (rec[0]==uid and rec[1]==pwd ):
                flg = True
                userType = rec[-1]
                break

    return flg,userType

#To let admin to add users
def Add():
    with open('users.txt', 'r') as fh:
        lines = fh.readlines()
    for data in lines:
        rec = data.strip().split('|')  
        print(rec)  
    while True:
        uid = input('Enter new User ID (Press Enter to return): ')
        if uid == '':
            return AdminMenu()
        uid_check = False
        for data in lines:
            rec = data.strip().split('|') 
            if rec[0] == uid:
                print('User ID has been taken. Please Try Again. ')
                uid_check = True
                break
        if uid_check: #if uid_check = True, continue looping the uid input.
            continue

        username = input('Enter new User Name: ')
        username_check = False
        for data in lines:
            rec = data.strip().split('|') 
            if rec[2] == username:
                print('User Name has been taken. Please Try Again.')
                username_check = True
                break
        if username_check:
            continue

        pwd = input('Create new Password: ')
        userType = input('User Type (A/S): ')
        newuser = uid+'|'+pwd+'|'+username+'|'+userType+'\n'
        with open('users.txt', 'a') as fh:
            fh.write(newuser)
        print('User account has created successfully.')
        break

def ChangeID():
    print ('ChangeID')
    flg = False
    with open('users.txt', 'r') as fh:
        lines = fh.readlines()
    
    users = []

    for line in lines:
        rec = line.strip().split('|')  
        users.append(rec)  
    print(users)

    search = input("Please Enter the UserID to Change ID [Press Enter to return]: ")
    if search == "":
        return Modify()

    NewID = input("Please Enter the New ID [Press Enter to return]: ")
    if NewID == "":
        return Modify()

    for rec in users:
        if search == rec[0]:
            flg = True
            for data in users:
                if NewID == data[0]:
                    print('ERROR!!!!!!!!!!')
                    print("ID has been taken,Please Try Again")
                    print("="*100)
                    return ChangeID()
            rec[0] = NewID
            print(rec)
            print('UserID has been updated successfully')

    if not flg:
        print('User not found')
        print("="*100)
        return ChangeID()
    with open('users.txt', 'w') as fh:
        for rec in users:
            fh.write('|'.join(rec) + '\n')


def ChangeName():
    print ('ChangeName')
    flg = False
    with open('users.txt', 'r') as fh:
        lines = fh.readlines()
    
    users = []

    for line in lines:
        rec = line.strip().split('|')  
        users.append(rec)
    print(users)

    

    search = input("Enter the UserID to Change Name [Press Enter to return]: ")
    if search == "":
        return Modify()
    
    NewName = input("Please Enter the New Name [Press Enter to return]: ")
    if NewName == "":
        return ChangeName()
    
    for rec in users:
        if search == rec[0]:
            flg = True
            for data in users:
                if NewName == data[2]:
                    print('ERROR!!!!!!!!!!')
                    print("Name has been taken,Please Try Again")
                    print("="*100)
                    return ChangeName()
            rec[2] = NewName
            print('User Name has been updated successfully')
            print(rec)

    if not flg:
        print('User not found')
        print("="*100)
        return ChangeName()
    with open('users.txt', 'w') as fh:
        for rec in users:
            fh.write('|'.join(rec) + '\n')


def ChangePass():
    print("Change User Password")
    flg = False
    with open('users.txt', 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        rec = line.strip().split('|')  
        print(rec)
    
    search = input('Enter UserID to Change Password [Press Enter to return]: ')
    if search == '':
        return Modify()
    for index in range(len(lines)):
        rec = lines[index].strip().split("|")
        if rec[0] == search:
            print(rec)
            flg = True
            newpass = input("Enter New Password [Press Enter to return]: ") 
            if newpass == "":
                return ChangePass()
            rec[1] = newpass
            lines[index] = '|'.join(rec) + '\n'
            print("New Password has been updated.")
            print(rec)
                 
    if not flg:
        print('User not found')
        print("="*100)
        return ChangePass()
    with open('users.txt', 'w') as fh:
        fh.writelines(lines)

#ModifyUser
def Modify():
    print("Choose the number")
    print("1.Change User ID")
    print("2.Change User Name")
    print("3.Change User Account Password")
    option = input('Enter your option: ')
    print('='*50)
    if option == '1':
        ChangeID()
    if option == '2':
        ChangeName()
    elif option == '3':
        ChangePass()

def Delete():
    allrec = []
    with open('users.txt', 'r') as fh:
        for line in fh:
            allrec.append(line.strip().split("|"))

    for rec in allrec:
        print(rec[0],rec[1],rec[2],rec[3])

    skey = input("Enter user ID to delete: ")
    ind = -1
    for i in range(len(allrec)):
        if (skey in allrec[i][0]):
            ind = i
            break
    if ind != -1:
        print(allrec[ind])
        ans = input("Are you sure to delete (y/n): ")
        if ans.lower() == "y" or ans.upper() == 'Y':
            del allrec[ind]
            print("User is successfully deleted.")
        else:
            print("User is not deleted.")
            return
            
    print(allrec)

    with open('users.txt', 'w') as fh:
        for rec in allrec:
            record = "|".join(rec) + "\n"
            fh.write(record)

def Search():
    #Search users
    flg = False
    search = input("Enter the user ID or user Name to Search:")

    with open('users.txt', 'r') as fh:
        lines = fh.readlines()

    for line in lines:
        rec = line.strip().split("|")
        if rec[0] == search or rec[2] == search:
            print(rec)
            flg = True
    if not flg:
        print('users not found')

def Transaction_Cancel():
    with open('transactions.txt', 'r') as fh:
        lines = fh.readlines()
    for i, line in enumerate(lines, 1): #The enumerate function assigns an index (starting from 1) to each line in fh. 
        print(f"{i}: {line.strip()}") #i represents the line number, and line contains the content of each line.
    trancancle = input('Please enter a number to delete the specific row of transaction [Press Enter to return]: ')
    if trancancle == '':
        return AdminMenu()
    trancancle = int(trancancle)
    if 1 <= trancancle <=len(lines):
        print(lines[trancancle - 1])
        ans = input('Do you sure to delete the selected transaction history (y/n)?: ')
        if ans == 'Y' or ans == 'y':
            del lines[trancancle - 1]
            with open('transactions.txt', 'w') as fh:
                fh.writelines(lines)
            print('Transaction has successfully deleted.')
    
    else:
        print('Invalid input. Please enter correct row number.')

def add_PPE():
    new_item_code= input('Please enter a new item code: ')
    new_item_name= input('Please enter a new item name: ')
    initial_quan = input('Please enter the initial quantity of the item: ')
    item_sup = input('Please enter the supplier code for the supplying of the item: ')
    item_dis = input('Please enter a hospital code for the distribution of the item: ')
    new_rec = '\n'+new_item_code+'|'+new_item_name+'|'+initial_quan+'|'+item_sup+'|'+item_dis
    with open('PPE.txt', 'a') as fh:
        fh.write(new_rec)

def AdminMenu():
    print('Admin Menu')
    print('1. Add new user')
    print('2. Modify user')
    print('3. Delete user')
    print('4. Search user')
    print('5. Inventory Management')
    print('6. Cancel Transaction')
    print('7. Add PPE Item')
    print('8. Exit')
    option = input('Enter your option: ')
    print('='*50)
    if option == '1':
        Add()
    elif option == '2':
        Modify()
    elif option == '3':
        Delete()
    elif option == '4':
        Search()
    elif option == '5':
        InventoryManagement()
    elif option == '6':
        Transaction_Cancel()
    elif option == '7':
        add_PPE()
    elif option == '8':
        print('Thankyou')
        exit() 
    
    restart = input('Do you want to go back to the menu (y/n): ')
    if restart == 'y' or restart == 'Y':
        return AdminMenu()
    else:
        print('='*50)
        print('Thankyou')
        exit()

def StaffMenu():
    print('Staff Menu')
    print('1. Inventory Management')
    print('2. Exit')
    option = input('Enter your option: ')
    print('='*50)
    if option == '1':
        InventoryManagement()
    elif option == '2':
        print('Thankyou')
        exit()

    restart = input('Do you want to go back to the menu (y/n): ')
    if restart == 'y' or restart == 'Y':
        return StaffMenu()
    else:
        print('='*50)
        print('Thankyou')
        exit()
        

def Check():
    print('Item Details:')
    print('_'*100)
    header = ['Item Code', 'Item Name', 'Quantity(Box)', 'Supplier Code', 'Hospital Code']
    for i in header:
        i = i.center(20)
        print(i, end='')
    print()
    print('_'*100)
    
    tmplist = []
    with open('PPE.txt', 'r') as fh:
        for line in fh:
            rec = line.strip().split('|')
            tmplist.append(rec) # all records from txt will append into a temporary list
    
    tmplist.sort() #sort function will sort the string in tmplist base on the natural order(Alphabetical order)

    # Print the sorted records
    width = 20
    for rec in tmplist:
        for item in rec:
            itemlist = item.center(width)
            print(itemlist, end='')
        print()
        print('_'*100)
    
def Insufficient():
    insuff = False
    with open('PPE.txt', 'r') as fh:
        print('Stock items below 50 boxes will be shown.')
        for line in fh:
            rec = line.strip().split('|')
            stock = int(rec[2])
            item = rec[1]
            itemcode = rec [0]
            supply = rec[3]
            if stock <= 25:
                print(f'{item} has only {stock} boxes left. ') 
                print(f'Insufficient Item : {item} \nItem code : {itemcode} \nSupplier: {supply}')
                print('='*50)
                insuff = True
    if not insuff:
        print('There is no insufficient item.')

def receive():
    temp1 = [] #Item Code list
    with open ('PPE.txt', 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        rec = line.strip().split('|')
        temp1.append(rec[0])
    
    temp2 = []  #Supplier Code list
    with open ('suppliers.txt', 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        rec = line.strip().split('|')
        temp2.append(rec[0])

    while True:
        Check()
        print(temp1)
        itemcode = input('Please enter an item code[press Enter to return]: ')
        if itemcode =='':
            return InventoryManagement()
        
        elif itemcode not in temp1:
            print('Please enter a correct item code. ')
            continue #will continue looping if itemcode does not match the item code
        
        with open('PPE.txt', 'r') as fh1:
            lines = fh1.readlines()#read every line in PPE.txt 

        print(temp2)
        supplier = input('Item received from (supplier code): ')
        supplier_found = False
        for line in lines:
            data = line.strip().split('|')
            if data[0] == itemcode and supplier != data[3]:
                print('Please enter a correct supplier code. ')
                supplier_found = True
                break #this is to check if the item code match the supplier or not, if does not match it will jump out the for loop and loop the while loop again
        if supplier_found:
            continue

        quantity_rec = input('Please enter received quantity: ')
        if quantity_rec.isdigit():
            quantity = int(quantity_rec)
        
        else:
            print('Please enter a valid integer for the quantity! ')
            continue #this is to check whether the user input a valid integer or not, if not it will loop again

        print('_'*50)

        rec = itemcode+'|'+supplier+'|'+str(quantity)+'|'+current_datetime_str+'|'+'R'+'\n'
        with open('transactions.txt', 'a') as fh2:
            fh2.write(rec) #everything user had entered will be recorded into transactions.txt with the formular of rec
        print(f'{rec}has successfully recorded into transaction.txt. ')
        print('_'*50)

        for line in lines:
            data = line.strip().split('|') #the .strip() is used to avoid empty spaces and .split('|') is used to separate every component in every line
            if data[0] == itemcode: #after spliting the line with '|', data now will be a list of list. To search the correct row, data[0] is actually the first column in PPE.txt, the data[0] == itemcode means row = column
                newquantity = int(data[2]) + quantity #data[2] is a string in a list, it cannot do any addition with integer so it has change into integer
                data[2] = str(newquantity) #after the addition, newquantity is an integer type, int type cannot be added into a str type list, so it has to change into str to make it same type
            abc.append('|'.join(data))#abc is an empty list, after replacing a new data in data[2], .append('|'.join(data)) will append the new data spliting with '|'
        
        with open('PPE.txt', 'w') as fh:
            fh.writelines('\n'.join(abc)) #this will join the abc list into PPE.txt
        Check()
        abc.clear() #this is to clear the temp list abc to avoid overlapping 
        break

def distribute():
    temp1 = [] #Item Code list
    with open ('PPE.txt', 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        rec = line.strip().split('|')
        temp1.append(rec[0])

    temp3 = []  #Hospital Code list
    with open ('hospitals.txt', 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        rec = line.strip().split('|')
        temp3.append(rec[0])

    while True:
        Check()
        print(temp1)
        itemcode = input('Please enter an item code[press Enter to return]: ')
        if itemcode =='':
            return InventoryManagement()
        
        elif itemcode not in temp1:
            print('Please enter a correct item code. ')
            continue

        with open('PPE.txt', 'r') as fh1:
            lines = fh1.readlines()

        for line in lines:
            rec = line.strip().split('|')
            if itemcode == rec[0] and int(rec[2]) < 25:
                print('Current stock level for the item is lower than 25. Unavailable to distribute item.')
                return distribute()

        print(temp3)
        hospital = input('Please enter hospital code to distribute item: ')
        hospital_found = False
        for line in lines:
            data = line.strip().split('|')
            if data[0] == itemcode and hospital != data[-1]:
                print('Please enter a correct hospital code. ')
                hospital_found = True
                break
        if hospital_found:
            continue

        quantity_rec = input('Please enter distributed quantity: ')
        if quantity_rec.isdigit():
            quantity = int(quantity_rec)
        
        else:
            print('Please enter a valid integer for the quantity! ')
            continue

        for line in lines:
            data = line.strip().split('|')
            if data[0] == itemcode and int(data[2]) >= quantity: #this is to check whether the stock is enough or not, if not it will print out insufficient stock.
                rec = itemcode+'|'+hospital+'|'+str(quantity)+'|'+current_datetime_str+'|'+'S'+'\n' #this is to avoid insufficient stock but transaction is still recorded in the transactions.txt
                with open('transactions.txt', 'a') as fh2:
                    fh2.write(rec)
                print('_'*50)
                print(f'{rec}has successfully recorded into transaction.txt. ')
                print('_'*50)
                newquantity = int(data[2]) - quantity
                data[2] = str(newquantity)
            elif data[0] == itemcode and int(data[2]) < quantity:
                print('Insufficient stock for the item to distribute. ')
                return
            abc.append('|'.join(data))
        with open('PPE.txt', 'w') as fh:
            fh.writelines('\n'.join(abc))
        Check()
        abc.clear()
        break

def Receive_and_Distribute():
    print('[1] Receive')
    print('[2] Distribute')
    trantype = input('Please select transaction type: ')
    if trantype == '1':
        receive()

    elif trantype == '2':
        distribute()

def TrackReceived():
    #track item received from specific time period
    from datetime import datetime
    with open('transactions.txt', 'r') as fh:
        readdate = fh.readlines()

    print('Item received during a specific time period. ')
    startdate = input('Please enter start date (YYYY-MM-DD): ')
    enddate = input('Please enter end date (YYYY-MM-DD): ')

    start_datetime = datetime.strptime(startdate, "%Y-%m-%d") #to convert the dates to datetime objects
    end_datetime = datetime.strptime(enddate, "%Y-%m-%d")

    tranflg = False

    print('='*50)
    print('Transactions within the specified date range: ')

    header = ['Item Code', 'Supplier/Hospital', 'Quantity(Box)', 'Date & Time', 'Transaction Type']
    print('_'*100)
    for i in header:
        i = i.center(20)
        print(i, end='')
    print()
    print('_'*100)

    for line in readdate:
        rec = line.strip().split('|')
        daterecorded = datetime.strptime(rec[3], "%Y-%m-%d %H:%M:%S").date()
        width = 20
        if start_datetime.date() <= daterecorded <= end_datetime.date() and rec[-1] == 'R':
            for row in rec:
                transactionlist = row.center(width)
                print(transactionlist, end='')
            print()
            print('_'*100)
            
            tranflg = True

    if not tranflg:
        print('There are no transactions in the specified date range.')

def TrackDisributed():
    from datetime import datetime
    with open('transactions.txt', 'r') as fh:
        readdate = fh.readlines()

    print('Item distributed during a specific time period. ')
    startdate = input('Please enter start date (YYYY-MM-DD): ')
    enddate = input('Please enter end date (YYYY-MM-DD): ')

    start_datetime = datetime.strptime(startdate, "%Y-%m-%d") #to convert the dates to datetime objects
    end_datetime = datetime.strptime(enddate, "%Y-%m-%d")

    tranflg = False

    print('='*50)
    print('Transactions within the specified date range: ')

    header = ['Item Code', 'Supplier/Hospital', 'Quantity(Box)', 'Date & Time', 'Transaction Type']
    print('_'*100)
    for i in header:
        i = i.center(20)
        print(i, end='')
    print()
    print('_'*100)

    for line in readdate:
        rec = line.strip().split('|')
        daterecorded = datetime.strptime(rec[3], "%Y-%m-%d %H:%M:%S").date()
        width = 20
        if start_datetime.date() <= daterecorded <= end_datetime.date() and rec[-1] == 'S':
            for row in rec:
                transactionlist = row.center(width)
                print(transactionlist, end='')
            print()
            print('_'*100)
            
            tranflg = True

    if not tranflg:
        print('There are no transactions in the specified date range.')

#Mainlogic
def TrackingDate():
    print('[1] Track Item and Quantity Received in Specific Time Period.')
    print('[2] Track Item and Quantity Distributed in Specific Time Period.')
    trackopt = input('Please enter your option: ')
    if trackopt == '1':
        TrackReceived()
    elif trackopt == '2':
        TrackDisributed()
   
def TrackQuantity():
    temp1 = [] #Item Code list
    with open ('PPE.txt', 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        rec = line.strip().split('|')
        temp1.append(rec[0])
    while True:
        print(temp1)
        searchcode = input('Please enter an item code to track available quantity of the item: ')
        if searchcode not in temp1:
            print('Please enter a valid item code.')
            continue
        
        else:
            header = ['Item Code', 'Item Name', 'Quantity(Box)', 'Supplier Code', 'Hospital Code']
            print('_'*100)
            for i in header:
                i = i.center(20)
                print(i, end='')
            print()
            print('_'*100)
            with open('PPE.txt', 'r') as fh:
                lines = fh.readlines()

            for line in lines:
                rec = line.strip().split('|')
                width = 20
                if rec[0] == searchcode:
                    for item in rec:
                        searchitem = item.center(width)
                        print(searchitem, end='')
                    print()
                    print('_'*100)

        break

def distribution_details():
    temp1 = [] #Item Code list
    with open ('PPE.txt', 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        rec = line.strip().split('|')
        temp1.append(rec[0])
    while True:
        print(temp1)
        searchcode = input('Please enter an item code to check the details of total item distributed: ')
        if searchcode not in temp1:
            print('Please enter a valid item code.')
            continue
        
        else:
            header = ['Item Code', 'Supplier/Hospital', 'Quantity(Box)', 'Date & Time', 'Transaction Type']
            print('_'*100)
            for i in header:
                i = i.center(20)
                print(i, end='')
            print()
            print('_'*100)
            with open('transactions.txt', 'r') as fh:
                lines = fh.readlines()
            
            totalquantity = 0

            for line in lines:
                rec = line.strip().split('|')
                width = 20
                if rec[0] == searchcode and rec[-1] == 'S':
                    allquantity = int(rec[2])
                    for item in rec:
                        searchitem = item.center(width)
                        print(searchitem, end='')
                    print()
                    print('_'*100)
                    totalquantity += allquantity
                        
            print(f'Total Quantity Distributed: {str(totalquantity).center(44)}')
            print('_'*100)
            
        break
                
def receive_details():
    temp1 = [] #Item Code list
    with open ('PPE.txt', 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        rec = line.strip().split('|')
        temp1.append(rec[0])
    while True:
        print(temp1)
        searchcode = input('Please enter an item code to check the details of total item received: ')
        if searchcode not in temp1:
            print('Please enter a valid item code.')
            continue
        
        else:
            header = ['Item Code', 'Supplier/Hospital', 'Quantity(Box)', 'Date & Time', 'Transaction Type']
            print('_'*100)
            for i in header:
                i = i.center(20)
                print(i, end='')
            print()
            print('_'*100)
            with open('transactions.txt', 'r') as fh:
                lines = fh.readlines()
            
            totalquantity = 0

            for line in lines:
                rec = line.strip().split('|')
                width = 20
                if rec[0] == searchcode and rec[-1] == 'R':
                    allquantity = int(rec[2])
                    for item in rec:
                            searchitem = item.center(width)
                            print(searchitem, end='')
                    print()
                    print('_'*100)
                    totalquantity += allquantity
                        
            print(f'Total Quantity Received: {str(totalquantity).center(50)}')
            print('_'*100)
            
        break

def Searchfunctionalities():        
    print('[1] Search for total item received')
    print('[2] Search for total item distributed')
    option = input('Please enter your option: ')
    if option == '1':
        receive_details()
    elif option == '2':
        distribution_details()

def SupDetails():
    Sup_detail = ['Supplier Code', 'Supplier Name']
    for i in Sup_detail:
        i = i.center(30)
        print(i, end='')
    print()
    print('_'*60)

    with open ('suppliers.txt', 'r') as fh:
        for line in fh:
            rec = line.strip().split('|')
            for data in rec:
                suplist = data.center(30)
                print(suplist, end='')
            print()
            print('_'*60)

def HosDetails():
    Hos_detail = ['Hospital Code', 'Hospital Name']
    for i in Hos_detail:
        i = i.center(30)
        print(i, end='')
    print()
    print('_'*60)

    with open ('hospitals.txt', 'r') as fh:
        for line in fh:
            rec = line.strip().split('|')
            for data in rec:
                hoslist = data.center(30)
                print(hoslist, end='')
            print()
            print('_'*60)

def InventoryManagement():
    print("Item Inventory Management")
    print("1. Inventory List")
    print("2. Item Supplied or Distributed")
    print("3. Insufficient Stock Items")
    print("4. Track Available Quantity of Particular Item")
    print("5. Track Quantity Received or Distributed Between Time Period ")
    print('6. Search Transaction Details of Particular Item')
    print('7. Check for Supplier Details')
    print('8. Check for Hospital Details')
    print("9. Exit")
    option = input("Enter your option: ")
    print('='*50)
    if option == '1':
        Check()    
    elif option == '2':
        Receive_and_Distribute()
    elif option == '3':
        Insufficient()
    elif option == '4':
        TrackQuantity()
    elif option == '5':
        TrackingDate()
    elif option == '6':
        Searchfunctionalities()
    elif option == '7':
        SupDetails()
    elif option == '8':
        HosDetails()
    elif option == '9':
        if userType == 'A':
            return AdminMenu()
        elif userType == 'S':
            return StaffMenu()
    
    restart = input('Do you want to go back to the menu (y/n): ')
    if restart == 'y' or restart == 'Y':
        return InventoryManagement()
    else:
        print('='*50)
        print('Thankyou')
        return exit()

def Initial_Setup():
    #Supplier Setup
    with open ('suppliers.txt', 'r') as fh:
        data0 = fh.read()
    
    if len(data0) == 0 :
        print('='*80)
        print('Supplier Detail Setup')
        while True:
            Supcode = input('Please enter a supplier code: ')
            Supname = input('Please enter a supplier name: ')
            Supdetails = Supcode+'|'+Supname+'\n'
            with open ('suppliers.txt', 'a') as fh:
                fh.write(Supdetails)
            print('Supplier Details successfully setup.')
            answer = input('Do you want to continue supplier detail setup (y/n): ')
            if answer == 'Y' or answer == 'y':
                continue
            else:
                print('Supplier Detail Setup Done.')
                break

    #Hospital Setup
    with open ('hospitals.txt', 'r') as fh:
        data1 = fh.read()
    
    if len(data1) == 0 :
        print('='*80)
        print('Hospital Detail Setup')
        while True:
            Hoscode = input('Please enter a Hospital code: ')
            Hosname = input('Please enter a Hospital name: ')
            Hosdetails = Hoscode+'|'+Hosname+'\n'
            with open ('hospitals.txt', 'a') as fh:
                fh.write(Hosdetails)
            print('Hospital Details successfully setup.')
            answer = input('Do you want to continue hospital detail setup (y/n): ')
            if answer == 'Y' or answer == 'y':
                continue
            else:
                print('Hospital Detail Setup Done.')
                break

    #Inventory Setup
    with open('PPE.txt', 'r') as fh:
        data2 = fh.read()

    if len(data2) == 0 :
        print('='*80)
        print('Initial Inventory Setup')
        while True:
            itemcode = input('Please enter an item code: ')
            itemname = input('Please enter an itemname: ')
            quantity = int(input('Please enter the quantity of the item: '))
            with open('suppliers.txt', 'r') as fh1:
                for line in fh1:
                    rec = line.strip().split('|')
                    print(rec)
            supplier = input('Please enter a supplier code: ')
            with open('hospitals.txt', 'r') as fh2:
                for line in fh2:
                    rec = line.strip().split('|')
                    print(rec)
            receiver = input('Please enter a hospital code: ')
            PPE = itemcode+'|'+itemname+'|'+str(quantity)+'|'+supplier+'|'+receiver+'\n'
            with open('PPE.txt', 'a') as fh:
                fh.write(PPE)
            print('Item Inventory successfully setup.')
            answer = input('Do you want to continue initial inventory setup (y/n): ')
            if answer == 'Y' or answer == 'y':
                continue
            else:
                print('Initial Inventory Setup Done.')
                break

#MainLogic
while True:
    valid = login()
    userType = valid[1]

    if valid[0] == True :
        print('Login Successful...')
        if userType == 'A':
            Initial_Setup()
            AdminMenu()
        elif userType == 'S':
            StaffMenu()
        break

    else:
        print('Login Unsuccessful. Please Try Again.')


   


