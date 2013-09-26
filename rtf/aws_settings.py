from settings import *

####################
#   AWS SETTINGS   #
####################
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
AWS_PRELOAD_METADATA = True
AWS_CLOUDFRONT_DOMAIN = CONFIG.get('aws_cloudfront_domain', '')
AWS_S3_SECURE_URLS = False
AWS_ACCESS_KEY_ID = CONFIG.get('aws_access_key_id', '')
AWS_SECRET_ACCESS_KEY = CONFIG.get('aws_secret_access_key', '')
AWS_STORAGE_BUCKET_NAME = CONFIG.get('aws_bucket_name', '')
CLOUDFRONT_URL = "http://" + AWS_CLOUDFRONT_DOMAIN + "/"
S3_URL = "http://"+ AWS_STORAGE_BUCKET_NAME +".s3.amazonaws.com/"
COMPRESS_ENABLED = False
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_STORAGE = 'storage.CachedS3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
]
STATIC_URL = CLOUDFRONT_URL
MEDIA_URL = STATIC_URL + "media/"
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
