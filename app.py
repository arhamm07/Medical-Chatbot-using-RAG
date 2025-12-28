from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings_model
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

os.environ['GROQ_API_KEY'] = GROQ_API_KEY
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

embeddings = download_embeddings_model()

index_name = 'medical-chatbot'
doc_search = PineconeVectorStore.from_existing_index(
    index_name= index_name,
    embedding= embeddings
)


retriever = doc_search.as_retriever(search_type= 'similarity', search_kwargs= {'k' : 3})
llm = ChatGroq(
    model = 'llama-3.1-8b-instant'
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

questoin_answer_chain = create_stuff_documents_chain(
    llm= llm,
    prompt= prompt
)

rag_chain = create_retrieval_chain(
    retriever,
    questoin_answer_chain
)



@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods= ['GET', 'POST'])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    response = rag_chain.invoke({'input' : input})
    print('Response :', response['answer'])
    
    return str(response['answer'])


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 8080, debug= True)