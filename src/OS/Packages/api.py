import os
import requests
import tqdm

class File:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.path, 'w') as file:
            file.write(data)

    def append(self, data):
        with open(self.path, 'a') as file:
            file.write(data)

    def delete(self):
        os.remove(self.path)
        
class currOS:
    def getOsDir(self):
        return os.path.dirname(__file__)
    
    def getCurrFile(self):
        return os.path.basename(__file__)

    def getCurrFilePath(self):
        return os.path.abspath(__file__)
    
class Web:


    def download_file(self, url):
        # Send a GET request to the URL and get the response
        response = requests.get(url, stream=True)

        # Get the total size of the file
        total_size = int(response.headers.get("Content-Length", 0))

        # Get the file name from the URL
        file_name = os.path.basename(url)
        print("Downloading: " + file_name)
        print("Total size: " + str(total_size) + " bytes")
        print("From: " + url)
        # Create a progress bar using tqdm
        progress_bar = tqdm.tqdm(total=total_size, unit="B", unit_scale=True)

        # Open a file in binary write mode to save the downloaded data
        with open(file_name, "wb") as f:
            # Iterate over the response data in blocks of 1024 bytes
            for data in response.iter_content(1024):
                # Write the data to the file
                f.write(data)
                # Update the progress bar manually
                progress_bar.update(len(data))

        # Close the progress bar
        progress_bar.close()

        # Return the file name
        return file_name


