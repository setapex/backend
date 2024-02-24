import httpx

class MicroserviceClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_items(self, user_token):
        headers = {'Authorization': f'Bearer {user_token}'}
        with httpx.Client() as client:
            response = client.get(f'{self.base_url}/get_items/', headers=headers)
            response.raise_for_status()
            return response.json()

    def get_item_by_id(self, user_token, item_id):
        headers = {'Authorization': f'Bearer {user_token}'}
        with httpx.Client() as client:
            response = client.get(f'{self.base_url}/get_item/{item_id}', headers=headers)
            response.raise_for_status()
            return response.json()

    def create_item(self, user_token, item):
        headers = {'Authorization': f'Bearer {user_token}'}
        with httpx.Client() as client:
            response = client.post(f'{self.base_url}/create_item/', json=item, headers=headers)
            response.raise_for_status()
            return response.json()

    def update_item(self, user_token, item_id, item):
        headers = {'Authorization': f'Bearer {user_token}'}
        with httpx.Client() as client:
            response = client.put(f'{self.base_url}/change_item/{item_id}', json=item, headers=headers)
            response.raise_for_status()
            return response.json()

    def delete_item(self, user_token, item_id):
        headers = {'Authorization': f'Bearer {user_token}'}
        with httpx.Client() as client:
            response = client.delete(f'{self.base_url}/delete_item/{item_id}', headers=headers)
            response.raise_for_status()
            return response.json()

    def delete_all_items(self, user_token):
        headers = {'Authorization': f'Bearer {user_token}'}
        with httpx.Client() as client:
            response = client.delete(f'{self.base_url}/delete_items/', headers=headers)
            response.raise_for_status()
            return response.json()
