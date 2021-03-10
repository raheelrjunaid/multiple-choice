from time import sleep
from rich import print
from keyboard import is_pressed as keypress
from sys import stdout


# class Order():
#     def __init__(self, size, topping):
#         self.size = size
#         self.topping = topping


def deleteLines(line_count):
    for line in range(line_count):
        stdout.write('\x1b[1A')
        stdout.write('\x1b[2K')


def refresh_list(cursorPos, array, first=False):
    if not first:
        deleteLines(len(array))

    for item in array:
        if cursorPos == array.index(item):
            print(f"[green]> {item}[/green]")
        else:
            print(item)


def refresh_cursor(cursorPos, array):
    if keypress("j"):
        cursorPos += 1
        if cursorPos >= len(array):
            cursorPos = 0
    if keypress("k"):
        cursorPos -= 1
        if cursorPos < 0:
            cursorPos = len(array) - 1
    return cursorPos


def multipleChoice(array, showNum=False):
    cursorPos = 0

    refresh_list(cursorPos, array, first=True)
    while True:
        if keypress("j") or keypress("k"):
            cursorPos = refresh_cursor(cursorPos, array)
            refresh_list(cursorPos, array)
            sleep(0.3)
        if keypress("enter"):
            array_choice = array[cursorPos]
            print(f"Selected {array_choice}.")
            sleep(0.5)
            return array_choice


pizza_sizes = [
    "Individual",
    "Small",
    "Medium",
    "Large"
]

pizza_toppings = [
    "Pepperoni",
    "Pineapple",
    "Chicken",
    "Extra Cheese"
]


def main():
    try:
        print("Choose a pizza size:")
        multipleChoice(pizza_sizes)
        print("Choose a pizza topping:")
        multipleChoice(pizza_toppings)
        # order = Order(size, topping)

        # for field in order.items():
        #     print(field)
    except KeyboardInterrupt:
        print("\nExited Program")


if __name__ == "__main__":
    main()
