import requests

superhero = {'Captain America', 'Hulk', 'Thanos'}
url = 'https://akabab.github.io/superhero-api/api/all.json'
hero_stat = {}
all_superhero = requests.get(url)
for hero in all_superhero.json():
    if hero['name'] in superhero:
        hero_stat[f'{hero["name"]}'] = hero["powerstats"]["intelligence"]
print(f'Самый умный супер герой из предложенных: {list(sorted(hero_stat.items(), key=lambda item: -item[1]))[0][0]}')

