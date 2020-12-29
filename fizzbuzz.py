import time
from os import system, name


def is_multiplier(num: int, multiplier: int) -> bool:
    return int(num % multiplier) == 0


def process_fizzbuzz(num: int) -> None:
    for x in range(1, num+1):
        out = ""

        if is_multiplier(x, 3):
            out += "Fizz"
        elif is_multiplier(x, 5):
            out += "Buzz"
        
        if out == '':
            print(x)
        else:
            print(out)


def process_fizzbuzz_old(num: int) -> None:
    for x in range(1, num+1):
        if is_multiplier(x, 3) and is_multiplier(x, 5):
            print("FizzBuzz")
        elif is_multiplier(x, 3):
            print("Fizz")
        elif is_multiplier(x, 5):
            print("Buzz")
        else:
            print(x)


def get_input() -> int:
    num = input("What amount of FizzBuzz you want to generate: ")
    try:
        return int(num)
    except Exception as e:
        print(e)
        print("\nInvalid number...")
        exit(-1)


def clear() -> None: 
    if name == 'nt': 
        _ = system('cls')
    else: 
        _ = system('clear') 


if __name__ == '__main__':
    num = get_input()
    print("\n")

    start_time = time.time()
    process_fizzbuzz_old(num)
    middle_time = time.time()
    process_fizzbuzz(num)
    end_time = time.time()

    print("\nOld method took me {:.3f} seconds!".format(float(middle_time - start_time)))
    print("New method took me {:.3f} seconds!".format(float(end_time - middle_time)))
