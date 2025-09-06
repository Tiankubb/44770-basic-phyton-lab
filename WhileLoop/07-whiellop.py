numbers = []
while True:
    value = input()
    if value.lower() == "end":
        break
    try:
        num = float(value)
        numbers.append(num)
    except:
        print("ป้อนตัวเลขหรือ end เท่านั้น")
if numbers:
    print("ค่าสูงสุด:", max(numbers))
    print("ค่าต่ำสุด:", min(numbers))
else:
    print("ไม่มีข้อมูล")