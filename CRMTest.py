from dynamics365crm.client import Client
import webbrowser
import json
from pathlib import Path
import os
from types import SimpleNamespace

def readConfig():
    configFilePath = Path(os.getcwd()).parent / "credentials.json"
    print(f"Reading config file from {configFilePath}")

    args = SimpleNamespace()

    with open(configFilePath) as f:
        data = json.load(f)['CRM app']
        args.client_id = data['client_id']
        args.client_secret = data['client_secret']
        args.resource = data['resource']
    return args

def login(args):
    client_id = args.client_id #From Azure app registration
    client_secret = args.client_secret #From Azure app secrets
    redirect_url = 'https://stavrostest/auth'

    client = Client(args.resource, client_id, client_secret)

    #https://github.com/GearPlug/dynamics365crm-python
    #You construct an authorization url using the url_petition method
    #Here you must set the redirect URL that you have also set in the Azure app
    url = client.url_petition(redirect_url)

    #The user access to this url and authorize your app with a set of permissions (scopes). 
    #The user is redirected to your web server and you grab the authorization code and exchange it 
    # with the exchange_code method for an access token. 
    # Then you start using the provided access token to access resources on the user behalf.
    webbrowser.open(url)

    #Get the code from URL, it can be used only once to get a token
    code = input("Enter the code you've got from the URL: ")

    token = client.exchange_code(redirect_url, code)
    client.set_token(token['access_token'])

    return client

args = readConfig()

tokenFile = "token.txt"
if os.path.isfile(tokenFile):
    f = open(tokenFile, "r")
    token = f.read()
    f.close()
    client = Client(resource=args.resource, token=token)
else:
    client = login(args)
    f = open(tokenFile, "w")
    f.write(client.token)
    f.close()
    

list_contacts = client.get_contacts()
print(list_contacts)