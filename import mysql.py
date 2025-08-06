import mysql.connector

def update_people(people_id, new_name,password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="yashu_ece"
    )

    mycursor = mydb.cursor()
    
    # Fixed SQL statement
    sql = "UPDATE people SET name = %s,password = %s WHERE id = %s"
    val = (new_name, password, people_id)
    
    mycursor.execute(sql, val)
    mydb.commit()
    
    print(mycursor.rowcount, "record(s) updated.")
    
    mycursor.close()
    mydb.close()

# Corrected input prompts
id = input("Enter person ID: ")
name = input("Enter the new name: ")
password = input("enter new password")
update_people(id,name,password)
