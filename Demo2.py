from firebase import firebase
firebase = firebase.FirebaseApplication('https://atom940414.firebaseio.com', None)
result =firebase.patch('/users', {3:'anita'})
print(result)