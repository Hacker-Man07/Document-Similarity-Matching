import os
from text_extraction import extract_text_from_pdf
from feature_extraction import extract_features
from similarity import calculate_combined_similarity
from database import InvoiceDatabase
from evaluation import evaluate

def load_invoices_from_directory(directory: str, db: InvoiceDatabase):
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return
    
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")
            text = extract_text_from_pdf(file_path)
            features = extract_features(text)
            db.add_invoice({
                'filename': filename,
                'text': text,
                'features': features
            })

def main(training_directory: str, testing_directory: str):
    db = InvoiceDatabase()
    load_invoices_from_directory(training_directory, db)

    results = []
    if not os.path.exists(testing_directory):
        print(f"Directory does not exist: {testing_directory}")
        return
    
    for filename in os.listdir(testing_directory):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(testing_directory, filename)
            input_text = extract_text_from_pdf(file_path)
            input_features = extract_features(input_text)

            max_similarity = 0
            most_similar_invoice = None
            for invoice in db.get_all_invoices():
                similarity = calculate_combined_similarity(input_text, invoice['text'], input_features, invoice['features'])
                if similarity > max_similarity:
                    max_similarity = similarity
                    most_similar_invoice = invoice

            results.append({
                'input_invoice': filename,
                'most_similar_invoice': most_similar_invoice['filename'] if most_similar_invoice else None,
                'similarity_score': max_similarity
            })

    evaluate(results)

if __name__ == "__main__":
    main("data/training/", "data/testing/")
