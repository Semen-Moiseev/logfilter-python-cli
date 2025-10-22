#!/usr/bin/env python3

import argparse
from pathlib import Path

def filter_logs(file_path, keywords):
	file = Path(file_path)
	if not file.exists():
		print(f"Файл {file_path} не найден!")
		return

	with file.open("r", encoding="utf-8") as f:
		for line in f:
			if any(keyword in line for keyword in keywords):
				print(line, end = "")

def main():
	parser = argparse.ArgumentParser(description = "Фильтрация логов по ключевым словам")
	parser.add_argument("file", help = "Путь к лог-файлу")
	parser.add_argument("keywords", nargs = "+", help = "Ключевые слова для фильтрации")
	args = parser.parse_args()

	filter_logs(args.file, args.keywords)

if __name__ == "__main__":
	main()