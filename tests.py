from firethon import Firebase, FirebaseConfig

config = FirebaseConfig(
    url='https://tuktuk-express-default-rtdb.asia-southeast1.firebasedatabase.app',
    path_to_service_account_file='firebase_service.json')

firebase = Firebase(config=config)

response = firebase.put('/1/new_orders.json', {'hello': 'hello'})
print(response.content)
