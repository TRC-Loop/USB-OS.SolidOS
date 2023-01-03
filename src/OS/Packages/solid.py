import os
import zipfile
import shutil
from api import Web, currOS
def install(package):
    try:
        url = f'https://stellar-cloud.com:2020/packages/{package}.zip'
        pkgname = Web().download_file(url)
        
        # Extract the package to the current working 
        print("Extracting package")
        zip = zipfile.ZipFile(pkgname)
        zip.extractall(currOS().getCurrFile())
        zip.close()

        # Remove the downloaded package file
        os.remove(package)
        print("Package installed successfully")
    except Exception as e:
        print(f"Error installing {package}: {e}")

def uninstall(package):
    try:
        # Remove the package files
        shutil.rmtree(currOS().getCurrFile() + package)
    except Exception as e:
        print(f"Error uninstalling {package}: {e}")
