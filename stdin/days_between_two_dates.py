from datetime import date
import sys


date_list = [date.fromisoformat(lines.rstrip()) for lines in sys.stdin]
print((max(date_list) - min(date_list)).days)