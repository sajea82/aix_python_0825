pass_count = 0
for i in range(1,6):
    score = int(input(f"{i}번째점수:"))
    if score >= 60:
        pass_count += 1

    print(f"합격자수: {pass_count}")





