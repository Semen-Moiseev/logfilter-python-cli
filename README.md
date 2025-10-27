# logfilter-python-cli

`LogFilter` — это консольный инструмент, который позволяет просматривать лог-файлы и фильтровать строки по ключевым словам

---

## Возможности

- Фильтровать логи по ключевым словам и уровням (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)
- Анализировать количество логов по уровням
- Выводить статистику в консоль
- Сохранять статистику в JSON и CSV
- Простое использование из командной строки
- Минимальные зависимости — только стандартная библиотека

---

## Структура проекта

```
logfilter-python-cli/
├── .venv/                # Виртуальное окружение
├── logtool/
│   ├── __init__.py
│   ├── cli.py
│   ├── filter.py
│   ├── analyzer.py
│   └── report.py
├── data/
│ └── logs.log            # Тестовый лог-файл
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

### 2.1. Создайте и активируйте виртуальное окружение

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux / macOS
```

### 2.2. Сборка docker образа

```bash
docker build -t logtool-cli .
```

## Использование

### 1. Напрямую через Python

```bash
python -m logtool.cli <аргументы>

python -m logtool.cli data/logs.log --filter user --summary --save-json
```

### 2. Через Docker

```bash
docker run --rm -it logtool-cli <аргументы>

docker run --rm -it logtool-cli data/logs.log --filter user --summary --save-json
```

Аргументы:

- file — путь к лог-файлу (обязательный)
- --filter — ключевое слово или несколько через пробел
- --level — уровень логов (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- --summary — вывод статистики в консоль
- --save-json — сохраняет статистику в JSON
- --save-csv — сохраняет статистику в CSV
