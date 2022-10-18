from requests import Response
import json

def parse_api_call(response: Response):
    return json.dumps(response.json())
