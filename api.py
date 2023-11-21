from fastapi import FastAPI, HTTPException, Query
from sklearn.metrics.pairwise import cosine_similarity
from vectorize import vectorize_text
from data_preprocessing import preprocess_data

# Assuming the dataset is in the same directory as the script
data_file_path = 'bigBasketProducts.csv'

# Load and preprocess data
data = preprocess_data(data_file_path)

# Vectorize preprocessed data
tfidf_vectorizer, tfidf_matrix = vectorize_text(data)

app = FastAPI()

@app.get("/query/")
async def query_engine(query: str = Query(..., description="Query text to find similar product description")):
    try:
        query_vector = tfidf_vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
        most_similar_idx = cosine_similarities.argsort()[-1]
        return {"response": data.iloc[most_similar_idx]['processed_description']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
