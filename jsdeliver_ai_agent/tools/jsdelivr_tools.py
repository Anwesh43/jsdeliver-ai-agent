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
