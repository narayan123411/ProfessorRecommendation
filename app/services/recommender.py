from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from app.models.dataset_loader import load_and_prepare_dataset
from app.services.preprocessing import preprocess_text

def recommend_professors(text, course_code, challenge_level):
    df = load_and_prepare_dataset()
    filtered = df[df['course'].str.contains(course_code, case=False)]
    filtered = filtered[filtered['Difficulty Category'].str.contains(challenge_level, case=False)]

    if filtered.empty:
        raise ValueError("No matching professors found.")

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(filtered['combined_features'].fillna(''))

    user_vector = tfidf.transform([preprocess_text(text + " " + challenge_level)])
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()

    filtered['Cosine Similarity'] = similarity_scores
    features = filtered[['Cosine Similarity', 'Course Difficulty Index','SFI','PEI']].fillna(0)
    features['Cosine Similarity'] *= 2

    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
    knn.fit(scaled)
    distances, indices = knn.kneighbors(scaled)

    results = filtered.iloc[indices[0]]
    results = results[results['Cosine Similarity'] > 0]
    return results[['name', 'course', 'Cosine Similarity', 'SFI', 'PEI']]
