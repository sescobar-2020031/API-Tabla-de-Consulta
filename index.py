import json
from random import randint
from array import array
from webbrowser import get
from flask import Flask, render_template
import requests


url_api = 'https://pokeapi.co/api/v2/pokemon/'

app = Flask(__name__)

@app.route('/')
def main():
    nombres = []
    fotos = []
    numeroPoke = []
    tipo = []
    peso = []
    altura = []

    for i in range(0, 6):

        #Obtine un poquemon random
        result_0 = randint(1, 800)
        pokemon_name = str(result_0)
        numeroPoke.append(result_0)
        pokemon_data_url = url_api + pokemon_name
        data = get_pokemon_data(pokemon_data_url)

        #Obtiene una imagaen
        res = json.loads(requests.get(pokemon_data_url).text)
        image = res['sprites']
        image = image['front_default']
        fotos.append(image)

        #obtiene el nombre del pokemon
        nombre_pokemon = data.get("name")
        nombres.append(nombre_pokemon)

        #obtiene el tipo del pokemon
        pokemon_type = [types['type']['name'] for types in data['types']]
        tipo.append(", ".join(pokemon_type))

        #obtiene el peso del pokemon
        pokemon_peso = data.get("weight")
        peso.append(pokemon_peso)

        #obtiene la altura del pokemon
        pokemon_altura = data.get("height")
        altura.append(pokemon_altura)
    return render_template('index.html',len = len(nombres),  pokemon=nombres,
    imagen=fotos, no=numeroPoke, tipo = tipo, peso=peso, altura=altura)

#Obtiene un pokemon
def get_pokemon_data(url_pokemon=''):
    pokemon_data = {
        "name": '',
        "height": '',
        "types": '',
        "weight": '',

    }
    response = requests.get(url_pokemon)
    data = response.json()

    pokemon_data['name'] = data['name']
    pokemon_data['height'] = data['height']
    pokemon_data['types'] = data['types']
    pokemon_data['weight'] = data['weight']

    return pokemon_data


if __name__ == '__main__':
    app.run(debug=True)
