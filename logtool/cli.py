#!/usr/bin/env python3

import argparse
from pathlib import Path

from .filter import filter_logs

def main():
	parser = argparse.ArgumentParser(description="CLI-утилита для фильтрации и анализа логов")

	parser.add_argument("file", help="Путь к лог-файлу")
	parser.add_argument("--filter", help="Фильтр по ключевому слову")
	args = parser.parse_args()

	log_path = Path(args.file)
	if not log_path.exists():
		print(f"The file {log_path} was not found!")
		return

	filtered_lines = filter_logs(log_path, keywords=args.filter)
	print("\n".join(filtered_lines))

if __name__ == "__main__":
	main()