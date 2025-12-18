import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_results():
    # 1. Veriyi Yükle
    csv_path = 'data/results.csv'
    if not os.path.exists(csv_path):
        print("❌ HATA: results.csv dosyası bulunamadı! Önce main.py'yi çalıştır.")
        return

    df = pd.read_csv(csv_path)
    
    # Puanları sayıya çevirmeyi garantiye al (Hata önleyici)
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')

    # Grafik Ayarları (LinkedIn için şık görünüm)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(14, 10))

    # --- GRAFİK 1: GENEL PERFORMANS SIRALAMASI ---
    plt.subplot(2, 1, 1) # Sayfayı ikiye böl, üsttekini seç
    
    # Ortalamayı hesapla ve sırala
    avg_scores = df.groupby('Prompt_Name')['Score'].mean().sort_values(ascending=False).reset_index()
    
    # Çizim
    sns.barplot(x='Score', y='Prompt_Name', data=avg_scores, palette='viridis', hue='Prompt_Name', legend=False)
    plt.title('Hangi Prompt Tekniği Daha Başarılı? (Ortalama Puan)', fontsize=16, fontweight='bold')
    plt.xlabel('Ortalama Puan (0-100)', fontsize=12)
    plt.ylabel('')
    plt.xlim(0, 100) # X eksenini 0-100 arası sabitle
    
    # Çubukların ucuna puanları yaz
    for index, row in avg_scores.iterrows():
        plt.text(row.Score + 1, index, f"{row.Score:.1f}", va='center', fontweight='bold')

    # --- GRAFİK 2: KATEGORİ BAZLI ISI HARİTASI (HEATMAP) ---
    plt.subplot(2, 1, 2) # Alttaki alanı seç
    
    # Pivot Tablo Oluştur (Satır: Prompt, Sütun: Kategori, Değer: Puan)
    pivot_table = df.pivot_table(index='Prompt_Name', columns='Category', values='Score', aggfunc='mean')
    
    # Isı haritası çiz
    sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="RdYlGn", linewidths=.5)
    plt.title('Hangi Teknik Hangi Görevde İyi? (Heatmap Analysis)', fontsize=16, fontweight='bold')
    plt.ylabel('')
    plt.xlabel('Soru Kategorisi')

    # --- KAYDETME ---
    plt.tight_layout()
    output_path = 'data/final_analysis.png'
    plt.savefig(output_path, dpi=300) # Yüksek kalite kaydet
    print(f"📊 Grafikler oluşturuldu ve kaydedildi: {output_path}")
    
    # --- KONSOL RAPORU ---
    print("\n🏆 --- KAZANAN TEKNİKLER --- 🏆")
    print(avg_scores)
    print("\n💡 Mimarın Yorumu: En yüksek puanı alan teknik, genel kullanım için en güvenilir olandır.")

if __name__ == "__main__":
    analyze_results()