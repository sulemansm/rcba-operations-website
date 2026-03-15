import secrets
import urllib.parse
import requests

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_INFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"


def generate_state():
    """
    Generate a secure random state string for OAuth.
    Used to prevent CSRF attacks.
    """
    return secrets.token_hex(16)


def build_auth_url(client_id, redirect_uri, state):
    """
    Build the Google OAuth login URL.
    """

    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": "openid email profile",
        "state": state,
        "access_type": "online",
        "prompt": "select_account"
    }

    return GOOGLE_AUTH_URL + "?" + urllib.parse.urlencode(params)


def exchange_code(code, client_id, client_secret, redirect_uri):
    """
    Exchange authorization code for access token.
    """

    response = requests.post(
        GOOGLE_TOKEN_URL,
        data={
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code"
        }
    )

    response.raise_for_status()

    return response.json()


def fetch_user(access_token):
    """
    Fetch user profile from Google using the access token.
    """

    response = requests.get(
        GOOGLE_INFO_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    response.raise_for_status()

    return response.json()