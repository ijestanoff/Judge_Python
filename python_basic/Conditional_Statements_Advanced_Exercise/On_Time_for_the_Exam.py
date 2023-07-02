# •	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.

exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

# •	"Late", ако студентът пристига по-късно от часа на изпита;
# •	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# •	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# •	"mm minutes before the start" за идване по-рано с по-малко от час;
# •	"hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:05”;
# •	 "mm minutes after the start" за закъснение под час;
# •	"hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:03”.

exam_time = exam_hour * 60 + exam_min
arrive_time = arrive_hour * 60 + arrive_min

if arrive_time > exam_time:
    print("Late")
    if arrive_time - exam_time < 60:
        print(f"{arrive_time - exam_time} minutes after the start")
    else:
        late_hour = (arrive_time - exam_time) // 60
        late_min = (arrive_time - exam_time) % 60
        print(f"{late_hour}:{late_min:02d} hours after the start")
elif 0 <= (exam_time - arrive_time) <= 30:
    print("On time")
    if 0 < exam_time - arrive_time < 60:
        print(f"{exam_time - arrive_time} minutes before the start")
else: # after more than 30min
    print("Early")
    if exam_time - arrive_time < 60:
        print(f"{exam_time - arrive_time} minutes before the start")
    else:
        early_hour = (exam_time - arrive_time) // 60
        early_min = (exam_time - arrive_time) % 60
        print(f"{early_hour}:{early_min:02d} hours before the start")

