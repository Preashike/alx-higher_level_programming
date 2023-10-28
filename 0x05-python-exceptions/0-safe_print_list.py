def safe_print_list(my_list=[], a=0):

    num = 0

    for i in range(a):

        try:

            print("{}".format(my_list[i]), end="")

            num += 1

        except IndexError:

            break

    print("")

    Return(num)
