#!/usr/bin/env python3

from collections import Counter

def analyze_logs(log_lines):
	levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]
	counter = Counter()

	for line in log_lines:
		for level in levels:
			if level in line:
				counter[level] += 1
				break

	return dict(counter)