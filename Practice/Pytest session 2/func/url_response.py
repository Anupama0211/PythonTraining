import requests

def get_response():
    response = requests.get('https://httpbin.org/json')
    if response.status_code == 200:
        return response.json()['slideshow']

# {'author': 'Yours Truly', 'date': 'date of publication', 'slides': [{'title': 'Wake up to WonderWidgets!', 'type': 'all'}, {'items': ['Why <em>WonderWidgets</em> are great', 'Who <em>buys</em> WonderWidgets'], 'title': 'Overview', 'type': 'all'}], 'title': 'Sample Slide Show'}
