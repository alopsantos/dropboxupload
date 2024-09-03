import os
import dropbox
import dropbox.files


dbx = dropbox.Dropbox("TOKEN")


def upload_folder(local_folder_path, dropbox_folder_path):
    """
    Uploads a local folder to Dropbox.

    :param local_folder_path: The path to the local folder to upload
    :param dropbox_folder_path: The path to the Dropbox folder to upload to
    """
    for root, dirs, files in os.walk(local_folder_path):
        for file_name in files:
            local_file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(local_file_path, local_folder_path)
            dropbox_file_path = os.path.join(
                dropbox_folder_path, relative_path).replace("\\", "/")

            with open(local_file_path, 'rb') as f:
                print(f"Uploading {local_file_path} to {dropbox_file_path}...")
                dbx.files_upload(f.read(), dropbox_file_path)

    print("Upload complete!")


# Example usage
local_folder_path = 'local_files'
dropbox_folder_path = '/0 - Servidor Novo/'
upload_folder(local_folder_path, dropbox_folder_path)
