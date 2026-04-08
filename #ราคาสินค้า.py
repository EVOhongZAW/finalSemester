#ราคาสินค้า 
products = {
    "คอมพิวเตอร์ตั้งโต๊ะ": 5000,
    "คอมพิวเตอร์โน๊ตบุ๊ค": 8000,
    "สมาร์ทโฟน": 3000,
    "เครื่องปริ้นเตอร์": 4000,
    "แท็บเล็ต": 6000
}

print("ยินดีต้อนรับสู่ TechNo Shop - ร้านค้าสินค้าทางคอมพิวเตอร์")
print("รายการสินค้าที่มีในร้าน TechNo Shop:")
for product, price in products.items():
    print(f"{product}: {price} บาท")

selected_products = {}

#กำหนดจำนวนรอบในการเลือกสินค้า
while len(selected_products) < len(products):
    product_name = input("โปรดเลือกสินค้า (หรือพิมพ์ 'เสร็จสิ้น' เพื่อเรียกดูรายการ): ")
    
    if product_name == "เสร็จสิ้น":
        break
    elif product_name in products:
        quantity = int(input(f"ป้อนจำนวน {product_name} ที่คุณต้องการซื้อ: "))
        selected_products[product_name] = quantity
    else:
        print("สินค้าไม่ถูกต้อง โปรดตรวจสอบอีกครั้ง.")

#คำนวณราคาและส่วนลด
total_price = sum(products[product] * quantity for product, quantity in selected_products.items())
discount = 0

if total_price > 10000:
    discount = total_price * 0.1
elif total_price > 3000:
    discount = total_price * 0.05

#แสดงผลรายละเอียดการซื้อขาย
print("\nรายละเอียดการซื้อขาย＼(￣▽￣)／:")
for product, quantity in selected_products.items():
    print(f"{product}: {quantity} ชิ้น")

print(f"ราคารวมก่อนส่วนลด: {total_price} บาท")
print(f"ส่วนลด: {discount} บาท")
print(f"ราคารวมหลังส่วนลด: {total_price - discount} บาท")