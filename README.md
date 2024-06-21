# gen-ai-and-llm-integration

## 01 Running LLMs

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