import gradio as gr
import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample "standardised phrases"
standard_phrases = [
    "Optimal performance",
    "Utilize resources",
    "Enhance productivity",
    "Conduct an analysis",
    "Maintain a high standard",
    "Implement best practices",
    "Ensure compliance",
    "Streamline operations",
    "Foster innovation",
    "Drive growth",
    "Leverage synergies",
    "Demonstrate leadership",
    "Exercise due diligence",
    "Maximize stakeholder value",
    "Prioritize tasks",
    "Facilitate collaboration",
    "Monitor performance metrics",
    "Execute strategies",
    "Gauge effectiveness",
    "Champion change"
]

# Initialize spaCy for tokenization and word embeddings
nlp = spacy.load("en_core_web_md")

# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(standard_phrases)

def suggest_improvements(input_text):
    # Check if input_text is empty or None
    if not input_text:
        return {"message": "Please provide input text."}

    # Tokenize the input text
    input_doc = nlp(input_text)

    # Extract phrases from the input text
    input_phrases = [phrase.text for phrase in input_doc.noun_chunks]

    suggestions = []
    for input_phrase in input_phrases:
        # Calculate TF-IDF vector for the input phrase
        input_vector = tfidf_vectorizer.transform([input_phrase])

        # Calculate cosine similarities
        cosine_similarities = cosine_similarity(input_vector, tfidf_matrix)

        # Find the most similar standard phrase
        most_similar_index = np.argmax(cosine_similarities)
        similarity_score = cosine_similarities[0][most_similar_index]

        # If similarity is above a threshold, suggest replacement
        if similarity_score > 0.5:
            suggestions.append({
                "Original Phrase": input_phrase,
                "Recommended Replacement": standard_phrases[most_similar_index],
                "Similarity Score": similarity_score
            })

    if suggestions:
        return {"suggestions": suggestions}
    else:
        return {"message": "No suggestions for improvement found."}

# Create a Gradio interface for user input
iface = gr.Interface(
    fn=suggest_improvements,
    inputs=gr.inputs.Textbox(),
    outputs=gr.outputs.JSON(),
    live=True,
    capture_session=True,
    title="Text Improvement Engine"
)

iface.launch()
