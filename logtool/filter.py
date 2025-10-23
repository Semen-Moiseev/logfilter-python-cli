#!/usr/bin/env python3

from pathlib import Path

def filter_logs(file_path, keywords=None):
	file = Path(file_path)

	with file.open("r", encoding="utf-8") as f:
		lines = [line.strip() for line in f if line.strip()]

	if keywords:
		lines = [l for l in lines if keywords.lower() in l.lower()]

	return lines