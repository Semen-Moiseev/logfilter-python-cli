#!/usr/bin/env python3

import argparse
from pathlib import Path

from logtool.filter import filter_logs
from logtool.analyzer import analyze_logs
from logtool.report import save_report

def main():
	parser = argparse.ArgumentParser(description="CLI-утилита для фильтрации и анализа логов")

	parser.add_argument("file", help="Path to log file")
	parser.add_argument("--filter", nargs = "+", help="Keyword filter")
	parser.add_argument("--level", help="Filter by level (INFO, ERROR, WARNING ...)")
	parser.add_argument("--summary", action="store_true", help="Show statistics by level")
	parser.add_argument("--save-json", action="store_true", help="Save statistics in JSON")
	parser.add_argument("--save-csv", action="store_true", help="Save statistics in CSV")
	args = parser.parse_args()

	log_path = Path(args.file)
	if not log_path.exists():
		print(f"The file {log_path} was not found!")
		return

	filtered_lines = filter_logs(log_path, keywords=args.filter, level=args.level)
	stats = analyze_logs(filtered_lines) if args.summary else None

	print("\n".join(filtered_lines))

	if args.summary:
		print("\nStatistics by level:")
		for level, count in stats.items():
			print(f"{level:10} {count}")

	if args.save_json or args.save_csv:
		reports_dir = Path("reports")
		reports_dir.mkdir(exist_ok=True)

		save_report(stats, reports_dir, to_json=args.save_json, to_csv=args.save_csv)
		print(f"\nThe report has been saved to the directory: {reports_dir}")

if __name__ == "__main__":
	main()