from Face_recognition import face_unlock
from Listen_Speak import Speak_en
# FOR FACE UNLOCK 
def face():
    # Call the face_unlock function to check if the face is recognized
    result = face_unlock()

    # Check the result
    if result:
        print("Face recognized. Welcome Rishi Sir !")
        Speak_en("Face recognized. Welcome Rishi Sir !")
        return True
        
    else:
        print("Face not recognized. Access denied.")
        Speak_en("Face not recognized. Access denied.")
        return False
# FOR PASSWORD UNLOCK  
expected_password='qwerty@123'       
def password():
    entered_password=input("Enter the password : ")
    if expected_password==entered_password:
        print("Welcome Rishi Sir!")
        Speak_en("Welcome Rishi Sir!")
        return True
    else:
        print("Wrong Password. Access denied")
        Speak_en("Wrong Password. Access denied")
        return False

def unlock_sys():
    print("Select the method to unlock the bot :\n1. Face UNLOCK\n2. Password UNLOCK")
    Speak_en("Select the method to unlock the bot")
    ip=input("Enter 1 for Face & 2 for Password : ")
    if ip=='1':
        return face()

    elif ip=='2':
        return password()
    else:
        print("Invalid Input!")
        return False
