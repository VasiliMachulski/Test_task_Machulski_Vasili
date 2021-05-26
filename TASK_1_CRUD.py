import requests

add_new_pet = requests.post(url='https://petstore.swagger.io/v2/pet',
                            json={"id": 11042,
                                    "category": {"id": 0, "name": ""},
                                    "name": "Bill",
                                    "photoUrls": [""],
                                    "tags": [{"id": 0, "name": "white"}],
                                    "status": "available"})

read_pet = requests.get('https://petstore.swagger.io/v2/pet/11042')
print(read_pet.text)

update_pet = requests.put('https://petstore.swagger.io/v2/pet',
                          json={"id": 11042,
                                "category": {"id": 0, "name": "new"},
                                "name": "Bill_new",
                                "photoUrls": [""],
                                "tags": [{"id": 0, "name": "white-red"}],
                                "status": "available"})
print(update_pet.text)

delete_pet = requests.delete('https://petstore.swagger.io/v2/pet/11042')
print(delete_pet)

