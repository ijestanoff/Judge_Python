total_assessment = int(input())
average_total_assessment = 0
total_presentation = 0
while True:
    presentation = input()
    if presentation == "Finish":
        break
    average_assessment = 0
    for _ in range(total_assessment):
        assessment = float(input())
        average_assessment += assessment
    print(f"{presentation} - {average_assessment / total_assessment:.2f}.")
    total_presentation += 1
    average_total_assessment += average_assessment / total_assessment
print(f"Student's final assessment is {average_total_assessment / total_presentation:.2f}.")