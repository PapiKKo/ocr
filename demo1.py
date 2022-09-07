### ファイル内の文字列を検索・抽出
"""
import os

dir_path = r'/Users/arakiyuna/Downloads/ocr'
file_name = 'out_star.txt'

file_path = os.path.join(dir_path, file_name)

with open(file_path) as f:
    lines = f.readlines()
lines_strip = [line.strip() for line in lines ]
print(lines_strip)

"""
import re


lines = 'SEVENSHOLDINGS 7 セブン-イレブン 横浜みなとみらい4丁目店 神奈川県横浜市西区みなとみらい4 丁目3-6 電話: 045-663-2201 レジ #2 2012年08月12日 (金) 20:05 青 043 領収書 7プレミアムサラダチキンバー 香り箱の寿司 小 計 (税抜 8%) 消費税等 (8%) *128 *140 伝票番号 ¥268 ¥21 ¥289 合計 (税率 8% 対象 (内消費税等 8% 楽天ペイ支払 ¥289 お買上明細は上記のとおりです。 [*] マークは軽減税率対象です。 #1227620220812200537468490212895 ¥289) ¥21) 220-812-210-0365 SEVENSHOLDINGS'
###print(lines)
lines_strip = lines.split()
print(lines_strip)


if ('¥' in lines_strip) :
    list_money1 = [line_s for line_s in lines_strip if '¥' in line_s ]
    print(list_money1)
    m_str = ",".join(list_money1)
    m_num = re.compile(r"\d+").findall(m_str)
    print("領収金額：" + max(m_num))

"""スタバの領収書用　できてない
if ('\d' in lines_strip) :
    list_money1 = [line_s for line_s in lines_strip if '\d' in line_s ]
    print(list_money1)
    m_str = ",".join(list_money1)
    m_num = re.compile(r"\d+").findall(m_str)
    print("領収金額：" + max(m_num))
"""
###年月日文字入りの日付の場合
if ('年' in lines_strip) :
    list_date = [line_s for line_s in lines_strip if '年' in line_s ]
    print(list_date)
    date_str = "".join(list_date)
    print(date_str[5:])

if (r"/" in lines_strip) :
    list_date = [line_s for line_s in lines_strip if r"/" in line_s ]
    print(list_date)

"""
list_date_value = [item.split()[0] for item in list_date ]
print(list_date_value)
"""