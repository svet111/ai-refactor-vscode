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
### 1. Backend

```bash
cd server
pip install -r requirements.txt
uvicorn api:app --reload
```
### 2. Extention

```bash
cd extension
npm install
npm run compile
```
## API Key
Create .env file:
```bash
OPENAI_API_KEY=your_key_here
```
## Usage
1. Open Python file in VSCode
2. Run command:
```bash
AI: Refactor Code
```
4. See suggestions in panel
   
## Future Work
- Inline suggestions (Copilot-style)
- Multi-language support
- Diff view instead of text
- GitHub PR integration
