# 📊 Data-Driven Prompt Benchmarking Tool

> **"Prompt Engineering should not be an art; it must be a science."**

This project is an automated framework designed to scientifically evaluate and compare different prompt engineering techniques using an **LLM-as-a-Judge** architecture. Instead of relying on subjective "feelings," this tool generates empirical data to determine which prompting strategy yields the highest quality outputs.

## 🚀 Key Features

* **Automated Pipeline:** Tests 5 distinct prompting strategies against a stress-test dataset (Logic, Coding, Creative).
* **LLM-as-a-Judge Architecture:** Uses **GPT-4o** to act as an impartial judge, scoring responses from **GPT-3.5-turbo** based on accuracy, instruction following, and conciseness.
* **Structured Outputs:** Enforces `JSON Mode` for robust and parsable evaluation metrics.
* **Data Visualization:** Automatically generates heatmaps and bar charts to visualize performance differences.

## 🧪 Experiment Methodology

The system tests the following prompting techniques:

1.  **The Naked Prompt:** (Control Group) No instructions, raw input.
2.  **The Persona Architect:** Role-prompting (e.g., "You are an expert...").
3.  **Chain-of-Thought (CoT):** Forcing step-by-step reasoning.
4.  **The Tip Motivation:** Reward/penalty mechanism (e.g., "I will tip you $200").
5.  **Structured Delimiter:** Strict formatting constraints.

## 📂 Project Structure

```bash
prompt-benchmarking/
├── src/
│   ├── generator.py   # Generates responses using GPT-3.5
│   ├── judge.py       # Evaluates responses using GPT-4o (0-100 Score)
│   ├── analysis.py    # Visualizes data with Seaborn/Matplotlib
│   └── config.py      # API configurations
├── data/
│   ├── questions.json # Stress-test dataset (Logic, Coding, etc.)
│   └── results.csv    # Benchmark outputs
├── main.py            # Orchestrator
└── .env               # API Keys
