import requests

headers = {
    "Content-Type": "application/json",
    "x-api-key": "DEMO-API-KEY"
}

requestOptions = {
    'method': 'GET',
    'headers': f'{headers}',
    'redirect': 'follow'
}

def get_cat():
    url = f'https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1", {requestOptions})'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# cat_image = get_cat()
# print(cat_image)
