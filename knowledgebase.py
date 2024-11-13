from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from phi.vectordb.pgvector import PgVector2
from phi.embedder.azure_openai import AzureOpenAIEmbedder

embeddings = AzureOpenAIEmbedder()

#create a knowledge base containing literatue about molecular interactions
interaction_knowledge_base = PDFKnowledgeBase(
    path="PDF/molecular_interactions",
    vector_db=PgVector2(
        collection="molecular_interactions",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        embedder=embeddings,
        ),
        reader=PDFReader(chunk=True),
)

#create a knowledge base containing literature about the RFB review
rfb_knowledge_base = PDFKnowledgeBase(
    path="PDF/rfb",
    vector_db=PgVector2(
        collection="pdf_documents_rfbreview",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        embedder=embeddings,
    ),
    reader=PDFReader(chunk=True),
)

if __name__ == "__main__":
    interaction_knowledge_base.load(recreate=False)
    rfb_knowledge_base.load(recreate=False)

