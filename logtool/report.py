#!/usr/bin/env python3

import json
import csv
from datetime import datetime
from pathlib import Path

def save_report(stats, reports_dir, to_json=False, to_csv=False):
	if not stats:
		print("No data to save!")
		return

	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

	if to_json:
		json_path = Path(reports_dir / f"log_stats_{timestamp}.json")
		with json_path.open("w", encoding="utf-8") as f:
			json.dump(stats, f, ensure_ascii=False, indent=2)

	if to_csv:
		csv_path = Path(reports_dir / f"log_stats_{timestamp}.csv")
		with csv_path.open("w", newline="", encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerow(["Level", "Count"])
			for level, count in stats.items():
				writer.writerow([level, count])