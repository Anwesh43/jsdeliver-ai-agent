import requests 
from urllib.parse import urlencode 
from typing import Dict 

class BaseHTTPClient:
    def __init__(self, baseURL : str):
        self.baseURL = baseURL 

    def handleError(self, e):
        return {
            "status": "Error", 
            "message": f"Error due to {str(e)}"
        }
    
    def getCall(self, endpoint : str, qpParams : Dict = {}):
        response = requests.get(f"{self.baseURL}/{endpoint}")
        response.raise_for_status()
        return response.json()