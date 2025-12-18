import pandas as pd
from tqdm import tqdm  # İlerleme çubuğu (Progress Bar) için
from src.utils import load_json, save_results
from src.generator import generate_response
from src.judge import evaluate_response

def main():
    # 1. HAZIRLIK: Verileri Yükle
    print("📂 Veri setleri yükleniyor...")
    questions = load_json('data/questions.json')
    templates = load_json('data/prompt_templates.json')

    total_ops = len(questions) * len(templates)
    print(f"🚀 TEST BAŞLIYOR: Toplam {total_ops} adet senaryo test edilecek.\n")
    
    results = [] # Sonuçları biriktireceğimiz boş liste

    # 2. DÖNGÜ: Her Soru ve Her Şablon İçin Çalış
    # tqdm(...) komutu terminalde şık bir ilerleme çubuğu gösterir.
    for q in tqdm(questions, desc="Analiz Devam Ediyor"):
        
        for t in templates:
            # A. YARIŞMACI (Generator): Cevabı Üret
            response_text = generate_response(t['template'], q['text'])
            
            # B. HAKEM (Judge): Cevabı Puanla
            score, reason = evaluate_response(q['text'], response_text)
            
            # C. KAYIT: Veriyi listeye ekle
            results.append({
                "Question_ID": q['id'],
                "Category": q['category'],
                "Question_Text": q['text'],
                "Prompt_Name": t['name'],
                "Model_Response": response_text,
                "Score": score,
                "Reason": reason
            })

    # 3. BİTİŞ: Veriyi CSV'ye Kaydet
    print("\n💾 Sonuçlar kaydediliyor...")
    df = pd.DataFrame(results)
    save_results(df)
    
    print("\n✅ MÜKEMMEL! Proje başarıyla tamamlandı.")
    print("📊 Analiz dosyan şurada: data/results.csv")

if __name__ == "__main__":
    main()