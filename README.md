# SHL Assessment Recommendation Agent

An AI-powered conversational recommendation system that helps recruiters discover relevant SHL assessments based on hiring requirements.

This project uses:

* Retrieval-Augmented Generation (RAG)
* FAISS vector search
* Sentence Transformers embeddings
* Groq LLMs
* FastAPI backend

The assistant can:

* Recommend SHL assessments for hiring roles
* Ask clarifying questions for vague requirements
* Handle conversational refinements
* Compare assessments
* Refuse unrelated/off-topic queries

<br>

# Features

## Conversational Recommendations

The assistant recommends SHL assessments based on:

* Role
* Skills
* Seniority
* Behavioral requirements
* Communication and leadership needs

Example:

```text
Hiring a Java backend developer with communication skills
```

<br>

## Clarification Handling

If the query is too vague, the assistant asks follow-up questions.

Example:

```text
I need an assessment
```

Response:

```text
Could you share the role, seniority level, and important skills you are hiring for?
```

<br>

## Comparison Queries

The system can compare assessments.

Example:

```text
What is the difference between OPQ and Java 8?
```

<br>

## Off-Topic Refusal

The assistant only handles SHL assessment-related queries.

Example:

```text
How do I legally terminate employees?
```

Response:

```text
I can only help with SHL assessments and assessment recommendations.
```

<br>

# Tech Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Backend API     | FastAPI               |
| Vector Database | FAISS                 |
| Embeddings      | Sentence Transformers |
| LLM             | Groq (Llama 3.1)      |
| Web Scraping    | BeautifulSoup         |
| Data Storage    | JSON                  |

<br>

# Project Structure

```text
shl-assessment-agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── rag.py
│   ├── retriever.py
│   ├── models.py
│   ├── prompts.py
│   ├── utils.py
│
├── data/
│   ├── assessments.json
│   ├── clean_assessments.json
│   ├── faiss.index
│   ├── metadata.json
│
├── scraper/
│   ├── scrape_shl.py
│
├── requirements.txt
├── clean_data.py
├── create_embeddings.py
├── .env
│
└── README.md
```

<br>

# How It Works

## 1. Data Collection

The scraper collects SHL assessment information from the SHL product catalog.

Collected information includes:

* Assessment name
* Description
* URL
* Full text content


## 2. Embedding Generation

Assessment content is converted into embeddings using:

```text
all-MiniLM-L6-v2
```


## 3. Vector Search

FAISS is used to retrieve semantically relevant assessments based on user queries.


## 4. LLM Response Generation

Relevant assessments are passed to Groq Llama 3.1 to generate concise conversational responses.

<br>

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/harshkad/SHLRecommendationAgent.git
cd SHLRecommendationAgent
```

<br>

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

<br>

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

<br>

## 4. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

<br>

# Running the Project

## Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

<br>

# API Endpoints

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

<br>

## Chat Endpoint

```http
POST /chat
```

Example Request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java backend developer with communication skills"
    }
  ]
}
```

Example Response:

```json
{
  "reply": "I recommend Java technical and communication-focused assessments.",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com/products/product-catalog/view/java-8-new/",
      "test_type": "Technical"
    }
  ],
  "end_of_conversation": false
}
```

<br>

# Interactive API Docs

FastAPI automatically provides Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

<br>

# Current Capabilities

* Semantic retrieval using FAISS
* Conversational recommendations
* Refinement handling
* Comparison support
* Off-topic refusal
* SHL-only grounded responses
* Structured JSON responses

<br>

# Future Improvements

Potential future enhancements:

* Better reranking
* Hybrid keyword + semantic search
* Persistent FAISS index storage
* Advanced metadata extraction
* Multi-language support
* Deployment optimization
* Evaluation metrics dashboard

---

# Example Queries

```text
Hiring Java backend developer with stakeholder communication
```

```text
Add personality and leadership assessments too
```

```text
What is the difference between OPQ and Java 8?
```

```text
Hiring senior data analyst with SQL and leadership skills
```

---

# Notes

This project is designed as a conversational SHL assessment recommendation system and is intended for educational and evaluation purposes.

The assistant only recommends assessments available in the SHL product catalog.
