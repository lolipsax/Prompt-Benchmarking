import json
import os

def load_json(filepath):
    """Verilen dosya yolundaki JSON verisini okur ve döndürür."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dosya bulunamadı: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_results(df, filepath="data/results.csv"):
    """Sonuçları CSV olarak kaydeder."""
    df.to_csv(filepath, index=False)
    print(f"✅ Sonuçlar kaydedildi: {filepath}")