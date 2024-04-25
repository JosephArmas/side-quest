"""This "application" is a demonstration using SQLAlchemy to create a small number of tables and populate
them.  Not evey possible use case for SQLAlchemy is explored in this demonstration, only those which are
required for this particular demonstration.

Technical Note: Be sure to have psycopg2 or whichever package you need to support whichever
relational dialect that you are using installed.  No imports call attention to the database
connectivity library, that is referenced when you run your application."""

# Think of Session and engine like global variables.  A little ghetto, but the only
# other alternative would have been a singleton design pattern.
from pprint import pprint

import sqlalchemy.sql.functions

# the db_connection.py code sets up some connection objects for us, almost like Java class variables
# that get loaded up at run time.  This statement builds the Session class and the engine object
# that we will use for interacting with the database.
from db_connection import Session, engine
# orm_base defines the Base class on which we build all of our Python classes and in so doing,
# stipulates that the schema that we're using is 'demo'.  Once that's established, any class
# that uses Base as its supertype will show up in the postgres.demo schema.
from orm_base import metadata
import logging
from sqlalchemy import Column, String, Integer, Float, UniqueConstraint, \
    Identity, ForeignKey, distinct, bindparam
from sqlalchemy.orm import relationship, backref
from orm_base import Base


from Building import Building
from Room import Room
from Hook import Hook
from Key import Key

from Employee import Employee
from Request import Request
from Loan import Loan
from Key_In_Use import Key_In_Use
from Key_Lost import Key_Lost
from Key_Return import Key_Return
from Door_Type import Door_Type
from Door import Door
from Access import Access


if __name__ == '__main__':
    def menu(): 
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
        print("11. Quit")
        while True:
            select = int(input("Enter Choice: "))
            try:
                if select == 1:
                    keys = sess.query(Key)
                    print("Key table: ")
                    print("hook_id, key_id")
                    for key in keys:
                        print(key.hook_id, key.key_id)
                    new_key = CreateKey()
                    print("new key being added:", new_key)
                    sess.add(new_key)
                    sess.commit()
                    print("Key table updated: ")
                    for key in keys:
                        # print("with insert: ")
                        print(key.hook_id, key.key_id)
                elif select == 2:
                    rooms = sess.query(Room)
                    employees = sess.query(Employee)
                    print("rooms: ") 
                    for room in rooms:
                        print(room.room_number, room.building_name)
                    print("employees: ")
                    for employee in employees:
                        print(employee.employee_id)
                    rq = ReqAccess()
                    print("your request: ", rq)
                    sess.add(rq)
                    sess.commit()
                    requests = sess.query(Request)
                    print("Request table updated: ")
                    for request in requests:
                        print(request.building_name, request.room_number, request.employee_id, request.date_requested)
                elif select == 3:
                    requests = sess.query(Request)
                    print("Request table: ")
                    for r in requests:
                        print(r.employee_id, r.date_requested, r.room_number, r.building_name)
                    loan = IssueKey()
                    sess.add(loan)
                    sess.commit()
                    loans = sess.query(Loan)
                    print("Loan Table updated: ")
                    for l in loans:
                        print(l.key_id, l.employee_id, l.date_requested, l.room_number, l.building_name)
                elif select == 4:
                    print("loans table: ")
                    loans = sess.query(Loan)
                    for loan in loans:
                        print(loan.employee_id, loan.key_id, loan.date_requested, loan.room_number, loan.building_name)
                    lk = LostKey()
                    sess.add(lk)
                    sess.commit()
                    lost_keys = sess.query(Key_Lost)
                    print("table of lost keys: ")
                    for key in lost_keys:
                        print("lost keys: ")
                        print(key.lost_report_date, key.loans_key_id, key.loans_employee_id, key.loans_room_number, key.loans_building_name, key.loans_request_date)
                elif select == 5:
                    # TODO display all rooms an employee can enter given the keys they already have
                    enter = sess.query(Key_In_Use)
                    for e in enter:
                        print(e.loans_employee_id,e.loans_room_number,e.loans_building_name)

                elif select == 6:
                    # TODO delete a key
                    keys = sess.query(Key)
                    print("Key table: ")
                    for k in keys:
                        print(k.hook_id,k.key_id)
                    a = DelKey()
                    print("deleting key:",a.key_id)
                    print("Key table updated: ")
                    for j in keys:
                        print(j.hook_id, j.key_id)

                elif select == 7:
                    # TODO delete a employee 
                    emps = sess.query(Employee)
                    print("Employee id table: ")
                    for e in emps:
                        print(e.employee_id)
                    a = DelEmp()
                    print("Deleting employee id:", a.employee_id)
                    print('Employee id table updated: ')
                    for u in emps:
                        print(u.employee_id)
                elif select == 8:
                    # TODO add a new door that can be opened by an exisiting hook
                    door_t = sess.query(Door_Type)
                    print("existing door type:")
                    for d in door_t:
                        print(d.type)
                    user_input = input("Enter new door: ")
                    dr: Door_Type = Door_Type(type=user_input)
                    sess.add(dr)
                    sess.commit()
                    dewr = sess.query(Door)
                    for do in dewr:
                        print(do.room_number, do.building_name, do.door_type)
                    d_room = int(input('Enter room number: '))
                    d_building = input('Enter building name: ')
                    d1: Door = Door(room_number=d_room, building_name=d_building, door_type=user_input)
                    sess.add(d1)
                    sess.commit()
                    acc = sess.query(Access)
                    for j in acc:
                        print(j.hook_id, j.room_number, j.building_name, j.door_type)
                    hook_sel = int(input('Enter hook id: '))
                    building = input("Enter building name: ")
                    room = int(input('Enter room number: '))
                    new_access: Access = Access(hook_id=hook_sel,room_number=room,building_name=building,door_type=user_input)
                    sess.add(new_access)
                    sess.commit()
                    for new in acc:
                        print(new.hook_id, new.room_number, new.building_name, new.door_type)
                elif select == 9:
                    # TODO update an access request to move to a new employee
                    req = sess.query(Request)
                    print("Request table: ")
                    for r in req:
                        print(r.employee_id, r.date_requested, r.room_number, r.building_name)
                    NewReq()
                    print("Request table updated: ")
                    for j in req:
                        print(j.employee_id, j.date_requested, j.room_number, j.building_name)
                elif select == 10:
                    # TODO display all employees who can get into a room 
                    print("Employees who can get into a room: ")
                    in_use = sess.query(Key_In_Use)
                    for i in in_use:
                        print(i.loans_employee_id)
                elif select == 11:
                    break
            except ValueError:
                print('Invalid choice. 1-10')

    def CreateKey():
        h = int(input("enter hook id: "))
        x = int(input("enter new key: "))
        k:  Key = Key(hook_id=h, key_id=x )
        return k 
    def ReqAccess():
        b = input('request building name: ')
        r = input('request room: ')
        e = input('employee number: ')
        d = input('input date: ')
        rq: Request = Request(building_name=b, room_number=r, employee_id=e, date_requested=d)
        return rq
    def LostKey():
        d = input('report lost date: ')
        k = int(input('insert key id: '))
        e = input('employee id: ')
        b = input('building name: ')
        rd = input('date requested: ')
        r = int(input('room number: '))
        lk: Key_Lost = Key_Lost(lost_report_date=d, loans_key_id=k, loans_employee_id=e, loans_building_name=b, loans_room_number=r, loans_request_date=rd )
        return lk
    def IssueKey():
        e = int(input('enter employee id: '))
        d = input('date requested: ')
        r = int(input('room number: '))
        b = input('building name: ')
        holder = sess.query(Access)
        for i in holder:
            if i.room_number == r:
                hk = i.hook_id
        hooks = sess.query(Hook)
        keys = sess.query(Key)
        for j in hooks:
            if j.hook_id == hk:
                hk_key = j.hook_id
                for k in keys:
                    if k.hook_id == hk_key:
                        key = k.key_id
                        lk: Loan = Loan(key_id=key, employee_id=e, date_requested=d, room_number=r, building_name=b)
        return lk
    def DelKey():
        d = int(input("enter key id to delete: "))
        key = sess.query(Key)
        for i in key:
            if i.key_id == d:
                a = i
                sess.delete(i)
                sess.commit()
        return a
    def DelEmp():
        d = int(input('enter employee id to delete: '))
        emps = sess.query(Employee)
        for e in emps:
            if e.employee_id == d:
                a = e
                sess.delete(e)
                sess.commit()
        return a
    def NewReq():
        o = int(input("replace which employee id? "))
        e = int(input("enter new employee id: "))
        new_emp: Employee  = Employee(employee_id=e)
        sess.add(new_emp)
        sess.commit()
        req = sess.query(Request)
        for i in req:
            if i.employee_id == o:
                i.employee_id = e
                sess.commit()
    
    def Available():
        in_use = sess.query(Key_In_Use)
        for i in in_use:
            print(i.loans_employee_id, i.loans_room_number, i.loans_building_name)










    logging.basicConfig()
    # use the logging factory to create our first logger.
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # use the logging factory to create our second logger.
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    metadata.drop_all(bind=engine)  # start with a clean slate while in development

    # Create whatever tables are called for by our "Entity" classes.  The simple fact that
    # your classes that are subtypes of Base have been loaded by Python has populated
    # the metadata object with their definition.  So now we tell SQLAlchemy to create
    # those tables for us.
    metadata.create_all(bind=engine)


    # input for employees
    e1: Employee = Employee (employee_id = 12345)
    e2: Employee = Employee (employee_id = 54321)
    e3: Employee = Employee (employee_id = 14567)
    e4: Employee = Employee (employee_id = 86754)
    e5: Employee = Employee (employee_id = 42069)
    e6: Employee = Employee (employee_id = 55555)
    e7: Employee = Employee(employee_id=90909)

    """ working -- tested
    e1: Employee = Employee (employee_id = 12345)
    b1: Building = Building(building_name = 'ECS')
    r1: Room = Room(room_number=417, building_name='ECS')
    rq: Request = Request(employee_id=12345, date_requested = '2022-11-11', room_number=417, building_name='ECS')
    h1: Hook = Hook(hook_id= 1)
    k1: Key = Key(key_id = 11, hook_id = 1)
    l1: Loan = Loan(key_id=11, employee_id=12345, date_requested='2022-11-11', room_number=417, building_name='ECS')
    kin1: Key_In_Use = Key_In_Use(loans_key_id=11,loans_employee_id=12345,loans_room_number=417,loans_building_name='ECS', loans_request_date='2022-11-11')
    lk1: Key_Lost = Key_Lost(lost_report_date='2022-12-11', loans_request_date='2022-11-11', loans_building_name='ECS', loans_room_number=417, loans_employee_id=12345, loans_key_id=11)
    kr1: Key_Return = Key_Return(return_date = '2023-01-08', loans_key_id=11, loans_employee_id=12345, loans_building_name='ECS', loans_room_number=417, loans_request_date='2022-11-11')
    dt1: Door_Type = Door_Type(type='front')
    d1: Door = Door(building_name='ECS', room_number=417,door_type='front')
    a1: Access = Access(hook_id=1, room_number=417,building_name='ECS', door_type='front')
    """




    #input for hooks
    h1: Hook = Hook(hook_id = 1)
    h2: Hook = Hook(hook_id = 2)
    h3: Hook = Hook(hook_id = 3)
    h4: Hook = Hook(hook_id = 4)
    h5: Hook = Hook(hook_id = 5)
    h6: Hook = Hook(hook_id = 6)
    h7: Hook = Hook(hook_id = 7)

    #input for keys

    k1: Key = Key(key_id = 11, hook_id = 1)
    k2: Key = Key(key_id = 12, hook_id = 2)
    k3: Key = Key(key_id = 13, hook_id = 3)
    k4: Key = Key(key_id = 1, hook_id = 4)
    k5: Key = Key(key_id = 2, hook_id = 5)
    k6: Key = Key(key_id = 3, hook_id = 6)
    k7: Key = Key(key_id = 5, hook_id = 7)


    #this key has a bad hook_id and SQLAlchemy is able to not add it to the table
    #this will break main.py and you cannot compile if you sess.add(k7)
    # k7: keys = keys(key_id = 3, hook_id = 16)

    #input for buildings
    b1: Building = Building(building_name = 'ECS')
    b2: Building = Building(building_name = 'VIV')
    b3: Building = Building(building_name = 'ENGR 4')
    b4: Building = Building(building_name = 'BIO')
    b5: Building = Building(building_name = 'HUM')
    b6: Building = Building(building_name = 'PSY')



    #input for rooms
    r1: Room = Room(room_number = 450, building_name = 'ECS')
    r2: Room = Room(room_number = 121, building_name = 'VIV')
    r3: Room = Room(room_number = 323, building_name = 'ENGR 4')
    r4: Room = Room(room_number = 274, building_name = 'BIO')
    r5: Room = Room(room_number = 136, building_name = 'HUM')
    r6: Room = Room(room_number = 412, building_name = 'PSY')
    r7: Room = Room(room_number = 342, building_name = 'ECS')
    r8: Room = Room(room_number = 700, building_name = 'ECS')
    r9: Room = Room(room_number = 800, building_name = 'ECS')

    #inputs for door_types
    dt1: Door_Type = Door_Type(type = 'Front')
    dt2: Door_Type = Door_Type(type = 'Back')
    # dt3: Door_Type = Door_Type(type = 'Left')
    dt4: Door_Type = Door_Type(type = 'Right')



    # input doors
    d1: Door = Door(room_number = 450, building_name = 'ECS', door_type = 'Front')
    d2: Door = Door(room_number = 121, building_name = 'VIV', door_type = 'Back')
    d3: Door = Door(room_number = 323, building_name = 'ENGR 4', door_type = 'Right')
    d4: Door = Door(room_number = 274, building_name = 'BIO', door_type = 'Right')
    d5: Door = Door(room_number = 136, building_name = 'HUM', door_type = 'Front')
    d6: Door = Door(room_number = 412, building_name = 'PSY', door_type = 'Back')
    d7: Door = Door(room_number = 136, building_name = 'HUM', door_type = 'Back')
    d8: Door = Door(room_number = 800, building_name = 'ECS', door_type = 'Front')
    d9: Door = Door(room_number = 700, building_name = 'ECS', door_type = 'Back')

    # input request
    rq1: Request = Request(employee_id=12345, date_requested='2022-10-10', room_number=450, building_name='ECS')
    rq2: Request = Request(employee_id=54321, date_requested='2023-12-10', room_number=121, building_name='VIV')
    rq3: Request = Request(employee_id=14567, date_requested='2021-1-23', room_number=136, building_name='HUM')
    rq4: Request = Request(employee_id=86754, date_requested='2012-10-31', room_number=412, building_name='PSY')
    rq5: Request = Request(employee_id=42069, date_requested='2010-11-10', room_number=274, building_name='BIO')
    rq6: Request = Request(employee_id=55555, date_requested='2024-2-24', room_number=323, building_name='ENGR 4')
    rq7: Request = Request(employee_id=55555, date_requested='2024-2-25', room_number=323, building_name='ENGR 4')

    # input loans
    l1: Loan = Loan(employee_id=12345, date_requested='2022-10-10', room_number=450, building_name='ECS', key_id=11)
    l2: Loan = Loan(employee_id=54321, date_requested='2023-12-10', room_number=121, building_name='VIV', key_id=12)
    l3: Loan = Loan(employee_id=14567, date_requested='2021-1-23', room_number=136, building_name='HUM', key_id=1)
    l4: Loan = Loan(employee_id=86754, date_requested='2012-10-31', room_number=412, building_name='PSY', key_id=2)
    l5: Loan = Loan(employee_id=42069, date_requested='2010-11-10', room_number=274, building_name='BIO', key_id=13)
    l6: Loan = Loan(employee_id=55555, date_requested='2024-2-24', room_number=323, building_name='ENGR 4', key_id=3)



    # input Keys in use
    # kin1: Key_In_Use = Key_In_Use(loans_key_id=11, loans_employee_id=12345, loans_building_name='ECS', loans_room_number=450, loans_request_date='2022-10-10')
    kin2: Key_In_Use = Key_In_Use(loans_key_id=12, loans_employee_id=54321, loans_building_name='VIV', loans_room_number=121, loans_request_date='2023-12-10')
    kin3: Key_In_Use = Key_In_Use(loans_key_id=1, loans_employee_id=14567 ,loans_building_name='HUM', loans_room_number=136, loans_request_date='2021-1-23')
    
    # # input keys lost
    kl1: Key_Lost = Key_Lost(loans_key_id=2, loans_employee_id=86754 ,loans_building_name='PSY', loans_room_number=412, loans_request_date='2012-10-31', lost_report_date='2012-12-14')

    # # input keys returned
    kr1: Key_Return = Key_Return(loans_key_id=13, loans_employee_id=42069 ,loans_building_name='BIO', loans_room_number=274, loans_request_date='2010-11-10', return_date='2010-12-20')
    # kr2: Key_Return = Key_Return(loans_key_id=3, loans_employee_id=55555 ,loans_building_name='ENGR 4', loans_room_number=323, loans_request_date='2024-2-24', return_date='2024-6-14')

    # # input access
    a1: Access = Access(hook_id=1, room_number=450, building_name='ECS', door_type='Front')
    a2: Access = Access(hook_id=2, room_number=121, building_name='VIV', door_type='Back')
    a3: Access = Access(hook_id=3, room_number=323, building_name='ENGR 4', door_type='Right')
    a4: Access = Access(hook_id=4, room_number=274, building_name='BIO', door_type='Right')
    a5: Access = Access(hook_id=5, room_number=136, building_name='HUM', door_type='Front')
    a6: Access = Access(hook_id=6, room_number=136, building_name='HUM', door_type='Back')
    a7: Access = Access(hook_id=7, room_number=412, building_name='PSY', door_type='Back')
    a8: Access = Access(hook_id=4, room_number=800, building_name='ECS', door_type='Front')
    a9: Access = Access(hook_id=2, room_number= 700, building_name='ECS', door_type='Back')











    # Do our database work within a context.  This makes sure that the session gets closed
    # at the end of the with, much like what it would be like if you used a with to open a file.
    # This way, we do not have memory leaks.
    with Session() as sess:
        sess.begin()
        print("Inside the session, woo hoo.")
        """  working
        sess.add(e1)
        sess.add(b1)
        sess.add(r1)
        sess.add(h1)
        sess.add(dt1)
        sess.commit()
        sess.add(d1)
        sess.add(k1)
        sess.add(rq)
        sess.commit()
        sess.add(a1)
        sess.add(l1)
        sess.commit()
        sess.add(kin1)
        sess.add(lk1)
        sess.add(kr1)
        sess.commit()
        """ 
        # adding the employees
        sess.add(e1)
        sess.add(e3)
        sess.add(e2)
        sess.add(e4)
        sess.add(e5)
        sess.add(e6)
        sess.add(e7)


        #adding the hooks
        sess.add(h1)
        sess.add(h2)
        sess.add(h3)
        sess.add(h4)
        sess.add(h5)
        sess.add(h6)
        sess.add(h7)


        #adding the keys
        sess.add(k1)
        sess.add(k2)
        sess.add(k3)
        sess.add(k4)
        sess.add(k5)
        sess.add(k6)
        sess.add(k7)
        sess.commit()


        #adding buildings
        sess.add(b1)
        sess.add(b2)
        sess.add(b3)
        sess.add(b4)
        sess.add(b5)
        sess.add(b6)


        #adding rooms
        sess.add(r1)
        sess.add(r2)
        sess.add(r3)
        sess.add(r4)
        sess.add(r5)
        sess.add(r6)
        sess.add(r7)
        sess.add(r8)
        sess.add(r9)

        #adding door types
        sess.add(dt1)
        sess.add(dt2)
        # sess.add(dt3)
        sess.add(dt4)
        sess.commit()


        #adding doors
        sess.add(d1)
        sess.add(d2)
        sess.add(d3)
        sess.add(d4)
        sess.add(d5)
        sess.add(d6)
        sess.add(d7)
        sess.add(d8)
        sess.add(d9)
        sess.commit()


        # adding request
        sess.add(rq1)
        sess.add(rq2)
        sess.add(rq3)
        sess.add(rq4)
        sess.add(rq5)
        sess.add(rq6)
        sess.add(rq7)
        sess.commit()

        # adding loans
        # sess.add(l1)
        sess.add(l2)
        sess.add(l3)
        # sess.add(l4)
        sess.add(l5)
        # sess.add(l6)
        sess.commit()

        #adding keys in use
        # sess.add(kin1)
        sess.add(kin2)
        sess.add(kin3)
        sess.commit()

        # adding keys lost
        # sess.add(kl1)
        # sess.commit()
        
        # adding key returned
        sess.add(kr1)
        # sess.add(kr2)
        sess.commit()

        # adding access
        sess.add(a1)
        sess.add(a2)
        sess.add(a3)
        sess.add(a4)
        sess.add(a5)
        sess.add(a6)
        sess.add(a7)
        sess.add(a8)
        sess.add(a9)
        sess.commit()

        menu()






        # Hopefully this means that SQLAlchemy will perform the insert into movies_genres for me.
        # sess.commit()

    print("Exiting normally.")