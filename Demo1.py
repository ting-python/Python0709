from firebase import firebase
firebase = firebase.FirebaseApplication('https://atom940414.firebaseio.com', None)
result =firebase.get('/users', 2)
print(result)