# logfilter-python-cli

`LogFilter` — это консольный инструмент, который позволяет просматривать лог-файлы и фильтровать строки по ключевым словам

---

## Возможности

- Фильтрация логов по нескольким ключевым словам (`ERROR`, `WARNING`, `INFO`, и т.д.)
- Простое использование из командной строки
- Возможность запуска через `python -m logfilter`
- Минимальные зависимости — только стандартная библиотека

---

## Структура проекта

```
logfilter-python-cli/
├── .venv/                # Виртуальное окружение
├── logfilter/
│ ├── __init__.py
│ └── log_filter.py       # Основная логика CLI-утилиты
├── scripts/
│ ├── run_log_filter.bat  # Батник для Windows
│
├── tests/
│ └── test_log_filter.log # Тестовый лог-файл
├── requirements.txt
└── README.md
```

---

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/<your-username>/logfilter-python-cli.git
cd logfilter-python-cli
```

### 2. Создайте и активируйте виртуальное окружение

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # macOS / Linux
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

## Использование

### 1. Напрямую через Python

```bash
python logfilter/log_filter.py tests\test_log_filter.log ERROR WARNING
```

### 2. Через BAT / PowerShell

```bash
scripts\run_log_filter.bat tests\test_log_filter.log ERROR WARNING
# или
.\scripts\run_log_filter.ps1 tests\test_log_filter.log ERROR WARNING

```
