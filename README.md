# LangGraph ReAct with Function Calling

LangGraph ReAct with Function Calling demonstrates how to build reasoning agents using **LangGraph**, **LangChain**, and **function calling** with custom tools.

This project showcases:
- ReAct (Reasoning + Acting) pattern with LangGraph
- Integration of **OpenAI** models (via `ChatOpenAI`)
- Web search capability using **TavilySearch**
- Custom Python tool (`triple`) for function calling
- Conditional graph flows for agent reasoning

---

## 📂 Project Structure

```
LangGraph_ReAct_Function_Calling/
├── .env                # Environment variables
├── .env.example        # Example env file
├── .gitignore
├── main.py             # Entry point, builds and runs the LangGraph workflow
├── nodes.py            # Defines reasoning and tool execution nodes
├── react.py            # Defines tools and LLM binding
├── poetry.lock
├── poetry.toml
├── pyproject.toml      # Poetry dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/mouyse/LangGraph-ReAct-Function-Calling.git
cd LangGraph-ReAct-Function-Calling
```

2. Install dependencies with **Poetry**:

```bash
poetry install
```

3. Activate virtual environment:

```bash
poetry shell
```

4. Setup environment variables:

```bash
cp .env.example .env
```

Update `.env` with your keys:

```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## 🚀 Usage

Run the project:

```bash
python main.py
```

Expected output (example):

```
Hello from LangGraph ReAct with Function calling
<Agent's reasoning and response with tool usage>
```

It will also generate a `flow.png` visualization of the LangGraph workflow.

---

## 🛠️ Tools Used

- **LangGraph** → For building graph-based reasoning workflows
- **LangChain** → Core framework for LLM orchestration
- **OpenAI (ChatOpenAI)** → LLM for reasoning and function calling
- **TavilySearch** → Web search integration
- **Custom tool (triple)** → Example numeric operation tool

---

## 📖 Example Query

The agent can answer:

```
"How many prime ministers has India had and list them down?
Which Prime Minister of India is Narendra Modi in the order of succession?
List it and then triple the number."
```

The reasoning agent will:
1. Search and retrieve information via TavilySearch
2. Use ReAct reasoning to determine the answer
3. Call the **triple tool** on the result

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open a PR or an issue.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🔗 Repository

[LangGraph-ReAct-Function-Calling](https://github.com/mouyse/LangGraph-ReAct-Function-Calling)
