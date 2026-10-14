from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 

load_dotenv()

class JSDelivrService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["JSDELIVR_BASE_URL"])

    def getPackageStats(self):
        try:
            packages = self.client.getCall("stats/packages")
            responseKeys = ["type", "name", "hits"]
            results = []
            for package in packages:
                resultObj = {}
                for responseKey in responseKeys:
                    resultObj[responseKey] = package[responseKey]
                results.append(resultObj)
            return results 
        except Exception as e:
            return self.client.handleError(e)

    def getPackageVersions(self, type: str, name : str):
        try:
            packageDetails = self.client.getCall(f"{type}/{name}")
            versionResults = []
            if "versions" in packageDetails:
                versionObjects = packageDetails["versions"]
                for versionObject in versionObjects:
                    version = versionObject["versions"]
                    versionParts = version.split("-")
                    if len(versionParts) == 1 and len(versionParts.split(".")) == 3:
                        versionResults.append(versionParts[0])
            return versionResults
        except Exception as e:
            return self.client.handleError(e)

    def getPackageVersionFileDetails(self, type : str, name : str, version : str):
        try:
            packageVersions = self.client.getCall(f"{type}/{name}@{version}")
            result = {}
            if "default" in packageVersions and "files" in packageVersions:
                result["entryFile"] = packageVersions["default"]
                result["fileStructure"] = packageVersions["files"]
            return result 
        except Exception as e:
            return self.client.handleError(e)

    def getPackageStats(self, type: str, name: str, version : str):
        try:
            packageStats = self.client.getCall(f"stats/packages/{type}/{name}")
            return packageStats
        except Exception as e:
            return self.client.handleError(e)
    