from src.config import client, GENERATOR_MODEL

def generate_response(prompt_template, user_input):
    """
    Belirli bir prompt şablonunu ve kullanıcı sorusunu birleştirip 
    OpenAI API'dan cevap alır.
    """
    
    # 1. Promptu İnşa Et (Şablondaki {input} yerine soruyu koy)
    full_prompt = prompt_template.replace("{input}", user_input)
    
    try:
        # 2. API Çağrısı Yap
        response = client.chat.completions.create(
            model=GENERATOR_MODEL,
            messages=[
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.7 # Yaratıcılık dengesi
        )
        
        # 3. Cevabı Döndür
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"⚠️ Hata oluştu (Generator): {e}")
        return "HATA"