import os
import re

def extract_number(filename):
    # 提取文件名中的数字部分
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else -1

ts_files = [f for f in os.listdir('.') if f.endswith('.ts')]
ts_files.sort(key=extract_number)

with open('filelist.txt', 'w', encoding='utf-8') as f:
    for ts in ts_files:
        f.write(f"file '{ts}'\n")