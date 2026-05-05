# ai-refactor-vscode
An AI-powered VSCode extension that analyzes and improves Python code using LLMs + static analysis.
## Features
- One-click code refactoring
- AST-based static analysis
- LLM-powered suggestions
- Side-by-side results in VSCode
- Works on full file instantly
  
## Architecture
- VSCode Extension (TypeScript)
- FastAPI backend (Python)
- OpenAI GPT-4.1

## Setup
  1. Backend
     
  - pip install -r requirements.txt
  - uvicorn api:app --reload
  
  2. Extension
  
  - cd extension
  - npm install
  - npm run compile

  Then open in VSCode → press F5

* for work add your API as in .env.example
