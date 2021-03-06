from google.oauth2 import service_account


def login_with_json(credentials_file_path):

    try:
        credentials = service_account.Credentials.from_service_account_file(credentials_file_path)

    except OSError:
        print('File not found')

    scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])

    return credentials, scoped_credentials
