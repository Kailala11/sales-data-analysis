# Analisis Data Penjualan & Visualisasi

Proyek analisis data penjualan komprehensif yang mengeksplorasi tren pendapatan, performa produk, dan pola perilaku pelanggan menggunakan Python dan teknik visualisasi data.

## Ringkasan Proyek

Proyek ini mendemonstrasikan kemampuan analisis data end-to-end, mulai dari pembuatan dan pembersihan data hingga analisis eksploratori dan menghasilkan insight bisnis yang actionable. Analisis mencakup data penjualan selama 2 tahun (2023-2024) dengan lebih dari 4.300 transaksi di berbagai kategori produk dan wilayah.

## Temuan Utama

### Performa Bisnis
- **Total Pendapatan**: Rp 3.44 Juta
- **Total Pesanan**: 4.309 transaksi
- **Rata-rata Nilai Pesanan**: Rp 799
- **Tingkat Pelanggan Berulang**: 82.8%
- **Pertumbuhan YoY**: 0.9% (2024 vs 2023)

### Performa Terbaik
- **Kategori Terbaik**: Electronics (54.9% dari pendapatan)
- **Produk Teratas**: Smartwatch (Pendapatan Rp 366K)
- **Wilayah Terdepan**: Makassar (18.2% dari penjualan)
- **Hari Puncak**: Rabu

## Teknologi yang Digunakan

- **Python 3.x**
  - `pandas` - Manipulasi dan analisis data
  - `numpy` - Komputasi numerik
  - `matplotlib` - Visualisasi statis
  - `seaborn` - Visualisasi data statistik
  
- **Alat Analisis Data**
  - Exploratory Data Analysis (EDA)
  - Analisis Statistik
  - Analisis Time Series
  - Segmentasi Pelanggan

## Struktur Proyek

```
sales-data-analysis/
├── data/
│   └── sales_data.csv                 # Dataset penjualan (4.309 transaksi)
├── scripts/
│   ├── generate_sales_data.py         # Script untuk generate dataset
│   ├── sales_analysis.py              # Script analisis utama
│   └── create_visualizations.py       # Script untuk membuat visualisasi
├── visualizations/
│   ├── dashboard_overview.png         # Dashboard overview utama
│   ├── customer_analysis.png          # Analisis perilaku pelanggan
│   ├── sales_heatmap.png             # Heatmap pola penjualan
│   └── performance_trends.png         # Tren performa kuartalan
├── results/
│   ├── monthly_sales_summary.csv      # Ringkasan penjualan bulanan
│   ├── product_performance.csv        # Performa produk
│   └── category_performance.csv       # Performa kategori
└── README.md                          # Dokumentasi proyek
```

## Analisis yang Dilakukan

### 1. Analisis Tren Bulanan
Mengidentifikasi pola penjualan bulanan untuk memahami musiman dan tren pertumbuhan:
- Juni 2023 mencatatkan pendapatan tertinggi (Rp 231.356)
- Tren penjualan menunjukkan kestabilan dengan pertumbuhan moderat
- Peningkatan signifikan pada bulan Juni-Juli (musim liburan)

### 2. Analisis Produk
Evaluasi mendalam terhadap performa produk:
- Top 10 produk berkontribusi 65% dari total pendapatan
- Kategori Electronics mendominasi dengan 6 produk di top 10
- Smartwatch menjadi produk terlaris dengan 483 unit terjual

### 3. Pola Pembelian Pelanggan
Menganalisis kapan dan bagaimana pelanggan berbelanja:
- Hari Rabu memiliki pendapatan tertinggi (Rp 532.989)
- Pola pembelian relatif konsisten sepanjang minggu
- Pelanggan Premium dan Regular berkontribusi 90% dari pendapatan

### 4. Segmentasi Pelanggan
Analisis perilaku berdasarkan segmen pelanggan:
- Segmen Regular: 2.573 pesanan (60% dari total)
- Segmen Premium: 1.284 pesanan dengan AOV tertinggi (Rp 814)
- Segmen VIP: 452 pesanan dengan diskon rata-rata 15%

### 5. Analisis Regional
Performa penjualan berdasarkan wilayah:
- Distribusi cukup merata antar 6 wilayah (13-18% per wilayah)
- Makassar memimpin dengan 18.2% dari total penjualan
- Potensi pertumbuhan di wilayah Bandung (13.8%)

## Visualisasi

### Dashboard Overview
Menampilkan metrik utama bisnis termasuk:
- Tren pendapatan bulanan (line chart)
- Top 10 produk berdasarkan revenue (horizontal bar chart)
- Distribusi pendapatan per kategori (pie chart)

### Customer Analysis
Analisis mendalam tentang perilaku pelanggan:
- Perbandingan revenue antar wilayah
- Pola penjualan berdasarkan hari dalam seminggu
- Performa segmen pelanggan
- Preferensi metode pembayaran

### Sales Heatmap
Visualisasi pola penjualan dalam format heatmap untuk mengidentifikasi:
- Hari dan bulan dengan penjualan tertinggi
- Pola musiman dalam data
- Waktu optimal untuk kampanye marketing

### Performance Trends
Analisis tren performa bisnis:
- Pendapatan per kuartal
- Perbandingan year-over-year
- Jumlah pesanan dan pendapatan

## Rekomendasi Bisnis

Berdasarkan hasil analisis, berikut rekomendasi strategis:

1. **Optimasi Inventory**
   - Fokus pada kategori Electronics yang menghasilkan 54.9% revenue
   - Tingkatkan stok Smartwatch, Laptop, dan Headphones
   - Monitor performa produk di kategori Books (hanya 2% revenue)

2. **Strategi Marketing**
   - Jalankan promosi khusus di hari Senin-Selasa untuk meningkatkan penjualan
   - Manfaatkan momentum penjualan tinggi di bulan Juni-Juli
   - Fokuskan campaign di wilayah Makassar dan Surabaya

3. **Program Loyalitas**
   - Tingkatkan repeat rate yang sudah baik (82.8%)
   - Buat program khusus untuk mengkonversi Regular ke Premium
   - Berikan benefit eksklusif untuk VIP customer

4. **Pengembangan Produk**
   - Ekspansi kategori Electronics dengan produk komplementer
   - Evaluasi ulang strategi untuk kategori Books
   - Pertimbangkan bundling produk populer

5. **Ekspansi Regional**
   - Tingkatkan penetrasi di Bandung yang masih relatif rendah
   - Replikasi strategi sukses Makassar ke wilayah lain
   - Sesuaikan inventory per wilayah berdasarkan preferensi lokal

## Cara Menjalankan Proyek

### Prerequisites
```bash
# Install required packages
pip install pandas numpy matplotlib seaborn
```

### Generate Dataset
```bash
python generate_sales_data.py
```

### Jalankan Analisis
```bash
python sales_analysis.py
```

### Buat Visualisasi
```bash
python create_visualizations.py
```

## Hasil Output

Setelah menjalankan seluruh script, Anda akan mendapatkan:

1. **Data Files**
   - `sales_data.csv` - Dataset utama
   - `monthly_sales_summary.csv` - Ringkasan bulanan
   - `product_performance.csv` - Performa produk
   - `category_performance.csv` - Performa kategori

2. **Visualizations**
   - `dashboard_overview.png` - Dashboard utama
   - `customer_analysis.png` - Analisis pelanggan
   - `sales_heatmap.png` - Heatmap penjualan
   - `performance_trends.png` - Tren performa

3. **Console Output**
   - Statistik lengkap dan insight bisnis
   - Rekomendasi strategis
   - Key findings dari analisis

## Skills yang Didemonstrasikan

- Data Cleaning dan Preprocessing
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Data Visualization
- Business Intelligence
- Python Programming
- Data Storytelling
- Insight Generation

## Pengembangan Lebih Lanjut

Potensi pengembangan proyek ini:

1. **Predictive Analytics**
   - Forecasting penjualan menggunakan Time Series
   - Prediksi churn customer
   - Rekomendasi produk berbasis Machine Learning

2. **Advanced Visualization**
   - Dashboard interaktif dengan Plotly/Dash
   - Real-time monitoring dashboard
   - Geographic visualization dengan peta

3. **Deep Dive Analysis**
   - Cohort analysis untuk customer retention
   - Market basket analysis
   - Customer Lifetime Value (CLV) calculation
   - RFM Analysis (Recency, Frequency, Monetary)

4. **Integration**
   - Koneksi ke database (PostgreSQL/MySQL)
   - API untuk data real-time
   - Export otomatis ke Excel/PowerPoint

## Kontak

Jika Anda tertarik dengan proyek ini atau ingin berdiskusi lebih lanjut:

- LinkedIn: [Your LinkedIn Profile]
- Email: your.email@example.com
- Portfolio: [Your Portfolio Website]

---

**Note**: Dataset yang digunakan dalam proyek ini adalah data sintetis yang dibuat untuk keperluan demonstrasi dan pembelajaran.
