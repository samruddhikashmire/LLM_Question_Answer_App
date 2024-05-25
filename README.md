# Streamlit Question and Answer System

This project is a Streamlit application that generates random questions based on selected topics and verifies user answers using the `ollama` API.

## Features

- Generate random questions in three categories: Geography, Health, and Sports.
- Verify user-provided answers to the generated questions.
- Persistent state management using `st.session_state` to maintain the generated question and verification result across interactions.

## Requirements

- Python 3.7 or higher
- Streamlit
- Ollama API (with access to the `llama2` model)

