# 📉 Chat Financeiro — LangChain + LangGraph + Yahoo Finance

A professional-grade AI assistant for querying real-time stock prices using the power of **LangChain**, **LangGraph**, and **yfinance**.
Built with extensibility and clean code practices in mind, this project demonstrates how to integrate tool-calling agents using OpenAI models.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/LangGraph-Agent-brightgreen.svg" />
  <img src="https://img.shields.io/badge/OpenAI-API-lightgrey.svg" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
</p>

---

## 🚀 Features

* 🔗 Tool-calling agent powered by LangGraph + LangChain
* 📈 Real-time stock price lookup via Yahoo Finance (through `yfinance`)
* 🧠 Contextual memory via message history
* 🔐 Environment configuration with `.env` (not tracked by Git)
* ✨ Minimal, readable, production-quality code

---

## 🧰 Technologies Used

* [LangChain](https://github.com/langchain-ai/langchain)
* [LangGraph](https://github.com/langchain-ai/langgraph)
* [LangChain OpenAI Integration](https://python.langchain.com/docs/integrations/llms/openai/)
* [yfinance](https://github.com/ranaroussi/yfinance)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📆 Installation

### 1. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/chat-financeiro.git
cd chat-financeiro
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a `.env` file by copying the example:

```bash
cp .env.example .env
```

Then, add your OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
```

---

## 💡 Usage

Run the chatbot via:

```bash
python main.py
```

Then ask questions like:

```txt
You: What is the current price of AAPL?
You: Quanto está a ação VALE3.SA?
```

To exit, type `exit`, `sair`, or `quit`.

---

## 🗂 Project Structure

```bash
chat-financeiro/
├── main.py              # Entry point - ChatAgent implementation
├── requirements.txt     # Clean production dependencies
├── .env.example         # Environment variable template
├── .gitignore           # Ignores .env, __pycache__, etc.
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

---

## 🔐 Environment Variables

* `OPENAI_API_KEY` – required to access OpenAI models.

---

## 🛡 License

This project is licensed under the [MIT License](LICENSE):

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## 🙌 Contributing

Pull requests are welcome. For major features, please open an issue first to discuss what you would like to change.

---

## 🧠 About

This project was built as part of a Python and AI learning journey focused on building professional-grade tools from scratch.
It serves both as a demonstration of intelligent agent design using LangChain and as a portfolio reference in clean, secure, and tested Python code.

> Built with care by \[Your Name] — [LinkedIn](https://linkedin.com) | [GitHub](https://github.com/YOUR_USERNAME)
