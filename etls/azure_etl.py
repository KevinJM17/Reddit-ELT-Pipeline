from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient

def connect_to_storage_account(connect_string: str):
    try:
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(connect_string)
        print('Connected to Azure Storage Account')
        return blob_service_client
    
    except Exception as e:
        print(e)

def create_container(blob_service_client: BlobServiceClient, container_name: str):
    try:
        blob_service_client.create_container(name=container_name)
        print('Container created')
    
    except ResourceExistsError:
        print('A container with this name already exists')

    except Exception as e:
        print(e)

def upload_blob(blob_service_client, container_name:str, file_path:str, file_name:str):
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        print(f'Uploading {file_name} to Azure Storage as blob')
        # Upload the created file
        with open(file=file_path, mode="rb") as data:
            blob_client.upload_blob(data)

    except FileNotFoundError:
        print('File not found')