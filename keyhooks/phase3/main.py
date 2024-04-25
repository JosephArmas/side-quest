import pymongo
from pymongo import MongoClient

def printMenu():
    print("1. Create a new Key")
    print("2. Request access to a given room by a given employee")
    print("3. Display key issued to an employee")
    print("4. Capturing losing a key")
    print("5. Display all rooms an employee can enter, given the key that they already have")
    print("6. Delete a key")
    print("7. Delete an employee")
    print("8. Add a new door that can be opened by an existing hook")
    print("9. Update an access request to move it to a new employee")
    print("10. Display all employees who can get into a room")
    print("0. Quit")

def menu():
    printMenu()
    while True:
        try:
            select = int(input('Enter Choice: '))
        except ValueError:
            print('please enter numbers')
        else:
            if select == 0:
                print('exiting...')
                break
            elif select == 1:
                # TODO - Present list
                for x in keys.find({}, {"_id":0, "key_id":1, "hook_id":1}):
                    print(x) 
                while True:
                    try:
                        hook_input = int(input('Enter hook: '))
                        key_number = int(input('Enter a key number: '))
                    except ValueError:
                        print('enter number please')
                    else:
                        if list(hooks.find({'hook_id' : {'$eq': hook_input}})):
                            print(f'hook_id:{hook_input}, key_number:{key_number} has been created')
                            new_key = {'hook_id': hook_input, 'key_id': key_number}
                            keys.insert_one(new_key)
                            print('going to home screen....')
                            print('')
                        else:
                            print('need to insert new key first')
                    break
                printMenu()

                # print(hook_input)
                # checker = hooks.find({'hook_id': {'$in': hook_input}})
                # print(type(checker))
                # checker = hooks.find({'hook_id': {'$exist': hook_input}})
                # checker = list(checker)
                # print(hooks.find({'hook_id': {'$exist': hook_input}}))

                # print(checker)

                # try: 
                    # result = hooks.find({'hook_id': hook_input})
                # except:
                    # print('enter int')
            elif select == 2:
                # TODO - Request access to a given room by a given employeer
                # TODO - show popoulated employees 
                # TODO - show buildings and room
                for x in employees.find({}, {'_id': 0, 'employee_id': 1, 'name': 1}):
                    print(x)
                while True:
                    try:
                        employee_num = int(input('Enter employee number: '))
                    except ValueError:
                        print('enter number please')
                    else:
                        for j in rooms.find({}, {'_id': 0, 'building_name': 1, 'room_number': 1}):
                            print(j)
                        try:
                            room = int(input('Enter room number: '))
                        except: 
                            print('error please try again')                            
                        else:
                            building = input('Enter building name: ')
                            requestDate = input('Enter request date (xxxx-xx-xx): ')
                            l1 = {'employee_id': employee_num, 'building_name': building, 'room_number': room, 'date_requested': requestDate}
                            requests.insert_one(l1)
                            print('sucessfully enter in database')
                            print('going back to menu...')
                            print('')
                            break
                printMenu()
            elif select == 3:
                # TODO - Display key issued to an employee
                # TODO - show total request

                for r in requests.find({}, {'_id': 0, 'employee_id': 1, 'date_requested': 1, 'room_number': 1, 'building_name': 1}):
                    print(r)
                # TODO - show access
                while True:
                    try:
                        empId = int(input('enter employee number '))
                    except:
                        print('enter values 0-9')
                    else:
                        if list(requests.find({'employee_id' : {'$eq': empId}})):
                            print(True)
                            building = input('Enter building name ')
                            room = int(input('Enter room number '))
                            rq = access.find()
                            rq = list(rq)
                            for i in rq:
                                for k,v in i.items():
                                    if i['building_name'] == building and i['room_number'] == room:
                                        # print(i['hook_id'])
                                        hk = i['hook_id']
                                    # break
                                # break
                            r = requests.find()
                            r = list(r)
                            for i in r:
                                for k,v in i.items():
                                    if i['building_name'] == building and i['room_number'] == room:
                                        daterq = i['date_requested']
                                    # break
                                # break
                            k = keys.find()
                            k = list(k)
                            for i in k:
                                for k,v in i.items():
                                    if hk == i['hook_id']:
                                        keyID = i['key_id'] 
                                    # break
                                # break
                        # print(daterq)
                        kiu = {'loans_key_id' : keyID, 'employee_id': empId, 'room_number': room, 'building_name': building, 'date_requested': daterq}
                        loans.insert_one(kiu)
                        # print(keyID)
                        break
                printMenu()

            elif select == 4:
                # TODO - Capture losing a key
                # while True:
                #     try:
                #         empID = int(input('Enter employee id: '))
                #     except:
                #         print('enter value 0-9')
                #     else:
                #         keyID = int(input('Enter key'))
                for l in loans.find({}, {'_id': 0}):
                    print(l)
                empID = int(input('Enter employee id: '))
                keyID = int(input('Enter key id: '))
                ls = loans.find()
                ls = list(ls)
                for i in ls:
                    for k,v in i.items():
                        if i['employee_id'] == empID:
                            building = i['building_name']
                            room = i['room_number']
                            daterq = i['date_requested']
                datelost = input('enter date lost: (xxxx-xx-xx): ')
                kl = {'lost_report_date': datelost, 'loans_key_id': keyID, 'loans_employee_id': empID, 'room_number': room, 'building_name': building, 'loans_request_date': daterq}
                key_losts.insert_one(kl)
                printMenu()

            elif select == 5:
                # TODO - Display all rooms an employee can enter, given the key that they already have
                for e in employees.find({}, {'_id': 0, 'employee_id': 1, 'name': 1}):
                    print(e)
                while True:
                    try:
                        emp = int(input('Enter employee id: '))
                    except:
                        print('enter only values 0-9')
                    else:
                        for e in key_in_uses.find({'loans_employee_id': emp}, {'_id': 0, 'loans_key_id': 1, 'loans_employee_id': 1,'loans_building_name': 1, 'loans_room_number': 1,'loans_request_date':1}).sort('loans_building_name').sort('loans_room_number'):
                            print(e)
                        break
                printMenu()
            elif select == 6:
                # TODO - Delete a key 
                # TODO - iterate through keys 
                for k in keys.find({}, {'_id': 0, 'hook_id': 1, 'key_id': 1}):
                    print(k)
                while True:
                    try:
                        hook_input = int(input('Enter hook id: ')) 
                        key_input = int(input('Enter key id: '))
                    except:
                        print('please enter values 0-9')
                    else:
                        if list(key_in_uses.find({'loans_key_id': {'$eq': key_input}})):
                            # print(True)
                            # print(f'value is {key_input}')
                            print('please select another key. key is in use.')
                            break
                        else:
                            keys.delete_one({'hook_id': hook_input, 'key_id': key_input})
                            print('successfully deleted key ')
                    break
                printMenu()
            elif select == 7:
                # TODO - Display employees
                for e in employees.find({}, {'_id': 0, 'employee_id': 1}):
                    print(e)
                while True:
                    try:
                        del_id = int(input('Enter an employee id to delete: '))
                    except:
                        print('please enter values 0-9')
                    else:
                        # TODO - Delete an employee 
                        if list(key_in_uses.find({'loans_employee_id' : {'eq': del_id}})):
                            print('cant delete id. key in use with this id.')
                            break
                        else:
                            employees.delete_one({'employee_id': del_id})
                            print('employee id successfully deleted')
                        break
                printMenu()
            elif select == 8:
                # TODO - Add a new door that can be opened by an existing hook
                # TODO 
                # * print existing door types
                print('list of current door types: ')
                for dt in door_types.find({}, {'_id': 0, 'type': 1}):
                    print(dt)

                # * get user input and add it 
                new_door_type = input('Enter new door type: ')
                new_dt = {'type': new_door_type}
                door_types.insert_one(new_dt)

                # * display the access, but in the proccess enter it to the doors tables
                print('printing door access: ')
                for a in access.find({}, {'_id': 0, 'hook_id': 1, 'room_number': 1, 'building_name': 1, 'door_type': 1}):
                    print(a)
                while True:
                    try:
                        hk = int(input('Enter hook id: '))
                    except:
                        print('please enter values 0-9')
                    else:
                # * display doors and have user
                # * input building name
                        bn = input('Enter building name: ')
                # * input room number
                        while True:
                            try:
                                rm = int(input('Enter room number: '))
                            except:
                                print('please enter values 0-9')
                            else:
                                new_access = {'hook_id': hk, 'room_number': rm, 'building_name': bn, 'door_type': new_door_type}
                                access.insert_one(new_access)
                                print('successfuly created ')
                                break
                        break
                printMenu()
            elif select == 9:
                # TODO - Update an access request to move it to a new employee
                for rq in requests.find({}, {'_id': 0,'employee_id': 1, 'date_requested': 1, 'room_number': 1, 'building_name': 1}):
                    print(rq)
                while True:
                    try:
                        old_employeeid = int(input('Enter employee id to change: '))
                    except:
                        print('Enter values 0-9')
                    else:
                        while True:
                            try:
                                new_empid = int(input('Enter new employee id '))
                            except:
                                print('Enter values 0-9')
                            else:
                                name = input('Enter employee name: ')
                                new_e = {'employee_id': new_empid, 'name': name}
                                employees.insert_one(new_e)
                                requests.update_one({'employee_id': old_employeeid}, {'$set': {'employee_id': new_empid}})
                                print('Successfuly updated')
                                break
                        break
                printMenu()
            elif select == 10:
                # TODO - Display all employees who can get into a room
                print('Employee who can get into a room: ')
                # for e in key_in_uses.find({}, {'_id': 0, 'loans_key_id': 0, 'loans_employee_id': 1, 'loans_room_number': 0, 'loans_building_name': 0, 'loans_request_date': 0}):
                    # print(e)
                for e in key_in_uses.find({}, {'_id': 0}):
                    print(e)
                printMenu()

cluster = MongoClient("mongodb+srv://user:user@cluster0.p25noys.mongodb.net/?retryWrites=true&w=majority")
db = cluster["hooks_phase3"]
access = db["access"]
buildings = db["buildings"]
door_types = db["door_types"]
doors = db["doors"]
employees = db["employees"]
hooks = db["hooks"]
key_in_uses = db["key_in_uses"]
key_losts = db["key_losts"]
keys = db["keys"]
loans = db["loans"]
requests = db["requests"]
rooms = db["rooms"]
key_returns = db["key_returns"]
""" 
TODO: 
* employess
* buildings
* doors
* hooks 
* door_types
* rooms
* access
"""
# Employess
employees.delete_many({})
employees.create_index('employee_id', unique=True)
e1 = {'employee_id': 12345, 'name': 'john doe'}
e2 = {'employee_id': 14567, 'name': 'homer simpson'}
e3 = {'employee_id': 54321, 'name': 'spider man'}
e4 = {'employee_id': 86754, 'name': 'naruto'}
e5 = {'employee_id': 42069, 'name': 'yo mama'}
e6 = {'employee_id': 90909, 'name': 'your dad'}
employees.insert_many([e1,e2,e3,e4,e5,e6])


# hooks
hooks.delete_many({})
hooks.create_index('hook_id', unique=True)
h1 = {'hook_id' : 1}
h2 = {'hook_id' : 2}
h3 = {'hook_id' : 3}
h4 = {'hook_id' : 4}
h5 = {'hook_id' : 5}
h6 = {'hook_id' : 6}
h7 = {'hook_id' : 7}
hooks.insert_many([h1,h2,h3,h4,h5,h6,h7])

# keys
keys.delete_many({})
keys.create_index([("key_id", pymongo.ASCENDING), ("hook_id", pymongo.ASCENDING)], unique=True)
k1 = {'key_id': 11, 'hook_id': 1}
k2 = {'key_id': 12, 'hook_id': 2}
k3 = {'key_id': 13, 'hook_id': 3}
k4 = {'key_id': 1, 'hook_id': 4}
k5 = {'key_id': 2, 'hook_id': 5}
k6 = {'key_id': 3, 'hook_id': 6}
k7 = {'key_id': 5, 'hook_id': 7}
keys.insert_many([k1,k2,k3,k4,k5,k6,k7])

buildings
buildings.delete_many({})
buildings.create_index('building_name', unique=True)
b1 = {'building_name': 'ECS'}
b2 = {'building_name': 'VIV'}
b3 = {'building_name': 'ENGR 4'}
b4 = {'building_name': 'BIO'}
b5 = {'building_name': 'HUM'}
b6 = {'building_name': 'PSY'}
buildings.insert_many([b1,b2,b3,b4,b5,b6])

# doors types
door_types.delete_many({})
# door_types('door_type', unique=True)
dt1 = {'type': 'Front'}
dt2 = {'type': 'Back'}
dt3 = {'type': 'Right'}
door_types.insert_many([dt1,dt2,dt3])

# rooms
rooms.delete_many({})
rooms.create_index([("room_number", pymongo.ASCENDING),("building_name", pymongo.ASCENDING)], unique=True)
r1 = {'room_number': 450, 'building_name': 'ECS'}   
r2 = {'room_number': 121, 'building_name': 'VIV'} 
r3 = {'room_number': 323, 'building_name': 'ENGR'} 
r4 = {'room_number': 274, 'building_name': 'BIO'} 
r5 = {'room_number': 136, 'building_name': 'HUM'} 
r6 = {'room_number': 412, 'building_name': 'PSY'} 
r7 = {'room_number': 342, 'building_name': 'ECS'} 
r8 = {'room_number': 700, 'building_name': 'ECS'} 
r9 = {'room_number': 800, 'building_name': 'ECS'} 
rooms.insert_many([r1,r2,r3,r4,r5,r6,r7,r8,r9])


# doors
doors.delete_many({})
doors.create_index([('room_number', pymongo.ASCENDING), ('building_name', pymongo.ASCENDING), ('door_type', pymongo.ASCENDING)])
d1 = {'room_number': 450 , 'building_name': 'ECS', 'door_type': 'Front'}
d2 = {'room_number': 121 , 'building_name': 'VIV' , 'door_type': 'Back'}
d3 = {'room_number': 323 , 'building_name': 'ENGR 4' , 'door_type': 'Right'}
d4 = {'room_number': 274, 'building_name': 'BIO' , 'door_type': 'Right'}
d5 = {'room_number': 136, 'building_name': 'HUM', 'door_type': 'Front'}
d6 = {'room_number': 412, 'building_name': 'PSY', 'door_type': 'Back' }
d7 = {'room_number': 136, 'building_name': 'HUM', 'door_type': 'Back' }
d8 = {'room_number': 800, 'building_name': 'ECS', 'door_type': 'Front'}
d9 = {'room_number': 700, 'building_name': 'ECS', 'door_type': 'Back'}
doors.insert_many([d1,d2,d3,d4,d5,d6,d7,d8,d9])



#access
access.delete_many({})
access.create_index([('hook_id', pymongo.ASCENDING), ('room_number',pymongo.ASCENDING), ('building_name', pymongo.ASCENDING), ('door_type',pymongo.ASCENDING)], unique=True)
a1 = {'hook_id' : 1, 'room_number': 450 , 'building_name': 'ECS', 'door_type': 'Front'} 
a2 = {'hook_id' : 2, 'room_number': 121, 'building_name': 'VIV', 'door_type': 'Back'} 
a3 = {'hook_id' : 3, 'room_number': 323, 'building_name': 'ENGR 4', 'door_type': 'Right'} 
a4 = {'hook_id' : 4, 'room_number': 274, 'building_name': 'BIO', 'door_type': 'Right'} 
a5 = {'hook_id' : 5, 'room_number': 136, 'building_name': 'HUM', 'door_type': 'Front'} 
a6 = {'hook_id' : 6, 'room_number': 136, 'building_name': 'HUM', 'door_type': 'Back'} 
a7 = {'hook_id' : 7, 'room_number': 412, 'building_name': 'PSY', 'door_type': 'Back'} 
a8 = {'hook_id' : 4, 'room_number': 800, 'building_name': 'ECS', 'door_type': 'Front'} 
a9 = {'hook_id' : 2, 'room_number': 700, 'building_name': 'ECS', 'door_type': 'Back'} 
access.insert_many([a1,a2,a3,a4,a5,a6,a7,a8,a9])

# request
requests.delete_many({})
rq = {'employee_id': 12345, 'date_requested': '2022-10-10', 'room_number': 450, 'building_name': 'ECS'}
rq2 = {'employee_id': 54321, 'date_requested': '2023-12-10', 'room_number': 121, 'building_name': 'VIV'}
rq3 = {'employee_id': 14567, 'date_requested': '2022-01-23', 'room_number': 136, 'building_name': 'HUM'}
rq4 = {'employee_id': 86754, 'date_requested': '2019-10-31', 'room_number': 412, 'building_name': 'PSY'}
requests.insert_many([rq, rq2,rq3,rq4])

#loans 
loans.delete_many({})
l1 = {'key_id': 11,'employee_id': 12345, 'date_requested': '2022-10-10', 'room_number': 450, 'building_name': 'ECS'}
l2  = {'key_id': 1,'employee_id': 14567, 'date_requested': '2022-01-23', 'room_number': 136, 'building_name':  'HUM'}
loans.insert_many([l1,l2])
# loans.insert_one(l2)

#keys_in_use
key_in_uses.delete_many({})
kiu = {'loans_key_id' : 11, 'loans_employee_id': 12345, 'loans_room_number': 450, 'loans_building_name': 'ECS', 'loans_request_date': '2022-10-10'}
kiu2 = {'loans_key_id' : 1, 'loans_employee_id': 14567, 'loans_room_number': 450, 'loans_building_name': 'HUM', 'loans_request_date': '2022-01-23'}
key_in_uses.insert_one(kiu)
key_in_uses.insert_one(kiu2)

#key_returned
key_returns.delete_many({})
kr = {'loans_key_id' : 1, 'loans_employee_id': 14567, 'loans_room_number': 136, 'loans_building_name': 'HUM', 'loans_request_date': '2022-10-10', 'return_date': '2023-01-23'}
key_returns.insert_one(kr)

# key_lost


menu()



