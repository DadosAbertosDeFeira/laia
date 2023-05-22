#!/bin/bash

echo "===== Starting the deploy ====="

cd /home/admin/app

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate

echo "Done!"
