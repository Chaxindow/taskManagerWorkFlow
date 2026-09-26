![CI](https://github.com/Chaxindow/taskManagerWorkFlow/actions/workflows/ci.yml/badge.svg)

# Task Manager CLI Projesi

Bu proje, Python ile geliştirilmiş, tip güvenli (type-safe) bir görev yöneticisi kütüphanesidir. Komut satırından (CLI) görev ekleyebilir, listelebilir ve tamamlanabilir.

## 🚀 Hızlı Başlangıç

### 1. Kurulum

Projeyi klonlayın ve sanal ortam (venv) oluşturup aktif edin.

```bash
git clone https://github.com/Chaxindow/taskManagerWorkFlow.git
cd taskManagerWorkFlow
python -m venv .venv
.\.venv\Scripts\activate  # Windows

# Gerekli paketleri kurun
pip install -e ".[dev]"
```

### 2. Çalıştırma

Proje, `task_manager_cli.py` dosyası aracılığıyla kullanılır.

```bash
# Görev ekleme
python task_manager_cli.py add "Alışverişe git"

# Görevleri listeleme
python task_manager_cli.py list

# Görev tamamlama
python task_manager_cli.py done 1
```

## 🛠️ Geliştirme Kuralları

Bu proje, yazılım mühendisliği prensiplerine uygun olarak geliştirilmiştir. Lütfen aşağıdaki kurallara uyun:

### 1. Git Kullanımı (Commit Mesajları)

- Her commit mesajı **İngilizce** olmalıdır.
- Mesajlar kısa ve açıklayıcı olmalıdır.
- commit mesaji  içinde **Türkçe karakter** kullanılmamalıdır.

### 2. Kodlama Kuralları (PEP 8)

- **Kodlama Dili**: Tüm kodlar **İngilizce** yazılmalıdır.
- **Değişken/Fonksiyon İsimleri**: İngilizce ve `snake_case` kullanılmalıdır.
- **Yorumlar**: Kod içindeki yorumlar da **İngilizce** olmalıdır.
- ** commit mesaji  içinde **Türkçe karakter** kullanılmamalıdır.

### 3. Proje Yapısı

- **src/task_manager/**: Kütüphane mantığı.
- **tests/**: Test dosyaları.
- **task_manager_cli.py**: Komut satırı arayüzü.

## 🧪 Testler

Yazılan kodun doğruluğunu garantilemek için testler mevcuttur.

```bash
# Tüm testleri çalıştır
pytest

# Testleri izleme modu (otomatik yeniden çalıştırma)
pytest -f
```

## 🏗️ Mimarisi

- **Core (Çekirdek)**: `src/task_manager/core.py` - Görev yönetimi mantığı.
- **CLI (Arayüz)**: `task_manager_cli.py` - Kullanıcı etkileşimi.
- **CI/CD**: `.github/workflows/ci.yml` - Otomatik test ve doğrulama.

---

*Geliştiren: Chaxindow*
