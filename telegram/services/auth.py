import requests



class AuthService:
    API_URL = 'https://auth-api.teamflame.ru/auth'

    def sign_in(self, user_id, email, password):
        # , email: str, password: str
        # access_token = ...
        response = requests.post(
            url=self.API_URL + '/sign-in',
            data={
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
