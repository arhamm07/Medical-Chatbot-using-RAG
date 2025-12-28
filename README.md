# 🏥 Medical Chatbot with RAG

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Framework: Flask](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![LLM: Llama-3.1-8B](https://img.shields.io/badge/LLM-Llama--3.1--8B-orange)](https://groq.com/)

A production-ready Medical Chatbot powered by Retrieval-Augmented Generation (RAG) that provides accurate and reliable medical information from trusted sources.

## ✨ Features

- **AI-Powered Medical Assistance**: Get instant responses to medical queries using state-of-the-art language models
- **Knowledge-Based**: Grounded in medical literature for accurate information
- **Real-time Chat Interface**: Modern, responsive web interface with typing indicators
- **Scalable Architecture**: Built with production-grade technologies
- **Privacy-Focused**: Local processing of sensitive medical queries

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **AI/ML**: 
  - LangChain for RAG pipeline
  - Groq API (Llama 3.1 8B) for text generation
  - BAAI/bge-small-en for document embeddings
- **Vector Database**: Pinecone for efficient similarity search
- **Frontend**: HTML5, CSS3, JavaScript (jQuery)
- **Deployment**: Container-ready with Docker

## 📦 Prerequisites

- Python 3.8+
- Pinecone API Key
- Groq API Key
- pip (Python package manager)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- [Pinecone](https://www.pinecone.io/) account (for vector database)
- [Groq](https://groq.com/) API key (for LLM access)
- Git (for version control)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/arhamm07/Medical-Chatbot-using-RAG.git
   cd Medical-Chatbot-using-RAG
   ```

2. **Set up a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory with your API keys:
   ```env
   # Required
   GROQ_API_KEY=your_groq_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   
   # Optional: Customize these if needed
   PINECONE_ENVIRONMENT=us-east-1  # Default Pinecone region
   MODEL_NAME=llama-3.1-8b-instant  # Default model
   ```

5. **Run the application**
   ```bash
   python app.py
   ```
   The application will be available at `http://localhost:8080`

### Docker Setup (Alternative)

```bash
# Build the Docker image
docker build -t medical-chatbot .

# Run the container
docker run -p 8080:8080 --env-file .env medical-chatbot
```

## 📚 Knowledge Base Management

The chatbot uses PDF documents stored in the `data/` directory as its knowledge base. The system is pre-configured to work with `Medical_book.pdf`.

### Adding New Documents
1. Place your PDF files in the `data/` directory
2. Run the indexing script:
   ```bash
   python store_index.py
   ```
   This will process all PDFs in the directory and update the vector store.

### Document Requirements
- Supported format: PDF
- Recommended size: Up to 100MB per file
- For best results, ensure documents have clear structure and formatting

### Updating Existing Documents
1. Replace the existing PDF file in the `data/` directory
2. Delete the existing index in Pinecone (or use a new index name)
3. Run the indexing script again

## 🏗️ Project Structure

```
├── app.py                # Main application entry point
├── requirements.txt      # Python dependencies
├── store_index.py        # Vector database indexing script
├── data/                 # Medical documents (PDFs)
│   └── Medical_book.pdf  # Primary knowledge source
├── src/
│   ├── helper.py         # Document processing utilities
│   └── prompt.py         # System prompts and templates
├── static/               # Frontend assets
│   └── style.css         # Styling
└── templates/            # HTML templates
    └── chat.html         # Chat interface
```

## 🤖 Architecture Overview

### System Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│   User Query    ├────>│  Web Interface  ├────>│  Flask Backend  │
│                 │     │                 │     │                 │
└─────────────────┘     └────────┬────────┘     └────────┬────────┘
                                 │                       │
                                 │                       ▼
                                 │           ┌─────────────────────┐
                                 │           │   Query Embedding   │
                                 │           └──────────┬──────────┘
                                 │                      │
                                 │           ┌──────────▼──────────┐
                                 │           │  Pinecone Vector    │
                                 │           │       Store         │
                                 │           └──────────┬──────────┘
                                 │                      │
                                 │           ┌──────────▼──────────┐
                                 └───────────┤  Retrieve Relevant  │
                                             │       Chunks        │
                                             └──────────┬──────────┘
                                                        │
                                             ┌──────────▼──────────┐
                                             │   LLM (Llama 3.1)   │
                                             └──────────┬──────────┘
                                                        │
                                             ┌──────────▼──────────┐
                                             │   Generate & Format  │
                                             │      Response       │
                                             └──────────┬──────────┘
                                                        │
                                                        ▼
```


### Key Components

1. **Document Processing Pipeline**
   - PDF loading and text extraction
   - Text chunking (1000 characters with 200-character overlap)
   - Embedding generation using BAAI/bge-small-en model
   - Vector storage in Pinecone

2. **Query Processing**
   - Query embedding using the same BAAI model
   - Semantic search to find most relevant document chunks
   - Context-aware response generation using Llama 3.1
   - Response formatting and delivery

3. **Performance**
   - Average response time: < 2 seconds
   - Supports concurrent users (limited by Groq API rate limits)
   - Efficient document retrieval with Pinecone's approximate nearest neighbor search

## 🛠️ Development

### Running Tests
```bash
# Install test dependencies
pip install -r tests/requirements.txt

# Run tests
pytest
```

### Code Style
This project follows PEP 8 style guidelines. Please run the following before committing:
```bash
# Auto-format code
black .

# Check for style issues
flake8
```

### Versioning
We use [SemVer](https://semver.org/) for versioning. For the versions available, see the [releases](https://github.com/arhamm07/Medical-Chatbot-using-RAG/releases).

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Reporting Issues
Please use the [issue tracker](https://github.com/arhamm07/Medical-Chatbot-using-RAG/issues) to report any bugs or suggest new features.

## 📄 Documentation

For detailed documentation, please refer to the [docs](docs/) directory.

## 👥 Team

- **Arham Rafique** - [@arhamm07](https://github.com/arhamm07)

## 🙏 Acknowledgments

- Built with [LangChain](https://python.langchain.com/)
- Powered by [Groq](https://groq.com/) and [Pinecone](https://www.pinecone.io/)
- Thanks to all contributors who have helped improve this project
