# config.py — Application settings
# We read sensitive values (passwords, API keys) from environment variables
# so we never write them directly in the code.

import os
from dotenv import load_dotenv

# Load the .env file if it exists (only used during local development)
load_dotenv()

class Config:
    # A secret key Flask uses to protect sessions and cookies
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

    # Database URL — defaults to SQLite locally, PostgreSQL on Render
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///cameroun_memory.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # disable a feature we don't need

    # Cloudinary credentials (for storing audio, video, and photos)
    CLOUDINARY_CLOUD_NAME  = os.environ.get('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY     = os.environ.get('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET  = os.environ.get('CLOUDINARY_API_SECRET')

    # Maximum file upload size: 100 MB
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024
