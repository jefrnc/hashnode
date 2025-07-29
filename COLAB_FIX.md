# 🔧 Solución para el error de dependencias en Google Colab

## El problema
El notebook está intentando instalar `torch==2.4.1+cu121` pero Colab ya tiene instalado `torch==2.6.0` con `torchaudio` y `torchvision` que dependen de esa versión.

## Solución rápida (copiar y pegar en una celda):

```python
# Celda 1: Desinstalar versiones conflictivas
!pip uninstall -y torch torchvision torchaudio

# Celda 2: Instalar versiones compatibles
!pip install torch==2.1.0+cu121 torchvision==0.16.0+cu121 torchaudio==2.1.0+cu121 -f https://download.pytorch.org/whl/torch_stable.html

# Celda 3: Instalar el resto de dependencias
!pip install accelerate==0.25.0 transformers==4.36.2 diffusers==0.25.0 bitsandbytes==0.41.2 safetensors==0.4.2 xformers==0.0.22.post7
!pip install ftfy==6.1.1 einops==0.7.0 opencv-python==4.8.1.78 Pillow==10.2.0
!pip install prodigyopt==1.0 lion-pytorch==0.0.6 pytorch-lightning==2.0.9 tensorboard==2.15.1
!pip install toml==0.10.2 voluptuous==0.13.1 huggingface-hub==0.20.1 imagesize==1.4.1
!pip install rich==13.7.1 altair==4.2.2 easygui==0.98.3 triton==2.1.0

# Celda 4: Verificar instalación
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
```

## Alternativa: Modificar el notebook

Si prefieres modificar el notebook original, busca la función `install_dependencies()` y reemplaza esta línea:

```python
# BUSCAR:
!pip install ... torch==2.4.1+cu121 ...

# REEMPLAZAR POR:
!pip install torch==2.1.0+cu121 torchvision==0.16.0+cu121 torchaudio==2.1.0+cu121 -f https://download.pytorch.org/whl/torch_stable.html
```

Y también cambiar xformers:
```python
# BUSCAR:
!pip install xformers==0.0.28.post1

# REEMPLAZAR POR:
!pip install xformers==0.0.22.post7
```

## Notas importantes:
- PyTorch 2.1.0 es totalmente compatible con el entrenamiento de LoRA
- Las versiones ajustadas mantienen la compatibilidad con CUDA 12.1
- Si sigues teniendo problemas, reinicia el runtime de Colab antes de instalar