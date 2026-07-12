# Oyun Bağımlılığı Risk Tahmini

Bu proje, bireylerin dijital oyun kullanım alışkanlıkları ile psikolojik, sosyal ve davranışsal özelliklerini analiz ederek **oyun bağımlılığı risk seviyesini makine öğrenmesi yöntemleriyle tahmin etmek** amacıyla geliştirilmiştir.

Proje kapsamında veri analizi, veri ön işleme, makine öğrenmesi modellerinin karşılaştırılması, istatistiksel testler ve Streamlit tabanlı web uygulaması geliştirme aşamaları gerçekleştirilmiştir.
## Canlı Uygulama

Uygulamayı çevrim içi olarak incelemek için:

[Streamlit Uygulamasını Aç](https://5bm93d4peycp6kx8jbsn3m.streamlit.app/)
## Risk Seviyeleri

Uygulama, kullanıcıları aşağıdaki dört risk sınıfından biriyle sınıflandırmaktadır:

- Low — Düşük Risk
- Moderate — Orta Risk
- High — Yüksek Risk
- Severe — Ciddi Risk

## Projenin Özellikleri

- Oyun alışkanlıklarının analiz edilmesi
- Psikolojik ve sosyal faktörlerin incelenmesi
- Eksik veri ve aykırı değer işlemleri
- Keşifsel veri analizi ve görselleştirme
- Sınıf dengesizliğinin SMOTE ile giderilmesi
- Üç farklı makine öğrenmesi modelinin karşılaştırılması
- GridSearchCV ile hiperparametre optimizasyonu
- 30 farklı random seed ile model kararlılığı analizi
- McNemar ve Wilcoxon istatistiksel testleri
- Streamlit tabanlı oyun bağımlılığı risk tahmin arayüzü
- Gradio tabanlı alternatif demo arayüzü
- Risk sınıfı ve sınıf olasılıklarının gösterilmesi

## Veri Seti

Projede Kaggle platformundan elde edilen **Gaming and Mental Health** veri seti kullanılmıştır.

Veri seti:

- 1000 katılımcı
- 27 değişken
- Demografik bilgiler
- Oyun oynama alışkanlıkları
- Uyku düzeni
- Akademik ve iş performansı
- Sosyal izolasyon
- Egzersiz alışkanlıkları
- Fiziksel ve psikolojik göstergeler
- Oyun bağımlılığı risk seviyesi

bilgilerini içermektedir.

## Veri Ön İşleme

Modelleme öncesinde aşağıdaki işlemler uygulanmıştır:

- Eksik değerlerin incelenmesi
- Eksik değerlerin ortalama ile doldurulması
- IQR yöntemiyle aykırı değer analizi
- Aykırı değerlerin sınır değerlere çekilmesi
- Gereksiz sütunların veri setinden çıkarılması
- Veri sızıntısı oluşturabilecek değişkenlerin belirlenmesi
- Kategorik değişkenlerin sayısal değerlere dönüştürülmesi
- StandardScaler ile özelliklerin ölçeklendirilmesi
- SMOTE ile sınıf dengesizliğinin giderilmesi
- Verilerin eğitim ve test kümelerine ayrılması

## Kullanılan Modeller

Projede aşağıdaki sınıflandırma algoritmaları karşılaştırılmıştır:

- K-En Yakın Komşu — KNN
- Random Forest
- Lojistik Regresyon

Modellerin hiperparametreleri `GridSearchCV` kullanılarak optimize edilmiştir.

## Model Değerlendirme

Modeller aşağıdaki performans ölçütleri ile değerlendirilmiştir:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Model sonuçlarının kararlılığını değerlendirmek amacıyla eğitim işlemleri 30 farklı random seed ile tekrarlanmıştır.

Modeller arasındaki performans farklarının istatistiksel olarak anlamlı olup olmadığını belirlemek için:

- McNemar testi
- Wilcoxon işaretli sıralama testi

uygulanmıştır.

## Model Sonuçları

| Model | Ortalama Doğruluk |
|---|---:|
| Random Forest | %81.4 |
| Lojistik Regresyon | %80.5 |
| KNN | Daha düşük performans |

Random Forest en yüksek ortalama doğruluğu elde etmiştir. Ancak Random Forest ve Lojistik Regresyon arasında istatistiksel olarak anlamlı bir fark bulunmamıştır.

Lojistik Regresyon modeli:

- Yorumlanabilir olması
- Daha düşük hesaplama maliyetine sahip olması
- Random Forest ile benzer performans göstermesi

nedeniyle final model olarak seçilmiştir.

Final model:

- Eğitim doğruluğu: `%82.2`
- Test doğruluğu: `%80.7`

sonuçlarını elde etmiştir. Eğitim ve test başarılarının birbirine yakın olması, modelde belirgin bir aşırı öğrenme problemi bulunmadığını göstermektedir.

## Streamlit Web Uygulaması

Makine öğrenmesi modeli, kullanıcıların tahmin yapabilmesi için Streamlit tabanlı bir web uygulamasına dönüştürülmüştür.

Uygulama kullanıcıdan:

- Yaş ve cinsiyet
- Oyun oynama süresi
- Tercih edilen oyun türü
- Kullanılan oyun platformu
- Uyku alışkanlıkları
- Akademik veya iş performansı
- Sosyal izolasyon düzeyi
- Egzersiz alışkanlıkları
- Fiziksel belirtiler
- Oyun harcamaları
- Oyun deneyimi

gibi bilgileri almaktadır.

Girilen bilgiler modelin eğitim sürecindeki ön işleme adımlarından geçirilerek oyun bağımlılığı risk seviyesi tahmin edilmektedir.

Uygulama sonucunda:

- Tahmin edilen risk seviyesi
- Low sınıfı olasılığı
- Moderate sınıfı olasılığı
- High sınıfı olasılığı
- Severe sınıfı olasılığı

kullanıcıya gösterilmektedir.

## Model Dosyaları

Streamlit uygulamasında aşağıdaki model bileşenleri kullanılmaktadır:

```text
model.pkl
scaler.pkl
label_encoders.pkl
X_columns.pkl
```

- `model.pkl`: Eğitilmiş final makine öğrenmesi modeli
- `scaler.pkl`: Sayısal özelliklerin ölçeklendirilmesi
- `label_encoders.pkl`: Kategorik değişkenlerin dönüştürülmesi
- `X_columns.pkl`: Modelin beklediği sütun sırasının korunması

## Proje Yapısı

```text
oyun-bagimliligi-risk-tahmini/
├── Makale/
│   └── makale.pdf
├── Rapor/
│   └── rapor.pdf
├── Streamlit/
│   ├── app.py
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── label_encoders.pkl
│   └── X_columns.pkl
├── Veri_Seti/
│   └── Gaming and Mental Health.csv
├── 24100011085_Emre_AYVAZ.ipynb
├── poster.pdf
└── README.md
```

## Kullanılan Teknolojiler

- Python
- Jupyter Notebook ve Google Colab
- Pandas ve NumPy
- Matplotlib ve Seaborn
- Scikit-learn
- Streamlit

## Kurulum

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/emre-ayvaz/oyun-bagimliligi-risk-tahmini.git
cd oyun-bagimliligi-risk-tahmini
```

Gerekli kütüphaneleri yükleyin:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn scipy streamlit gradio joblib jupyter
```

## Notebook'u Çalıştırma

```bash
jupyter notebook 24100011085_Emre_AYVAZ.ipynb
```

## Streamlit Uygulamasını Çalıştırma

Öncelikle Streamlit klasörüne geçin:

```bash
cd Streamlit
```

Ardından uygulamayı başlatın:

```bash
streamlit run app.py
```

Uygulama çalıştırıldıktan sonra tarayıcı üzerinden aşağıdaki adrese erişilebilir:

```text
http://localhost:8501
```

## Proje Belgeleri

Repository içerisinde aşağıdaki proje belgeleri bulunmaktadır:

- Jupyter Notebook
- Veri setleri
- Ayrıntılı proje raporu
- Araştırma makalesi
- Proje posteri
- Streamlit uygulaması
- Eğitilmiş model dosyaları

## Uyarı

Bu proje eğitim ve araştırma amacıyla geliştirilmiştir.

Uygulama tarafından üretilen tahminler tıbbi veya klinik tanı niteliğinde değildir. Kesin değerlendirme için uzman görüşü alınmalıdır.

## Geliştirici

**Emre Ayvaz**

Necmettin Erbakan Üniversitesi  
Mühendislik Fakültesi  
Bilgisayar Mühendisliği Bölümü
