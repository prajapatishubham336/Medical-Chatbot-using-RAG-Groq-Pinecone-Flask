# Medical-Chatbot-using-RAG-Groq-Pinecone-Flask
AI-powered Medical Chatbot using RAG, LangChain, Groq, Pinecone, HuggingFace Embeddings, and Flask for intelligent medical question answering from PDF documents.


A Retrieval-Augmented Generation (RAG) based Medical Chatbot that answers medical questions by retrieving relevant information from medical PDF documents using Pinecone Vector Database and generating responses with Groq Llama 3.3 70B.

---

## 📌 Features

- Upload medical knowledge from PDF files
- PDF text extraction using PyPDF
- Text chunking using LangChain
- Semantic embeddings using HuggingFace
- Pinecone Vector Database for fast retrieval
- Groq Llama 3.3 70B for response generation
- Retrieval-Augmented Generation (RAG)
- Flask-based web interface
- Intelligent fallback to LLM when required information is not available in the PDF
- Fast and accurate semantic search

---

## 🛠️ Tech Stack

- Python
- Flask
- LangChain
- Groq API
- Pinecone
- HuggingFace Embeddings
- Sentence Transformers
- PyPDF
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
Medical-Chatbot/
│
├── app.py
├── store_index.py
├── requirement.txt
├── setup.py
├── .env
│
├── Data/
│
├── src/
│   ├── __init__.py
│   ├── helper.py
│   └── prompt.py
│
├── templates/
│   └── chat.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── research/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Medical-Chatbot.git

cd Medical-Chatbot
```

---

### Create Virtual Environment

```bash
conda create -n medicalbot python=3.10

conda activate medicalbot
```

---

### Install Dependencies

```bash
pip install -r requirement.txt
```

---

### Configure Environment Variables

Create a **.env** file.

```env
PINECONE_API_KEY=YOUR_PINECONE_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

### Upload Documents to Pinecone

```bash
python store_index.py
```

---

### Run Application

```bash
python app.py
```

Open

```
http://127.0.0.1:8080
```

---

## 🧠 Workflow

```
Medical PDF
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
HuggingFace Embeddings
      │
      ▼
Pinecone Vector Database
      │
      ▼
Retriever
      │
      ▼
Groq Llama 3.3 70B
      │
      ▼
Medical Answer
```


## 💡 Example Questions

- What is Diabetes?
- What is Depression?
- Explain Acromegaly.
- What are the symptoms of Hypothyroidism?
- Explain Cushing Syndrome.
- What is Cortisol?
- What is Thyroid Gland?
- What is Acne?

---

## 📦 Requirements

- Python 3.10+
- Groq API Key
- Pinecone API Key

---

## 📚 References

- LangChain Documentation – https://python.langchain.com/docs/introduction/
- Groq API Documentation – https://console.groq.com/docs/
- Pinecone Documentation – https://docs.pinecone.io/
- Hugging Face Documentation – https://huggingface.co/docs
- Sentence Transformers (all-MiniLM-L6-v2) – https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- Flask Documentation – https://flask.palletsprojects.com/
- PyPDF Documentation – https://pypdf.readthedocs.io/
---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Shubham Prajapati**

GitHub: https://github.com/prajapatishubham336
