# LangGraph ReAct Function Calling

An AI-powered project using **LangGraph**, **LangChain**, and OpenAI to implement the ReAct (Reasoning + Acting) paradigm with function calling. This setup demonstrates how to integrate reasoning steps with external function executions.

---

## Features

- ReAct (Reason + Act) pattern with LangGraph
- Function calling support using LangChain and OpenAI
- Environment variable management via `.env`
- Organized project structure with Poetry for dependency management
- Ready-to-extend nodes (`nodes.py`) and entry script (`main.py`)

---

## Project Structure

```
LangGraph_ReAct/
│── .env                # Environment variables (not committed)
│── .env.example        # Example environment variables file
│── .gitignore
│── main.py             # Entry point
│── nodes.py            # Node definitions for LangGraph
│── poetry.lock
│── poetry.toml
│── pyproject.toml      # Project configuration with dependencies
│── README.md           # Documentation
```

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mouyse/LangGraph-ReAct-Function-Calling.git
   cd LangGraph-ReAct-Function-Calling
   ```

2. Install dependencies with Poetry:

   ```bash
   poetry install
   ```

3. (Optional) Activate the virtual environment:

   ```bash
   poetry shell
   ```

---

## Configuration

1. Copy `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Add your API keys inside `.env`:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

---

## Usage

Run the entry script:

```bash
poetry run python main.py
```

Example output:

```
Hello from LangGraph ReAct
<your OpenAI API key>
```

---

## Development

- Code formatting: [Black](https://github.com/psf/black)
- Import sorting: [isort](https://pycqa.github.io/isort/)

Run formatters:

```bash
poetry run black .
poetry run isort .
```

---

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
