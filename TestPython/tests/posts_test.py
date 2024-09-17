import requests

def test_get_all_albums() -> None:
    url =  requests.get("https://jsonplaceholder.typicode.com/albums",timeout= 5) 
    assert url.status_code == 200
    
def test_get_all_album() -> None:
    url =  requests.get("https://jsonplaceholder.typicode.com/albums", timeout=5)
    album = url.json()
    title_content = [album["title"] for album in album]
    assert 'quidem molestiae enim' in title_content
    
def test_create_post() -> None:
    payload = {
         "userId": 1,
         "id": 1,
         "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
         "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    headers = {
        "accept": "application/json"
    }
    url = requests.post("https://jsonplaceholder.typicode.com/posts",json=payload,headers=headers, timeout=10)
    assert url.status_code == 201