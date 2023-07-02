first_runner = int(input())
second_runner = int(input())
third_runner = int(input())
total_time = first_runner + second_runner + third_runner
total_minutes = total_time // 60
total_seconds = total_time % 60
print(f"{total_minutes}:{total_seconds:02d}")
