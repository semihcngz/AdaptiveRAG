from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()


urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [WebBaseLoader(url) for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)
docs_splits = text_splitter.split_documents(docs_list)

vektor_store = Chroma.from_documents(
    documents=docs_splits,
    collection_name='rag_chroma',
    embedding=OpenAIEmbeddings(),
    persist_directory='./.chroma' #database nereye kaydedilecek
)

retriever = Chroma(
    collection_name='rag_chroma',
    embedding_function=OpenAIEmbeddings(),
    persist_directory='./.chroma'
).as_retriever()