import threading

def calc_sum(start, end) :
    total = sum(range(start, end + 1))
    print(f"1 + 2 + 3 + ... + {end} = {total}")

t1 = threading.Thread(target=calc_sum, args=(1, 1000))
t2 = threading.Thread(target=calc_sum, args=(1, 100000))
t3 = threading.Thread(target=calc_sum, args=(1, 10000000))

t1.start()
t2.start()
t3.start()