#!/bin/bash
# Installation script for Google Colab

echo "🚀 Starting installation for Spanish Lora Trainer..."

# Update system packages
echo "📦 Updating system packages..."
apt-get update -qq
apt-get install -y aria2 -qq

# Upgrade pip
echo "🔧 Upgrading pip..."
pip install --upgrade pip

# Install PyTorch with CUDA 12.1 support
echo "🔥 Installing PyTorch..."
pip install torch==2.1.2 torchvision==0.16.2 --index-url https://download.pytorch.org/whl/cu121

# Install xformers for memory efficiency
echo "⚡ Installing xformers..."
pip install xformers==0.0.23.post1

# Install main dependencies
echo "📦 Installing core dependencies..."
pip install \
    accelerate==0.25.0 \
    transformers==4.36.2 \
    diffusers[torch]==0.25.0 \
    bitsandbytes==0.43.0 \
    safetensors==0.4.2

# Install data processing libraries
echo "🖼️ Installing data processing libraries..."
pip install \
    ftfy==6.1.1 \
    einops==0.7.0 \
    opencv-python==4.8.1.78 \
    Pillow==10.2.0

# Install optimization libraries
echo "🚀 Installing optimization libraries..."
pip install \
    prodigyopt==1.0 \
    lion-pytorch==0.0.6 \
    pytorch-lightning==1.9.0

# Install utility libraries
echo "🛠️ Installing utility libraries..."
pip install \
    tensorboard==2.15.1 \
    toml==0.10.2 \
    voluptuous==0.13.1 \
    huggingface-hub==0.20.1 \
    imagesize==1.4.1 \
    rich==13.7.1 \
    altair==4.2.2 \
    easygui==0.98.3

# Install triton
echo "⚙️ Installing triton..."
pip install triton==2.1.0

# Clone kohya repository if not exists
if [ ! -d "/content/kohya-trainer" ]; then
    echo "📥 Cloning kohya-ss repository..."
    git clone https://github.com/kohya-ss/sd-scripts /content/kohya-trainer
fi

echo "✅ Installation completed!"