
hex_lst = input("리틀 엔디언으로 변환할 헥사값 -->") #리틀엔디언으로 만들 헥사값 입력
change_hex = ""

if(len(hex_lst) % 2 != 0): # 짝수가 아닐경우 앞의 0이 사라져 있으니, 앞에 0추가 -> 0x08042411
    hex_lst ="0" + hex_lst

index = len(hex_lst)
count = 0 #2씩 증가하여 while문 작동
running = True
while(running):
    change_hex += r"\x" + hex_lst[index-2:index]
    count += 2
    index -= 2
    if(count == len(hex_lst)):
        running = False

print("변환된 리틀 엔디언 값 : {0}".format(change_hex))

    

# 결과 값
# 리틀 엔디언으로 변환할 헥사값 -->3333333
# 변환된 리틀 엔디언 값 : \x33\x33\x33\x03
