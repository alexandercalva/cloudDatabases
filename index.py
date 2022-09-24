from firebase import firebase

firebase = firebase.FirebaseApplication("https://fir-python-ce049-default-rtdb.firebaseio.com/",None)

# Variables

datos = {
    'id': '1',
    'Name' : 'Alexander',
    'LastName': 'Calva',
    'Phone': '0983545654',
    'Mail': 'prueba@gmail.com',
    'Address': 'Urb. Limonar',
    'Job': 'Carpinter' 
}

# Add registers to Database(post)
ansPost = firebase.post('/tutorial_firebase/data_post',datos)

# Read data from firebase
ansGet = firebase.get('/tutorial_firebase/data_post', '')
print(ansGet)

#Edit data from firebase
firebase.put('/tutorial_firebase/data_post/-NCkPLmQatOI0hdefvLh', 'id', '2')

# Delete data from firebase
firebase.delete('/tutorial_firebase/data_post', '-NCkQKqjEs7SOWm3OSsx')