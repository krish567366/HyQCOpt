from fastapi import Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from authlib.integrations.starlette_client import OAuth
from starlette.requests import Request
from jose import JWTError, jwt

oauth = OAuth()
oauth.register(
    name='auth0',
    client_id=os.getenv('AUTH0_CLIENT_ID'),
    client_secret=os.getenv('AUTH0_CLIENT_SECRET'),
    api_base_url=os.getenv('AUTH0_DOMAIN'),
    access_token_url=f"{os.getenv('AUTH0_DOMAIN')}/oauth/token",
    authorize_url=f"{os.getenv('AUTH0_DOMAIN')}/authorize",
    client_kwargs={'scope': 'openid profile email'},
)

async def get_current_user(request: Request):
    try:
        token = await oauth.auth0.authorize_access_token(request)
        userinfo = token.get('userinfo')
        jwt.decode(
            token['access_token'],
            os.getenv('AUTH0_CLIENT_SECRET'),
            audience=os.getenv('AUTH0_AUDIENCE'),
            issuer=os.getenv('AUTH0_DOMAIN') + '/'
        )
        return {
            'id': userinfo['sub'],
            'email': userinfo['email'],
            'tier': userinfo.get('https://hyqcopt/tier', 'basic')
        }
    except (JWTError, KeyError) as e:
        raise HTTPException(401, "Invalid credentials")