from typing import List, Union, Optional

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


# print(get_full_name("Jack", "Pie"))


def tell_state(on: bool):
    if on:
        print("State is ON")
    else:
        print("State is OFF")


# tell_state(True)


def process_items(items: set[str, str, str]):
    for item in items:
        print(item)


# process_items({"Great", "Bastard", "Leo"})


def get_total_cost(costs: dict[str, int]):
    total: int = 0
    for k, v in costs.items():
        total += v
    # print(total)
    return total


t = get_total_cost({'s': float(4.1), 'k': 20.2, 'm': 100.5, 'n': 5})
# print("Total is", t)


def print_str_or_int(i: Union[str, int]):
    print(i)


# print_str_or_int(12)
# print_str_or_int("Mary")


# Optional
def say_hi_to(nm: Optional[str]):
    if nm:
        print(nm.title())
    else:
        print(nm)


def say_hi_to2(nm: Union[int, None]):
    if nm:
        print(nm.real)
    else:
        print(nm)


say_hi_to(None)
say_hi_to2(None)
say_hi_to2(50)
