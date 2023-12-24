import arrow

now = "2023-06-11 00:00:00"
days = (arrow.now() - arrow.get(now)).days
year = 0
month = 0
while days >= 365:
    year += 1
    days -= 365
month = int(days / 30)
print(f"{year}年{month}月")
