# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути.
# Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

init_hours = int(input())
init_minutes = int(input())
total_minutes = init_hours * 60 + init_minutes
total_new_minutes = total_minutes + 15
new_hours = total_new_minutes // 60
if new_hours >= 24:
    new_hours -= 24
new_minutes = total_new_minutes % 60
print(f"{new_hours}:{new_minutes:02d}")

