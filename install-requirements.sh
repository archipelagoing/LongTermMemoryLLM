#!/bin/bash

echo "Installing base dependencies..."
pip install -r requirements-base.txt

# Detect OS
OS_TYPE=$(uname -s)

if [ "$OS_TYPE" == "Linux" ]; then
    echo "Detected Linux. Installing Linux-specific dependencies..."
    pip install -r requirements-linux.txt
elif [ "$OS_TYPE" == "Darwin" ]; then
    echo "Detected macOS. Installing macOS-specific dependencies..."
    pip install -r requirements-mac.txt
else
    echo "Unsupported OS: $OS_TYPE"
    exit 1
fi

# Prompt for GPU installation
read -p "Do you want to install GPU (CUDA) dependencies? (y/n): " install_gpu
if [[ "$install_gpu" == "y" || "$install_gpu" == "Y" ]]; then
    echo "Installing GPU dependencies..."
    pip install -r requirements-gpu.txt
fi

echo "Installation complete!"
