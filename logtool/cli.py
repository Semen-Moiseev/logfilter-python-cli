#!/usr/bin/env python3

import argparse
from pathlib import Path

from .filter import filter_logs
from .analyzer import analyze_logs

def main():
	parser = argparse.ArgumentParser(description="CLI-утилита для фильтрации и анализа логов")

	parser.add_argument("file", help="Путь к лог-файлу")
	parser.add_argument("--filter", nargs = "+", help="Фильтр по ключевому слову")
	parser.add_argument("--level", help="Фильтр по уровню (INFO, ERROR, WARNING и т.д.)")
	parser.add_argument("--summary", action="store_true", help="Показать статистику по уровням")
	args = parser.parse_args()

	log_path = Path(args.file)
	if not log_path.exists():
		print(f"The file {log_path} was not found!")
		return

	filtered_lines = filter_logs(log_path, keywords=args.filter, level=args.level)
	stats = analyze_logs(filtered_lines) if args.summary else None

	print("\n".join(filtered_lines))

	if args.summary:
		print("\nСтатистика по уровням:")
		for level, count in stats.items():
			print(f"{level:10} {count}")

if __name__ == "__main__":
	main()