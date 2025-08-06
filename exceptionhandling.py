import mysql.connector
def update_people(people_id, new_name):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "roottoor",
        database = "yashu_ece"
    )
    
    mycursor = mydb.cursor()
    sql = "UPDATE people SET name = %s, WHERE id = %S"
    val = (new_name, people_id)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    mydb.close()
    print(mycursor.rowcount,"record inserted.")
    
id = input("enter people ID ")
name = input("enter the name ")
update_people(id, name)