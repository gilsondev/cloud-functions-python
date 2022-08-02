from google.cloud import storage


class Storage:
    def __init__(self, bucket_name) -> None:
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket(bucket_name)

    def get_blob(self, filename) -> storage.Blob | None:
        return self.bucket.get_blob(filename)

    def upload(self, blob_filename, local_filename) -> None:
        blob = self.bucket.blob(blob_filename)
        blob.upload_from_filename(local_filename)
