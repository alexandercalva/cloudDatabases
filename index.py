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
        ansPost = firebase.post('/tutorial_firebase/data_post',datos)
        #return datos
    
    # Read data from firebase
    def ShowData(self):
        ansGet = firebase.get('/tutorial_firebase/data_post', '')
        print(ansGet)

    #Edit data from firebase
    def EditData(self):
        firebase.put('/tutorial_firebase/data_post/-NCkPLmQatOI0hdefvLh', 'id', '2')   

# Instance of persona class
personaFirestore = persona()

# Introduce information
personaFirestore.IntroInfo()
# Show all information
personaFirestore.ShowData()



# Delete data from firebase
#firebase.delete('/tutorial_firebase/data_post', '-NCkQKqjEs7SOWm3OSsx')