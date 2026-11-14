import requests

def main():
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
        posts = response.json()

    for i in posts:
        print(f"Post #i")

