# •	Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# •	Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# •	Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# •	Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала
pool_volume = int(input())
debit_first_pipe = int(input())
debit_second_pipe = int(input())
worker_time = float(input())
pool_level = (debit_first_pipe + debit_second_pipe) * worker_time
percent_first_pipe = (debit_first_pipe / (debit_first_pipe + debit_second_pipe)) * 100
percent_pool = (pool_level / pool_volume) * 100
if pool_volume >= pool_level:
    print(f"The pool is {percent_pool:.02f}% full. Pipe 1: {percent_first_pipe:.02f}%. Pipe 2: {100 - percent_first_pipe:.02f}%.")
else:
    print(f"For {worker_time:.02f} hours the pool overflows with {pool_level - pool_volume:.02f} liters.")
