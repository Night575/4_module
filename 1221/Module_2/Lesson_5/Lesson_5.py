import requests

response = requests.get('https://swapi.dev/api/')
starhips_url = response.json()['starships']

response = requests.get(starhips_url)
print(response.json())

starhips_list = []

for i in range(1, 6):
    detail_starships_speed_url = f'{starhips_url}/{i}'
    response = requests.get(detail_starships_speed_url)

    data = response.json()

    data['max_atmosphering_speed'] = int(data['max_atmosphering_speed'])

    starhips_list.append(data)

max_starhips_speed = 0
for starship in starhips_list:
    if starship['max_atmosphering_speed'] > max_starhips_speed:
        max_starhips_speed = starship['max_atmosphering_speed']

print(max_starhips_speed)