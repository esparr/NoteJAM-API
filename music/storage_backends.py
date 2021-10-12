from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
    
# class PublicMediaStorage(BaseS3Storage):
#     location = 'media'
#     default_acl = 'public-read'
#     file_overwrite = False