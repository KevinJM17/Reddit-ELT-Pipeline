from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient

def connect_to_storage_account(connect_string:str):
    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_string)
    return blob_service_client

def create_container(blob_service_client:BlobServiceClient.from_connection_string, container_name:str):
    try:
        blob_service_client.create_container(name=container_name)
        print('Container created')
    except ResourceExistsError:
        print('A container with this name already exists')

def upload_blob(blob_service_client:BlobServiceClient.from_connection_string, container_name:str, file_path:str, file_name:str):
    # upload_file_path = "./data/output/reddit_20250325.csv"
    # file_name = 'new data.csv'

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + file_name)

    # Upload the created file
    with open(file=file_path, mode="rb") as data:
        blob_client.upload_blob(data)
