# gen-ai-and-llm-integration

## 01 Running LLMs

```bash
# Install Pytorch conda
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y

# Latest Windows App SDK downloads
https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/downloads

# CUDA Toolkit 11.7 Downloads
https://developer.nvidia.com/cuda-11-7-0-download-archive

# cuDNN 9.2.0 Downloads
https://developer.nvidia.com/cudnn-downloads
```

**04 LMQL playground**

```bash
conda install conda-forge::nodejs -y
brew install yarn

# Running LMQL Programs
lmql playground
docker run -d -p 3000:3000 -p 3004:3004 lmql-docker:latest

# Self-Hosted Models
lmql serve-model
```

Link: 
- https://lmql.ai/docs/lib/python.html
- https://lmql.ai/docs/development/docker-setup.html