from core.database import session
from models import TokenDB


class TokensServices():
    def get_token_by_email(self, email: str):
        token = session.query(TokenDB).filter_by(email=email).first()
        return token


tokens_services = TokensServices()
