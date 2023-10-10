import requests
token = 'aa9fa3a5712c2353926d5b9aee70fa66'
host = 'https://api.pokemonbattle.me:9104'

response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Purrloin",
    "photo": "https://dolnikov.ru/pokemons/albums/509.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})

print(response_add_pokemon.text)

'''responce_change = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "12278",
    "name": "PurrloinAAA",
    "photo": "https://dolnikov.ru/pokemons/albums/510.png"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : 
              token } )

print(responce_change.text)'''

'''responce_gacha = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "12278"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : 
              token } )

print(responce_gacha.text)'''