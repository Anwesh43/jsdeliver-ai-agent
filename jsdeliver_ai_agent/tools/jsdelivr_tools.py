from services.jsdelivr_service import JSDelivrService 

jsd = JSDelivrService()

def getTopPackagesStats():
    print(f"Calling getTopPackagesStats tool")
    return jsd.getTopPackagesStats()

def getPackageVersions(type : str, name : str):
    print(f"Calling getPackageVersions tool for {type}/{name}")
    return jsd.getPackageVersions(type=type, name = name)

def getPackageStats(type : str, name : str):
    print(f"Calling getPackageStats for {type}/{name}")
    return jsd.getPackageStats(type, name)

def getPackageVersionFileDetails(type: str, name : str, version: str):
    print(f"Calling getPackageVersionDetails for {type}/{name}@{version}")
    return jsd.getPackageVersionFileDetails(type=type, name = name, version=version)

def writeHTML(htmlStr : str, fileName : str):
    print(f"Calling writeHTML tool for {fileName} and {htmlStr}")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": "success",
        "message": f"Written html to {fileName}, don't display html string to user"
    }

def getAvailableTools():
    return [
        getTopPackagesStats,
        getPackageVersions,
        getPackageStats,
        getPackageVersionFileDetails,
        writeHTML
    ]