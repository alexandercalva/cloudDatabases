#from typing_extensions import Self
from firebase import firebase

firebase = firebase.FirebaseApplication("https://fir-python-ce049-default-rtdb.firebaseio.com/",None)

#class

class persona:
    def __init__(self, name, lastname, phone, mail, password, address, job):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.mail = mail
        self.password = password
        self.address = address
        self.job = job
        

    def __str__(self):
        return 'Name: {}\nLastname: {}\nPhone: {}\nMail: {}\naddress: {}\nJob: {}'.format(self.name, self.lastname, self.phone, self.mail, self.address, self.job)
    
    def IntroInfo(self):
        self.name = input("Name: ")
        self.lastname = input("Lastname: ")
        self.phone = input("Phone: ")
        self.mail = input("Mail: ")
        self.password = input("Password: ")
        self.address = input("Address: ")
        self.Job = input("Job: ")

        datos = {
            'Name' : self.name,
            'LastName': self.lastname,
            'Phone': self.phone,
            'Mail': self.mail,
            'Address': self.address,
            'Job': self.job,
            'Passsword': self.password 
        }
        return datos

personaF = persona("Alex", "Calva", 983880592, "correo@gmail.com", "hola","urba", "developer")
ansPost = firebase.post('/tutorial_firebase/data_post',personaF.IntroInfo())
#print(personaF)
# Add registers to Database(post)


# Read data from firebase
ansGet = firebase.get('/tutorial_firebase/data_post', '')
print(ansGet)

#Edit data from firebase
#firebase.put('/tutorial_firebase/data_post/-NCkPLmQatOI0hdefvLh', 'id', '2')

# Delete data from firebase
#firebase.delete('/tutorial_firebase/data_post', '-NCkQKqjEs7SOWm3OSsx')