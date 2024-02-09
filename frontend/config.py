import os

from dotenv import load_dotenv

load_dotenv()

# all environment variables should be defined as Python variables here
STORAGE_SECRET = os.environ.get("STORAGE_SECRET")  # storage secret key is required to use app.storage

# in reality users passwords would obviously need to be hashed
passwords = {'user1': 'pass1', 'user2': 'pass2'}

unrestricted_page_routes = {'/login'}
