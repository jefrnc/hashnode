#!/usr/bin/env python3
"""
Fixed installation script for Spanish Lora Trainer dependencies
"""

import subprocess
import sys
import os

def run_command(cmd, description=""):
    """Run a shell command and handle errors"""
    print(f"\n{'='*60}")
    if description:
        print(f"📦 {description}")
    print(f"🔧 Running: {cmd}")
    print('='*60)
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False

def install_dependencies():
    """Install all required dependencies"""
    
    # Check if running in Colab
    try:
        import google.colab
        IN_COLAB = True
        print("🎯 Detected Google Colab environment")
    except ImportError:
        IN_COLAB = False
        print("💻 Running in local environment")
    
    # System dependencies (for Colab)
    if IN_COLAB:
        print("\n🔄 Updating system packages...")
        run_command("apt-get update -qq", "Updating apt packages")
        run_command("apt-get install -y aria2 -qq", "Installing aria2 for downloads")
    
    # Upgrade pip
    print("\n🔄 Upgrading pip...")
    run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrading pip")
    
    # Install PyTorch with CUDA support
    print("\n🔥 Installing PyTorch with CUDA support...")
    if IN_COLAB:
        # Colab-specific PyTorch installation
        run_command(
            f"{sys.executable} -m pip install torch==2.1.2 torchvision==0.16.2 --index-url https://download.pytorch.org/whl/cu121",
            "Installing PyTorch for CUDA 12.1"
        )
    else:
        # Local installation (adjust CUDA version as needed)
        run_command(
            f"{sys.executable} -m pip install torch==2.1.2 torchvision==0.16.2 --index-url https://download.pytorch.org/whl/cu118",
            "Installing PyTorch for CUDA 11.8"
        )
    
    # Install xformers (memory efficient attention)
    print("\n⚡ Installing xformers...")
    run_command(f"{sys.executable} -m pip install xformers==0.0.23.post1", "Installing xformers")
    
    # Install main dependencies
    print("\n📦 Installing main dependencies...")
    main_deps = [
        "accelerate==0.25.0",
        "transformers==4.36.2",
        "diffusers[torch]==0.25.0",
        "bitsandbytes==0.43.0",
        "safetensors==0.4.2",
        "ftfy==6.1.1",
        "einops==0.7.0",
        "opencv-python==4.8.1.78",
        "Pillow==10.2.0"
    ]
    
    for dep in main_deps:
        run_command(f"{sys.executable} -m pip install {dep}", f"Installing {dep}")
    
    # Install optimization libraries
    print("\n🚀 Installing optimization libraries...")
    opt_deps = [
        "prodigyopt==1.0",
        "lion-pytorch==0.0.6",
        "pytorch-lightning==1.9.0"
    ]
    
    for dep in opt_deps:
        run_command(f"{sys.executable} -m pip install {dep}", f"Installing {dep}")
    
    # Install utility libraries
    print("\n🛠️ Installing utility libraries...")
    util_deps = [
        "tensorboard==2.15.1",
        "toml==0.10.2",
        "voluptuous==0.13.1",
        "huggingface-hub==0.20.1",
        "imagesize==1.4.1",
        "rich==13.7.1",
        "altair==4.2.2",
        "easygui==0.98.3"
    ]
    
    for dep in util_deps:
        run_command(f"{sys.executable} -m pip install {dep}", f"Installing {dep}")
    
    # Install triton (for optimized kernels)
    print("\n⚙️ Installing triton...")
    run_command(f"{sys.executable} -m pip install triton==2.1.0", "Installing triton")
    
    # Clone kohya-ss repository
    print("\n📥 Cloning kohya-ss repository...")
    if IN_COLAB:
        repo_dir = "/content/kohya-trainer"
    else:
        repo_dir = os.path.expanduser("~/kohya-trainer")
    
    if os.path.exists(repo_dir):
        print(f"Repository already exists at {repo_dir}")
    else:
        run_command(
            f"git clone https://github.com/kohya-ss/sd-scripts {repo_dir}",
            "Cloning kohya-ss/sd-scripts"
        )
    
    print("\n✅ Installation completed successfully!")
    print("\nYou can now run the Spanish Lora Trainer notebook.")
    
    # Test imports
    print("\n🧪 Testing imports...")
    test_imports = [
        "torch",
        "torchvision",
        "xformers",
        "accelerate",
        "transformers",
        "diffusers",
        "bitsandbytes",
        "safetensors"
    ]
    
    failed_imports = []
    for module in test_imports:
        try:
            __import__(module)
            print(f"✅ {module} imported successfully")
        except ImportError as e:
            print(f"❌ Failed to import {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n⚠️ Warning: Failed to import {len(failed_imports)} modules: {', '.join(failed_imports)}")
        print("You may need to install them manually or check for compatibility issues.")
    else:
        print("\n🎉 All modules imported successfully!")

if __name__ == "__main__":
    install_dependencies()