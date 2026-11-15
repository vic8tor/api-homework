import requests

def main():
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
        posts = response.json()

        for post in posts[:5]:
            print(f"Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
            print("---")

    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")



main()