import requests
import json 


class Webhook:
    def __init__(self, data, zap_hook_url):
        self.data = data
        self.zap_hook_url = zap_hook_url
        

    def postRequest(self):    #remember that you must use the self as an argument
        r = requests.post(self.zap_hook_url, data=json.dumps(self.data), headers={'Content-Type': 'application/json'})



# if __name__ == "__main__":
    
#     zap_hook_url = 'https://hooks.zapier.com/hooks/catch/10537799/b22e70h/'
#     data =''




