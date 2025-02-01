#!/bin/bash

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "🚫 python3 could not be found, please install it."
    exit
fi

# Create virtual environment
echo "\n🔧 Creating virtual environment..."
python3 -m venv embeddings-env

# Activate virtual environment
echo "\n✅ Activating virtual environment..."
source embeddings-env/bin/activate

# Install dependencies
if [ -f requirements.txt ]; then
    echo "\n🚀 Installing dependencies...\n"
    pip install -r requirements.txt
    echo "\n🎉 Setup complete ✅\n"
else
    echo "\n ⚠️ No requirements.txt found.\n"
fi
