from rest_framework import authentication


class BearerAuthentication(authentication.TokenAuthentication):
    """
    postman 에서 token header 값에 'Token'대신에 'Bearer'가 오기 때문에
    TokenAuth를 상속받으면서 keyword 값만 Bearer로 변경
    """
    keyword = 'Bearer'
