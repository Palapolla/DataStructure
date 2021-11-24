# โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้ และให้แสดงผลดังตัวอย่าง

# 		    Speed (km/h)		ระดับพายุ
# 			0-51.99			Breeze
# 			52.00-55.99		Depression
# 			56.00-101.99	        Tropical Storm
# 			102.00-208.99	        Typhoon
# 			>= 209			Super Typhoon

#  *** Wind classification ***
# Enter wind speed (km/h) : 23.25
# Wind classification is Breeze.

print(' *** Wind classification ***')
n = float(input('Enter wind speed (km/h) : '))

if 0<=n<=51.99:
    print('Wind classification is Breeze.')
elif 52.00<=n<=55.99:
    print('Wind classification is Depression.')
elif 56.00<=n<=101.99:
    print('Wind classification is Tropical Storm.')
elif 102.00<=n<=208.99:
    print('Wind classification is Typhoon.')
elif n>=209:
    print('Wind classification is Super Typhoon.')
else:
    print('!!!Wrong value can\'t classify.')