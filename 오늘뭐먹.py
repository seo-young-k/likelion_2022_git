import random
import time #타임기능 임포트

for x in range(30):
    print(random.choice(['된장찌개','피자','제육볶음']))
    print('이 문장도 반복되나')

while True:

    print(random.choice(['된장찌개','피자','제육볶음']))
    break
    print('이 문장도 반복되나')
    time.sleep(1) #1초 쉬기
  
lunch = random.choice(["a",'b','c'])
lunch = "냉장고"
dinner = random.choice(["d",'e','f'])

print(lunch)

#dictionary
information = {'고향':'수원','이름':'서영','나이':23}

print(information)
print(information.get('이름'))

information = {'특기':'피아노','사는곳':'서울'}
print(information.get('특기'))

information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
foods = ["된장찌개", "피자", "제육볶음"]
print(information.get("취미"))
information["특기"] = "피아노"
information["사는곳"] = "서울"
del information["좋아하는 음식"]
print(information)
print(len(information))
information.clear()
print(information)
print(foods[1])
print(foods[-1])
foods.append('김밥')
print(foods)
del foods[1]

#리스트에서 반복
foods = ["된장찌개", "피자", "제육볶음"]
for x in foods:
    print(x)

#딕셔너리에서의 반복
information = {"고향":"수원","취미":"영화보기","좋아하는 음식":"국수"}
for x,y in information.itmes():
    print(x)
    print(y)

#집합 알아보기
foods = ["된장찌개", "피자", "제육볶음"]
foods_set1 = set(foods)
foods_set2 = set(["된장찌개", "피자", "제육볶음"])
print(foods_set1)
print(foods_set2)

#합집합
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 | menu2
print(menu3)

#교집합
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 & menu2
print(menu3)

#차집합
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 - menu2
print(menu3)

#만약에
import random

food = random.choice(["된장찌개","피자","제육볶음"])

print(food)
if(food == "제육볶음"):
    print("곱배기 주세요")
else:
    print("그냥 주세요")
print("종료")

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
while True:
    item = input("음식을 추가 해주세요 : ")
    lunch.append(item)
    print(lunch)


lunch = ["된장찌개", "피자", "제육볶음"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
    
print(lunch)
set_lunch = set(lunch)

set_dinner = set(["된장찌개", "피자", "제육볶음", "짜장면"])
food = "짜장면"
set_dinner = set_dinner - set([food])
print(set_dinner)

import random
import time

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)
while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_lunch)))
