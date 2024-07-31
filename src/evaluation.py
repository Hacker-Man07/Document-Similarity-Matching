from typing import List, Dict

def evaluate(results: List[Dict[str, str]]):
    
    for result in results:
        print(f"Input Invoice: {result['input_invoice']}")
        print(f"Most Similar Invoice: {result['most_similar_invoice']}")
        print(f"Similarity Score: {result['similarity_score']}\n")
