# strands-vs-langchain

Companion repo for the article **"AWS Strands Agents vs LangChain: A Practical Guide to Choosing the Right Framework."**

Same two agents, built twice — once in each framework — so you can run them side by side and feel the difference in boilerplate and control flow for yourself.

## Structure

```
strands/
  weather_agent.py       # minimal single-tool agent
  multi_tool_agent.py     # weather + currency conversion
langchain/
  weather_agent.py       # same task, LangChain version
  multi_tool_agent.py     # same task, LangChain version
```

## Setup

```bash
# Strands
pip install strands-agents
python strands/weather_agent.py

# LangChain
pip install langchain langchain-openai
export OPENAI_API_KEY=your_key_here
python langchain/weather_agent.py
```

## Why this repo exists

Read the full breakdown in the article — this repo is here so you don't have to take the comparison on faith. Clone it, run both, and see which control-flow model feels right for your use case.
