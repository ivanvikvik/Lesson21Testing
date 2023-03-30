import view
import logic
import util

# controller
def main():
    while True:
        size = int(input("Input size of list: "))
        if size > 0:
            break
        else:
            view.write("Error. User data was invalid.")

    ls = util.create_list(size)

    util.rnd_init_list(ls, -50, 50)
    # util.user_init_list(ls)

    second = logic.find_second_max_value(ls)

    msg = f"Second max value is {second}."
    view.write(ls)
    view.write(msg)


if __name__ == "__main__":
    main()
