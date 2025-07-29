# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Hashnode blog repository containing:
- A Spanish LoRA (Low-Rank Adaptation) training notebook for Stable Diffusion models
- Blog post content about a DevOps professional transitioning to trading

## Repository Structure

```
├── README.md                       # Minimal repository documentation
├── Spanish_Lora_Trainer.ipynb      # Jupyter notebook for training LoRA models in Spanish
└── cmdl5r9x0000p02lcb1sch53o.md   # Blog post about DevOps to trading transition
```

## Working with the LoRA Trainer Notebook

The `Spanish_Lora_Trainer.ipynb` is a Google Colab notebook based on Kohya's sd-scripts for training LoRA models. Key features:

- Supports LoRA and LoCon training types
- Configured for Spanish language users
- Includes dataset preparation, model downloading, and training configuration
- Uses accelerate, transformers, diffusers, and other ML libraries
- Supports various optimizers including AdamW8bit, Prodigy, and DAdaptation

### Key Parameters
- Default resolution: 512px
- Batch size: 2 (recommended)
- Learning rates: unet_lr=5e-4, text_encoder_lr=1e-4
- Network dimensions: dim=16, alpha=8

## Blog Content

The repository contains Hashnode blog posts in Markdown format with frontmatter metadata. Posts follow this structure:
- Frontmatter with title, date, cuid, slug, and tags
- Content in Spanish
- Focus on technical topics related to DevOps and trading

## Development Notes

- This is primarily a content repository for a Hashnode blog
- The Jupyter notebook is meant to be run in Google Colab environment
- No traditional build or deployment commands are needed
- Content updates should maintain the existing Markdown format with proper frontmatter