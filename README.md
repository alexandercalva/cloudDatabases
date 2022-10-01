# Overview

Program to perform a CRUD in Firebase Firestore using the Python programming language.

First the connection between Firebase and Python was created. For this it was necessary to create an account in Firebase with a Gmail email. Next, a real-time database was created in Firestore. This entire process was free. Second, a program was developed to register users with 9 fields, which were name, lastname, phone, mail, address, job, password, and experience. Third, a random id was created for each user to avoid duplication in this field. To achieve all this, necessary methods and libraries were used. Finally, a menu was created where the user can choose which option they want to do between register, search, update, or delete within the database. One of the main challenges was encrypting the password entered in the registry. It was achieved using the library called bcrypt.

The purpose of writing this software was to discover the ease with which a cloud database can be used with Python. It is true that it was done at the console level, but with this program the capacity and efficiency of using a database in real time is demonstrated.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

Firebase in Realtime Database with firestore

I used variables within a class with an object as main structure.


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

# Development Environment

I used the following tools for this project:
* Visual Studio Code
* Python
* Firebase

Libraries used:
* firebase
* random
* bcrypt
* sys
# Useful Websites

List of websites that I found helpful in this project
* [Stackoverflow - firebase](https://stackoverflow.com/questions/52133031/receiving-async-error-when-trying-to-import-the-firebase-package)
* [Stackoverflow - github ](https://stackoverflow.com/questions/51817479/vscode-please-clean-your-repository-working-tree-before-checkout)
* [Python diario](https://pythondiario.com/2017/09/algoritmos-hash-criptografia-con-python.html?amp=1)
* [Geeksforgeeks](https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/)
# Future Work

* Improve password entry for a user.
* Perform a specific query in the database
* Perform an authentication from console in Python

