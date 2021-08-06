import requests
class Oauth:
    client_id = "873068029024534538" # Your Client ID here
    client_secret = "YvGETgKaE5tzqgZeJZO2yW8m9pHnTpBn" # Your Client Secret here
    #redirect_url = "http://127.0.0.1:5000/login"
    redirect_url="https://someapi.xyz/register/discord"
    scope = "identify%20email%20guilds"
    #discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=833122385603461121&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Flogin&response_type=code&scope=identify%20email%20guilds" # Paste the generated Oauth2 link here
    discord_login_url="https://discord.com/api/oauth2/authorize?client_id=833122385603461121&redirect_uri=http%3A%2F%2F192.168.1.109%3A80%2Flogin&response_type=code&scope=identify%20email%20guilds"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"
 
    @staticmethod
    def get_access_token(code):
        payload = {
            "client_id": Oauth.client_id,
            "client_secret": Oauth.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": Oauth.redirect_url,
            "scope": Oauth.scope
        }
        headers={
          'Content-Type': 'application/x-www-form-urlencoded'
        }
 
        access_token = requests.post(url = Oauth.discord_token_url,data = payload,headers=headers)
        json=access_token.json()
        return json.get("access_token")
