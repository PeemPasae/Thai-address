# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:47:25 2024

@author: chana
"""

# เปิดไฟล์ mm.txt
with open("tambol.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์

# เปิดไฟล์ mm_deta.txt สำหรับเขียนข้อมูล
with open("tambol_deta.txt", "w", encoding="utf-8") as output_file:
    # วนลูปผ่านแต่ละบรรทัด
    for line in lines:
        # ตรวจสอบว่ามีคำว่า VALUES ในแต่ละบรรทัด
        if "VALUES" in line:
            # ตัดส่วน VALUES ออก
            values_part = line.split("VALUES")[1]

            # ลบเครื่องหมายวงเล็บ, ช่องว่าง, และ ;
            values_part = values_part.strip(" ();\n").replace("'", "")

            # แยกค่าด้วยเครื่องหมายคอมมา
            values = values_part.split(", ")

            # จัดรูปแบบผลลัพธ์
            mcode = values[0]
            mname = values[1]
            

            # สร้างสตริงผลลัพธ์ตามที่ต้องการ
            output = f"{mcode} {mname}\n"

            # เขียนข้อมูลลงไฟล์ mm_deta.txt
            output_file.write(output)

print("เขียนข้อมูลสำเร็จ!")