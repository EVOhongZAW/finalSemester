# ราคาและจำนวนสินค้า
products = {
    "น้ำเปล่า": {"price": 20, "quantity": 10},
    "น้ำวิตามินซี": {"price": 25, "quantity": 15},
    "น้ำแร่": {"price": 30, "quantity": 12},
    "น้ำอัดลม": {"price": 15, "quantity": 8},
    "น้ำผลไม้": {"price": 35, "quantity": 10}
}

# ราคาของเหรียญและธนบัตร
coin_values = {
    1: "บาท",
    2: "บาท",
    5: "บาท",
    10: "บาท"
}

banknote_values = {
    20: "บาท",
    50: "บาท",
    100: "บาท",
    500: "บาท",
    1000: "บาท"
}

# โปรโมชัน
def apply_promotion(total):
    if total >= 300:
        discount = total * 0.15
    elif total >= 150:
        discount = total * 0.1
    else:
        discount = 0

    total_with_discount = total - discount
    return total_with_discount, discount

def main():
    print("ยินดีต้อนรับสู่ตู้ขายเครื่องดื่มนินจาเต่า!")

    total_cost = 0
    cart = {}  # เก็บรายการสินค้าที่ลูกค้าซื้อ

    while True:
        print("\nรายการสินค้า:")
        for item, info in products.items():
            print(f"{item}: ราคา {info['price']} บาท (จำนวนคงเหลือ: {info['quantity']} ชิ้น)")

        item = input("\nโปรดเลือกชนิดของสินค้า (หรือพิมพ์ 'ชำระเงิน' เมื่อเสร็จสิ้นการสั่งซื้อ): ")

        if item.lower() == 'ชำระเงิน':
            break

        if item in products:
            if products[item]["quantity"] > 0:
                products[item]["quantity"] -= 1  # ลดจำนวนสินค้าในสต็อก
                total_cost += products[item]["price"]
                if item in cart:
                    cart[item]["quantity"] += 1
                else:
                    cart[item] = {"price": products[item]["price"], "quantity": 1}
                print(f"ราคารวมในตอนนี้: {total_cost} บาท")
            else:
                print(f"ขออภัย! {item} หมดสต็อก")
        else:
            print("ชนิดของสินค้าไม่ถูกต้อง")

    total_cost, discount = apply_promotion(total_cost)
    print("\nสรุปรายการสินค้าที่ซื้อ:")
    for item, info in cart.items():
        item_total = info["price"] * info["quantity"]
        print(f"{item}: จำนวน {info['quantity']} ชิ้น x {info['price']} บาท = {item_total} บาท")

    print(f"\nยอดรวมก่อนส่วนลด: {total_cost} บาท")
    print(f"ส่วนลด: {discount} บาท")
    print(f"ยอดรวมหลังส่วนลด: {total_cost - discount} บาท")

    while True:
        payment = float(input("\nกรุณาใส่จำนวนเงิน: "))
        if payment >= total_cost - discount:
            change = payment - (total_cost - discount)
            print(f"ทอนเงิน: {change} บาท")

            # คำนวณและแสดงเหรียญที่ใช้ทอน
            print("เหรียญทอน:")
            for coin_value in sorted(coin_values.keys(), reverse=True):
                coin_count = int(change / coin_value)
                if coin_count > 0:
                    print(f"{coin_count} {coin_values[coin_value]}: {coin_count * coin_value} บาท")
                change -= coin_count * coin_value

            # คำนวณและแสดงธนบัตรทอน
            print("ธนบัตรทอน:")
            for banknote_value in sorted(banknote_values.keys(), reverse=True):
                banknote_count = int(change / banknote_value)
                if banknote_count > 0:
                    print(f"{banknote_count} {banknote_values[banknote_value]}: {banknote_count * banknote_value} บาท")
                change -= banknote_count * banknote_value

            break
        else:
            print("จำนวนเงินไม่เพียงพอ โปรดใส่จำนวนเงินอีกครั้ง")

    print("\nขอบคุณที่ใช้บริการ!")

if __name__ == "__main__":
    main()