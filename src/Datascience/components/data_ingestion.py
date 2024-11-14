import os
import urllib.request as request
from src.Datascience import logger
import zipfile
from src.Datascience.entities.config_entity import DataIngestionconfig

# Data ingestion components
class DataIngestion:
    def __init__(self,config=DataIngestionconfig):
        self.config = config

    # Downloading the zip file 
    # Downloading the zip file
    def download_file(self):
    # Ensure the directory exists before downloading
        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)
    
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
            url=self.config.source_URL,
            filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info:\n{headers}")
        else:
            logger.info("File already exists")

    
    def extract_zip_file(self):
        """
        zip_file_path :str
        Extract the zip file into the data directory
        function returns None

        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)