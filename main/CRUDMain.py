'''
Created on 7 Nov 2017

@author: DEV-SYB-AF
'''
import dao.EmployeeDao as employee

def run():
    while True:
        print("Input pilihan Anda \n1.Insert Data\n2.Update Data\n3.Delete Data\n4.Lihat Data\n5.Keluar")
        list_input_data = [1,2,3,4]
        input_data = input("Pilihan yang anda pilih :")
        try:
            x = int(input_data)
            if x == 1:
                #insert
                first_name = input("Nama Awal :")
                last_name = input("Nama Akhir :")
                age = input("Usia :")
                gender = input("Jenis Kelamin :")
                income = input("Income :")
                
                employee.do_insert(first_name, last_name, age, gender, income)
                
            elif x == 2:
                #update
                first_name = input("Nama Awal :")
                age = input("Usia yang ingin di rubah :")
                
                employee.do_update(first_name, age)
                
            elif x == 3:
                #delete
                first_name = input("Nama Awal :")
                employee.do_delete(first_name)
                
            elif x == 4:
                #search
                employee.do_search()
            elif x == 5:
                print("See you")
                break
        except:
            print("\nAnda Memasukkan Nomor Yang Salah")
        finally:    
            print("\n----")

if __name__ == '__main__':
    run()

#load db config
'''
db = DBUtils.db_connect()
cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()
print(data)
    
db.close()    
#print(a.get('db_host'), a.get('db_username'))
''' 
'''
db = pymysql.connect(db_host, db_username, db_password, db_name)

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()
print(data)

db.close()
'''


