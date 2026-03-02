import re
import json

def to_float_money(s: str) -> float:
    return float(s.replace("\u00A0", " ").replace(" ", "").replace(",", "."))

def to_float_qty(s: str) -> float:
    return float(s.replace("\u00A0", " ").replace(" ", "").replace(",", "."))

# read raw.txt
with open("raw.txt", "r", encoding="utf-8", errors="ignore") as f:
    raw = f.read()

lines = raw.splitlines()
raw_upper = raw.upper()

re_item_no = re.compile(r"^\s*(\d+)\.\s*$")
re_qty_unit = re.compile(r"^\s*(\d+,\d{3})\s*x\s*([\d \u00A0]+,\d{2})\s*$")
re_money_line = re.compile(r"^\s*([\d \u00A0]+,\d{2})\s*$")
re_any_money = re.compile(r"\b\d{1,3}(?:[ \u00A0]\d{3})*,\d{2}\b|\b\d+,\d{2}\b")

# date & time
date_str = None
time_str = None
m_dt = re.search(r"ВРЕМЯ:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", raw_upper)
if m_dt:
    date_str = m_dt.group(1)
    time_str = m_dt.group(2)

# payment method
payment_method = None
if "БАНКОВСКАЯ КАРТА" in raw_upper or "КАРТА" in raw_upper:
    payment_method = "CARD"
elif "НАЛИЧ" in raw_upper:
    payment_method = "CASH"

# total from receipt
total_from_receipt = None
m_total = re.search(r"ИТОГО\s*:\s*([\d \u00A0]+,\d{2})", raw_upper)
if m_total:
    total_from_receipt = to_float_money(m_total.group(1))

# parse items
items = []
i = 0

while i < len(lines):
    m_no = re_item_no.match(lines[i])
    if not m_no:
        i += 1
        continue

    num = int(m_no.group(1))
    i += 1

    name_parts = []
    while i < len(lines) and not re_qty_unit.match(lines[i]):
        l = lines[i].strip()
        if l and l.lower() != "стоимость":
            name_parts.append(l)
        i += 1

    if i >= len(lines):
        break

    m_qu = re_qty_unit.match(lines[i])
    qty = to_float_qty(m_qu.group(1))
    unit_price = to_float_money(m_qu.group(2))
    i += 1

    while i < len(lines) and not re_money_line.match(lines[i]):
        i += 1
    if i >= len(lines):
        break

    line_total = to_float_money(re_money_line.match(lines[i]).group(1))
    i += 1

    items.append({
        "no": num,
        "name": " ".join(name_parts).strip(),
        "qty": qty,
        "unit_price": unit_price,
        "line_total": line_total
    })

# all prices
prices_found = [p.replace("\u00A0", " ").strip() for p in re_any_money.findall(raw)]

# computed total
total_computed = round(sum(x["line_total"] for x in items), 2)

# output
result = {
    "date": date_str,
    "time": time_str,
    "payment_method": payment_method,
    "prices_found": prices_found,
    "items": items,
    "items_count": len(items),
    "total_from_receipt": total_from_receipt,
    "total_computed": total_computed
}

print(json.dumps(result, ensure_ascii=False, indent=2))