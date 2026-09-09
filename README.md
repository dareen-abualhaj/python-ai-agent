# AI Agent CLI (Python)

An autonomous AI Agent command-line interface (CLI) built with Python and the OpenAI SDK (via OpenRouter). The agent interacts with the file system and executes Python code to solve tasks, debug code, and answer queries iteratively.

## 🚀 Features

- **Autonomous Agent Loop:** Iterates up to 20 times, maintaining conversation history (Assistant and Tool roles) until a final response is reached.
- **Secure File System Operations:** Strict path validation restricting agent actions to the designated directory.
- **Custom Tool Calling Architecture:** Includes dedicated tools for:
  - Listing directory contents and file metadata (`get_files_info`)
  - Reading file contents (`get_file_content`)
  - Writing and modifying files (`write_file`)
  - Executing Python files and tests (`run_python_file`)
- **Verbose Mode (`--verbose`):** Tracks token usage, function calls, and real-time execution outputs.

## 🛠️ Tech Stack

- **Python**
- **OpenAI SDK & OpenRouter API**
- **Uv (Package Manager)**
- **Git & GitHub**

## 💻 Installation & Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/dareen-abualhaj/python-ai-agent.git](https://github.com/dareen-abualhaj/python-ai-agent.git)
   cd python-ai-agent
