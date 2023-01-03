import os
import zipfile
import requests
import shutil

def install(package):
    url = f'https://stellar-cloud.com:2020/packages/{package}.zip'
    response = requests.get(url)
    open(package, 'wb').write(response.content)

    # Extract the package to the current working directory
    zip = zipfile.ZipFile(package)
    zip.extractall()
    zip.close()

    # Remove the downloaded package file
    os.remove(package)

def uninstall(package):
    # Remove the package files
    shutil.rmtree(package)
