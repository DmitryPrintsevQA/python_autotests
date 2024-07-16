import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ae66260bb2709bdd16ed55c14c77326a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "pokemon_id": "43728"
}

'''response =  requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)'''
'''
response =  requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)'''

response =  requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_create)
print(response.text)