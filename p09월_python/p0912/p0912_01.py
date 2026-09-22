pass_count = 0
pass_total = 0

for i in range(1,6):
    score = int(input(f"{i}번째 점수: "))
    if score >= 60:
        pass_count +=1
        pass_total += score 

print(f"합격자수 : {pass_count}")
print(f"합격자 점수 합계 : {pass_total}")


