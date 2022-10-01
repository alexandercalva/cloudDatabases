#from typing_extensions import Self
from firebase import firebase
import random
import bcrypt 
import sys

firebase = firebase.FirebaseApplication("https://fir-python-ce049-default-rtdb.firebaseio.com/",None)

#class
class persona:
           
    # Enter information in each field in the database
    def IntroInfo(self):
        #idUser = input("Id: ")
        name = input("Name: ")
        lastname = input("Lastname: ")
        phone = input("Phone: ")
        mail = input("Mail: ")
        password = input("Password: ")
        address = input("Address: ")
        job = input("Job: ")
        experience = input("Experience: ")
        
        # Change the password in safe mode.
        passwd = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(passwd, salt)
        encoding = sys.getdefaultencoding()
       
        # Store all information in datos object
        datos = {
            'Id' : random.randint(1,10000),
            'Name' : name,
            'LastName': lastname,
            'Phone': phone,
            'Mail': mail,
            'Address': address,
            'Job': job,
            'Passsword': hashed.decode(encoding),
            'Experience': experience
        }
        idUserFb = datos['Id']
        idUserFb = str(idUserFb)
        ansPost = firebase.post('/tutorial_firebase/data_post', datos)
           
    # Read data from firebase
    def ShowData(self):
        ansGet = firebase.get('/tutorial_firebase/data_post', '')
        print(ansGet)

    #Edit data from firebase
    def EditData(self):
        idUserFirebase = input("Enter the user idFirebase:  ")
        keyDatabase = input("Enter the key to edit: ")
        valueDatabase = input("Enter the value to change: ")
        try:   
            firebase.put('/tutorial_firebase/data_post/' +idUserFirebase , keyDatabase, valueDatabase)
        except:
            print("Error. Please, enter the information correctly")
    
    # Delete data form firebase
    def DeleteData(self):
        idUserFirebase = input("Enter the user idFirebase:  ")
        try:
            firebase.delete('/tutorial_firebase/data_post',idUserFirebase)
            print("Information was deleted correctly")
        except:
             print("Error. Please, enter the information correctly")

# Menu 
def menu():
    opc = int(input("Menu \n" +
    "1. Register \n" + 
    "2. Show \n" + 
    "3. Update \n" + 
    "4. Delete \n" + 
    "5. Exit \n" +
    "Choose an option: \n"))
    
    return opc

def main(opcion):
    # Instance of persona class
    personaFirestore = persona()
    
    while opcion != 5:
       
        if opcion == 1:
            # Introduce information
            personaFirestore.IntroInfo()
        if opcion == 2:
            # Show all information
            personaFirestore.ShowData()
        if opcion == 3:
            # Edit user
            personaFirestore.EditData()
        if opcion == 4:
            # Delete data from firebase
            personaFirestore.DeleteData()
        opcion = menu()
opcion = menu()
main(opcion)


