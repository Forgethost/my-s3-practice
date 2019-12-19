
class S3Bucket:

    def __init__(self, name=None):
        self.name = name

    def load_bucket(self, file_name, bucket, s3client, object_name=None):

        if object_name == None:
            object_name = file_name

        response = s3client.upload_file(file_name,bucket, object_name)
        return response

    def load_obj_bucket(self, file_obj, bucket, s3client, object_name=None):
        
        response = s3client.upload_fileobj(file_obj,bucket, object_name)
        return response


