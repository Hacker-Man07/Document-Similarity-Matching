from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, Set

def calculate_cosine_similarity(doc1: str, doc2: str) -> float:
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([doc1, doc2])
    return cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

def calculate_jaccard_similarity(set1: Set[str], set2: Set[str]) -> float:
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0

def calculate_feature_similarity(features1: Dict[str, str], features2: Dict[str, str]) -> float:
    score = 0
    if features1['invoice_number'] == features2['invoice_number']:
        score += 1
    if features1['date'] == features2['date']:
        score += 1
    if features1['amount'] == features2['amount']:
        score += 1
    if features1['addresses'] == features2['addresses']:
        score += 0.5
    if features1['phone_numbers'] == features2['phone_numbers']:
        score += 0.5
    if features1['email_addresses'] == features2['email_addresses']:
        score += 0.5
    return score / 4.5  # Normalizing the score to be between 0 and 1

def calculate_combined_similarity(doc1: str, doc2: str, features1: Dict[str, str], features2: Dict[str, str]) -> float:
    cosine_sim = calculate_cosine_similarity(doc1, doc2)
    feature_sim = calculate_feature_similarity(features1, features2)
    jaccard_sim = calculate_jaccard_similarity(set(features1['items'].split()), set(features2['items'].split()))
    return 0.4 * cosine_sim + 0.4 * feature_sim + 0.2 * jaccard_sim
