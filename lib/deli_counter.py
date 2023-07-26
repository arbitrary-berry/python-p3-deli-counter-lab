katz_deli = []


def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line = []
        num = 1
        while num <= len(katz_deli):
            line.append(f"{num}. {katz_deli[num-1]}")
            num += 1
        print(f"The line is currently: {' '.join(line)}")


def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    print(
        f"Welcome, {new_person}. You are number {katz_deli.index(new_person) + 1} in line."
    )


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]
