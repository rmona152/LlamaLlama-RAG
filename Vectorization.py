from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 

DATA_PATH = 'data/'
DB_FAISS_PATH = 'vectorstore/db_faiss'

#Create Vector DB
def CreateVectorDB():
    loader = DirectoryLoader(DATA_PATH,glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                   chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name='cognitivecomputations/dolphin-2.8-mistral-7b-v02',
                                       model_kwargs={'device': 'cpu'})
    db =FAISS.from_documents(texts,embeddings)
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    print("Vector Database creation in progress.")
    #CreateVectorDB()
