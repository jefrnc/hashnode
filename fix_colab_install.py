#!/usr/bin/env python3
"""
Fixed installation for Google Colab - handles PyTorch version conflicts
"""

import subprocess
import sys

def run_command(cmd):
    """Run shell command"""
    print(f"Running: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except:
        return False

print("🔧 Fixing PyTorch version conflicts in Google Colab...")

# First, uninstall conflicting packages
print("\n🗑️ Removing conflicting packages...")
run_command("pip uninstall -y torch torchvision torchaudio")

# Install compatible PyTorch 2.1.0 with CUDA 12.1
print("\n🔥 Installing PyTorch 2.1.0 with CUDA 12.1...")
run_command("pip install torch==2.1.0+cu121 torchvision==0.16.0+cu121 torchaudio==2.1.0+cu121 -f https://download.pytorch.org/whl/torch_stable.html")

# Install xformers compatible with PyTorch 2.1.0
print("\n⚡ Installing xformers...")
run_command("pip install xformers==0.0.22.post7")

# Install the rest of the dependencies
print("\n📦 Installing training dependencies...")
deps = """
accelerate==0.25.0
transformers==4.36.2
diffusers==0.25.0
bitsandbytes==0.41.2
safetensors==0.4.2
ftfy==6.1.1
einops==0.7.0
opencv-python==4.8.1.78
Pillow==10.2.0
prodigyopt==1.0
lion-pytorch==0.0.6
pytorch-lightning==2.0.9
tensorboard==2.15.1
toml==0.10.2
voluptuous==0.13.1
huggingface-hub==0.20.1
imagesize==1.4.1
rich==13.7.1
altair==4.2.2
easygui==0.98.3
triton==2.1.0
"""

for dep in deps.strip().split('\n'):
    if dep:
        run_command(f"pip install {dep}")

print("\n✅ Installation completed!")
print("\n🧪 Testing PyTorch installation...")
run_command("python -c 'import torch; print(f\"PyTorch version: {torch.__version__}\"); print(f\"CUDA available: {torch.cuda.is_available()}\")'")