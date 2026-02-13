from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# FAQs
faqs = [
    {"question": "How do I reset my password?", "answer": "Click on 'Forgot Password' to reset."},
    {"question": "How can I contact support?", "answer": "Email support@example.com"}
]

# Encode FAQ questions
faq_questions = [faq["question"] for faq in faqs]
faq_embeddings = model.encode(faq_questions)

# User query
query = "I forgot my login password"
query_embedding = model.encode([query])

# Similarity calculation
similarities = cosine_similarity(query_embedding, faq_embeddings)[0]

# Best match
best_idx = np.argmax(similarities)
best_score = similarities[best_idx]

# Threshold check
if best_score > 0.6:
    print("Answer:", faqs[best_idx]["answer"])
else:
    print("Sorry, I couldn't find a relevant answer.")
