# AI Resume Analyzer (Generative AI Project)

## Overview
AI-powered resume analysis system built using FastAPI and Large Language Models. The application analyzes resumes and provides skill insights, strengths, and improvement suggestions.

## Features
- Resume skill extraction
- AI-powered feedback
- Job role recommendations
- REST API architecture
- Dockerized deployment

## Tech Stack
- Python
- FastAPI
- OpenAI API
- Docker

## Architecture
User Input → FastAPI API → LLM Processing → Structured Analysis

## Installation

```bash
pip install -r requirements.txt
uvicorn app:app --reload
