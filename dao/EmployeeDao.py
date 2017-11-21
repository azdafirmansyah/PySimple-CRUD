'''
Created on 8 Nov 2017

@author: DEV-SYB-AF
'''

from utils import DBUtils

def do_insert(first_name, last_name, age, sex, income):
    try:
        db = DBUtils.db_connect()
        cursor = db.cursor()
        
        query = "insert into employee values(%s,%s,%s,%s,%s)"
        cursor.execute(query, (first_name, last_name, age, sex, income))
        
        db.commit()
        print("insert success")
    except TypeError as e:
        db.rollback()
        print("insert failed, do rollback", e)
    finally:
        db.close()
        print("Insert Process Done")
    
def do_update(first_name, age):
    try:
        db = DBUtils.db_connect()
        cursor = db.cursor()
        
        #query = "Update employee set age = "+age+ " where first_name= %s"
        #cursor.execute(query, age)
        query = "update employee set age = %s where first_name = %s"
        param = (age, first_name, "azda")
        cursor.execute(query, param)
        
        db.commit()
        print("update success")
    except TypeError as e:     
        db.rollback()
        print("update failed, do rollback", e)
    finally:
        db.close()
        print("Update Process Done")
        
def do_delete(first_name):
    try:
        db = DBUtils.db_connect()
        cursor = db.cursor()
        
        query = "delete from employee where username = %s"
        cursor.execute(query, first_name)
        
        db.commit()
        print("delete success")
    except TypeError as e:
        db.rollback()
        print("delete failed, do rollback", e)
    finally:
        db.close()
        print("Delete Process Done")
        
def do_search():
    try:        
        db = DBUtils.db_connect()
        cursor = db.cursor()
        
        query = "select * from employee"
        cursor.execute(query)
        
        result = cursor.fetchall()
        count = 0
        for i in result:
            count += 1
            print("Data ke : ",count)
            print("First Name : ", i[0])
            print("Last Name : ", i[1])
            print("Age : ", i[2])
            print("Sex : ", i[3])
            print("Income : ", i[4])
            print("-----------------")
    except TypeError as e:
        print("searc failed ", e)
    finally:
        db.close()