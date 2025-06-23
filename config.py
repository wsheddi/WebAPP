import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Secret key for Flask sessions
    SECRET_KEY = os.environ.get('SECRET_KEY', 'ksdfj0239kjsdlfji!@#89234')
    
    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT', 'cmssstoragewadha')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER', 'images')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY', '1Yq/2EqrzvtcyfSnuHLew6WiVTk7qHIvKBxHPVJ0EIe16JCBqFRwfifNI+MyRVqUF3/fZqIwvH63+AStM//KLw==')

    # SQL Database connection
    SQL_SERVER = os.environ.get('SQL_SERVER', 'cmsdbserverwadha.database.windows.net')
    SQL_DATABASE = os.environ.get('SQL_DATABASE', 'cmsdb')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME', 'Admin1')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD', 'Wadha@10')
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/"
        f"{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&Encrypt=yes"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MS Identity Platform (Azure AD)
    CLIENT_ID = os.environ.get('CLIENT_ID', '9d2b1629-415e-460e-b635-eda4dbd1d0c9')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET', 'bEZ8Q~mn9ueWDVxZMoBPpHsM7pcmsUwVh~QTPdbN')
    REDIRECT_PATH = os.environ.get('REDIRECT_PATH', '/getAToken')
    AUTHORITY = os.environ.get('AUTHORITY', 'https://login.microsoftonline.com/2c86bbfc-8d04-41ff-a83a-942f075e0f60')

    # MS Graph scope
    SCOPE = ["User.Read"]

    # Flask session type
    SESSION_TYPE = "filesystem"
