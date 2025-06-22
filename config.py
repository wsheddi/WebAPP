import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ksdfj0239kjsdlfji!@#89234'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmssstoragewadha'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '1Yq/2EqrzvtcyfSnuHLew6WiVTk7qHIvKBxHPVJ0EIe16JCBqFRwfifNI+MyRVqUF3/fZqIwvH63+AStM//KLw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsdbserverwadha.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cmsdb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'Admin1'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Wadha@10'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://' +
        SQL_USER_NAME + '@' + SQL_SERVER + ':' +
        SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' +
        SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MSAL (Microsoft Authentication) Info
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or "bEZ8Q~mn9ueWDVxZMoBPpHsM7pcmsUwVh~QTPdbN"
    CLIENT_ID = os.environ.get('CLIENT_ID') or "9d2b1629-415e-460e-b635-eda4dbd1d0c9"
    AUTHORITY = os.environ.get('AUTHORITY') or "https://login.microsoftonline.com/2c86bbfc-8d04-41ff-a83a-942f075e0f60"
    REDIRECT_PATH = os.environ.get('REDIRECT_PATH') or "/getAToken"  # Must match your app registration

    # Only need to read user profile for this app
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
