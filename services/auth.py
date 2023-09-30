import requests


class AuthService:
    API_URL = 'https://global-inno-hack-dd509ac0d0a4.herokuapp.com/auth'

    def sign_in(self, user_id, email, password):
        response = requests.post(
            url=self.API_URL + '/',
            params={
                'user_id': user_id,
                'email': email,
                'password': password
            },
            headers={
                'accept': 'application/json'
            }
        )
        tokens = response.json()
        return tokens


auth_service = AuthService()

if __name__ == "__main__":
    auth_service.sign_in(123, "kondrandr2004@yandex.ru", "Qwerty2004")
