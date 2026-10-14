from tools.jsdelivr_tools import getPackageVersionFileDetails, getPackageStats, getTopPackagesStats, getPackageVersions
from typing import Dict 
import json 

def writeFile(fileName : str, data : Dict):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data to {fileName}")

if __name__ == "__main__":
    packageStats = getTopPackagesStats()
    writeFile("test_packages_stats.json", packageStats)
    if len(packageStats) > 0:
        name = packageStats[0]["name"]
        typeStr = packageStats[0]["type"]
        packageVersions = getPackageVersions(type=typeStr, name=name)
        writeFile("tes_package_details.json", packageVersions)
        writeFile(f"test_package_stats_{name.replace("/", "_")}.json", getPackageStats(type=typeStr, name=name))
        if len(packageVersions) > 0:
            writeFile("test_package_version_details.json", getPackageVersionFileDetails(type=typeStr, name = name, version=packageVersions[0]))