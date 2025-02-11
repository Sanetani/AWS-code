"""
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:日本の祝日
X-WR-TIMEZONE:UTC
X-WR-CALDESC:日本の祝日と行事
"""

from icalendar import Calendar, Event
import os

# 入力ファイルと出力ファイルのパス
input_file_path = 'basic.ics'  # 元の .ics ファイル
output_file_path = 'filtered_2024_2025_holidays.ics'  # フィルタ後のファイル

# ファイルが存在するか確認
if os.path.exists(input_file_path):
    # .ics ファイルを開いて解析
    with open(input_file_path, 'r') as file:
        calendar = Calendar.from_ical(file.read())
    
    # ここでカレンダーのフィルタ処理を追加（例: 2024-2025の祝日だけ抽出）
    
    # フィルタ結果を出力ファイルに保存
    with open(output_file_path, 'wb') as f:
        f.write(calendar.to_ical())
else:
    print(f"ファイル {input_file_path} が存在しません。")
