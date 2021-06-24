

def prepare_package(requirements_file):
    """
    prepares package folder
    - copy project files
    - copy handler.py
    - install packages
    """


def make_archive():
    """
    make archive for a given folder. ready for upload
    """


def cleanup():
    """
    deletes tmp package folder
    """


def upload_to_bucket(folder, bucket):
    """
    makes archive, uploads to bucket, deletes tmp package
    """


def delete_bucket(bucket_name):
    """
    deletes bucket from s3
    """
