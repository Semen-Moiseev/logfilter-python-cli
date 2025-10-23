#!/usr/bin/env python3

from pathlib import Path

def filter_logs(file_path, keywords=None, level=None):
	file = Path(file_path)

	with file.open("r", encoding="utf-8") as f:
		lines = [line.strip() for line in f if line.strip()]

	if keywords:
		if isinstance(keywords, str):
			keywords = [keywords]

		lines = [l for l in lines if any(k.lower() in l.lower() for k in keywords)]
	if level:
		lines = [l for l in lines if level.upper() in l]

	return lines