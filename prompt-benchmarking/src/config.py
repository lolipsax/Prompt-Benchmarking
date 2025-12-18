import os
from dotenv import load_dotenv
from openai import OpenAI

# .env dosyasını yükle
load_dotenv()

# API Anahtarını kontrol et
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("HATA: .env dosyasında OPENAI_API_KEY bulunamadı!")

# İstemciyi (Client) başlat
client = OpenAI(api_key=api_key)

# Model Ayarları
GENERATOR_MODEL = "gpt-3.5-turbo"  # Soruları cevaplayan model (Yarışmacı)
JUDGE_MODEL = "gpt-4o"             # Puanlayan model (Hakem)