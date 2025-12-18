import json
from src.config import client, JUDGE_MODEL

def evaluate_response(user_input, model_response):
    """
    Orijinal soruyu ve modelin cevabını alır.
    GPT-4o (Hakem) kullanarak 1-100 arası puanlar.
    Sonucu JSON formatında döndürür.
    """
    
    # Hakeme ne yapacağını anlatan 'Sistem Komutu'
    system_prompt = """
    Sen tarafsız ve titiz bir 'Yapay Zeka Değerlendirme Uzmanı'sın.
    Görevin: Verilen soruya modelin verdiği cevabı analiz etmek.
    
    Kriterlerin:
    1. Doğruluk (Cevap yanlış bilgi içeriyor mu?)
    2. Talimata Uygunluk (Prompttaki kısıtlamalara uydu mu?)
    3. Netlik (Gereksiz uzatmış mı?)
    
    Çıktını KESİNLİKLE aşağıdaki JSON formatında ver:
    {
        "score": (0-100 arası bir sayı),
        "reason": "Puanı neden verdiğine dair kısa, tek cümlelik açıklama."
    }
    """

    # Hakeme gönderilecek vaka dosyası
    user_prompt = f"""
    SORU: {user_input}
    
    MODELİN CEVABI:
    {model_response}
    
    Lütfen değerlendirmeni yap.
    """

    try:
        response = client.chat.completions.create(
            model=JUDGE_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0,  # Hakem duygusal olmamalı, tutarlı olmalı.
            response_format={"type": "json_object"} # KRİTİK: Çıktıyı JSON olmaya zorlar.
        )
        
        # Gelen metni (String) Python sözlüğüne (Dictionary) çevir
        content = response.choices[0].message.content
        result = json.loads(content)
        
        return result['score'], result['reason']

    except Exception as e:
        print(f"⚠️ Hata oluştu (Judge): {e}")
        return 0, "Değerlendirme Hatası"