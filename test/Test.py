'''
Created on 8 Nov 2017

@author: DEV-SYB-AF
'''
from utils import Constant
from utils import DBUtils

print(Constant.CONFIG_PATH)

db = DBUtils.db_connect()
#try:
cursor = db.cursor()
    
#insert
#query = "insert into employee values(%s,%s,%s,%s,%s)"
#cursor.execute(query,(1,2,3,4,5))
#db.commit()

#select
#query = "select * from employee where income > '%s'"
#cursor.execute(query,300)
#result = cursor.fetchall()
#for row in result:
#    print(row[0],row[1],row[2],row[3],row[4])

#update
#query = "update employee set age = 100 where first_name = %s"
#cursor.execute(query, "azda")
#db.commit()

#delete
query = "delete from employee where first_name = %s"
cursor.execute(query,"1")
db.commit()

print("success")
db.close()
#except:     
    #
    #print()