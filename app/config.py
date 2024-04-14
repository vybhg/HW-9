import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Environment Variables for Configuration

# Directory where QR codes are saved
QR_DIRECTORY = Path(os.getenv('QR_CODE_DIR', './qr_codes'))

# Color of the QR code
FILL_COLOR = os.getenv('FILL_COLOR', 'red')

# Background color of the QR code
BACK_COLOR = os.getenv('BACK_COLOR', 'white')

# Base URL for the server
SERVER_BASE_URL = os.getenv('SERVER_BASE_URL', 'http://localhost:80')

# Directory exposed by the server for downloads
SERVER_DOWNLOAD_FOLDER = os.getenv('SERVER_DOWNLOAD_FOLDER', 'downloads')

# Secret key for cryptographic operations
SECRET_KEY = os.getenv("SECRET_KEY", "secret-getenvkey")

# Algorithm used for JWT encoding/decoding
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# Expiration time for access tokens (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Placeholder credentials for basic authentication
ADMIN_USER = os.getenv('ADMIN_USER', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'secret')
