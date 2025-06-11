import pandas as pd
from app.services.preprocessing import preprocess_text

def load_and_prepare_dataset(path='data/info_data_final.xlsx'):
    df = pd.read_excel(path).dropna(subset=['course'])
    df['publications_processed'] = df['pub'].apply(preprocess_text)
    df['course_name_processed'] = df['name'].apply(preprocess_text)
    df['course_processed'] = df['course'].apply(preprocess_text)
    df['Keywords_processed'] = df['Keywords'].apply(preprocess_text)
    df['challenge_level_processed'] = df['Difficulty Category']
    df['combined_features'] = df['course_name_processed'] + " " + df['publications_processed'] + " " + df['Keywords_processed'] + " " + df['challenge_level_processed']
    return df
