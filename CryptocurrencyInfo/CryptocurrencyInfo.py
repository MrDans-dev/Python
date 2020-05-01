import os
import blockchain as bc
import time

def get_info():
    stats = bc.statistics.get()
    ticker = bc.exchangerates.get_ticker()
    print("Hash Rate TH/s: ", stats.hash_rate/1000000000)
    print("Last Price PLN: ",ticker["PLN"].last)
    print("Last Price $: ",ticker["USD"].last)
    print("Block Difficulty: ",stats.difficulty)

while(1):
    get_info()
    print()
    time.sleep(1)