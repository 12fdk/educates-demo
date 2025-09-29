#!/bin/bash

# Pre work
touch ~/.bashrc

# Install Jupiter Lab
pip install jupyterlab 

# Install Opencoder
#curl -fsSL https://opencode.ai/install | bash
#npm install -g opencode-ai
cp opencode /home/eduk8s/bin

mkdir -p ~/.config/opencode/

echo 'export OLLAMA=http://ollama.$SESSION_NAMESPACE:11434/v1' >> ~/.bashrc 

echo '{
  "$schema": "https://opencode.ai/config.json",
  "model": "ollama/qwen3:0.6b",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local - test)",
      "options": {
        "baseURL": "{env:OLLAMA}"
      },
      "models": {
        "qwen3:0.6b": {
          "name": "qwen3:0.6b"
        }
      }
    }
  }
}' > ~/.config/opencode/opencode.json

#echo 'export PATH="/home/eduk8s/.opencode/bin:$PATH"' >> ~/.bashrc

# Post work
source ~/.bashrc

#jupyter lab --LabApp.token='1234' --LabApp.allow_remote_access='True' --LabApp.allow_origin='*'


#/home/eduk8s/.local/bin/jupyter lab --LabApp.token='lab' --LabApp.allow_remote_access='True' --LabApp.allow_origin='*'