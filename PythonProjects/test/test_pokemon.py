import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'ae66260bb2709bdd16ed55c14c77326a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '5551'

def test_status_code():
     response = requests.get (url=f'{URL}/pokemons', params= {TRAINER_ID : 'TRAINER_ID'})
     assert response.status_code == 404

