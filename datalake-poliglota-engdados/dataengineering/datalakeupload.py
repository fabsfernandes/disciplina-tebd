from google.cloud import storage
import mongodbexport, neo4jexport

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="symbolic-voyage-322500-a94e7e91accc.json"


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

if __name__ == "__main__":
    mongodbexport.export()
    upload_blob('example-tebd', 'tarefastodo_mongodb.json', 'tarefastodo_mongodb.json')
    neo4jexport.export()
    upload_blob('example-tebd', 'miniblog_neo4j.json', 'miniblog_neo4j.json')
