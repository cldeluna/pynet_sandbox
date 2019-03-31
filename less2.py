import os
import sys
import pprint
# Import local modules
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import less1


def print_msg(msg, opt_var=''):
    print("{} \t{}".format(msg, opt_var))


def main():
    # Lesson 2
    less1.print_header("Lesson 2 - Exercise 1A")

    f = open("show_version.txt")
    myfile = f.read()
    print(myfile)
    print("myfile is of type {}".format(type(myfile)))
    print("\n Used standard file open.")
    f.close()

    less1.print_header("Lesson 2 - Exercise 1B with Context Manager")
    with open("show_version.txt") as f:
        file_list = f.readlines()
        print(file_list)
        print("file-list is of type {}".format(type(file_list)))
        if type(file_list) == list:
            print("file_list has {} elements.".format(len(file_list)))
    print("\nUsed context manager to open file.\n")


    # Lesson 2
    less1.print_header("Lesson 2 - Exercise 2")

    ip_list = []
    ip1 = '1.1.1.1'
    ip2 = ['1.1.1.2']
    ip3 = ['1.1.1.3']
    ip4 = ['1.1.1.4']
    ip5 = ['1.1.1.5']

    ip_list.append(ip1)
    print_msg("IP List:",ip_list)
    ip_list.extend(ip2)
    print_msg("IP List:",ip_list)
    ip_list.extend(ip3)
    print_msg("IP List:",ip_list)
    ip_list = ip_list + ip4 + ip5
    print_msg("IP List:",ip_list)

    ip_list[0] = "2.2.2.2"
    print_msg("First Elemente has Changed and IP LIST is now: ",ip_list)


    # Lesson 2
    less1.print_header("Lesson 2 - Exercise 3")

    with open("show_arp.txt") as f:
        file_lines = f.readlines()

    pprint.pprint(file_lines)
    print("\nSliced Output")
    sliced_file = file_lines[1:]
    pprint.pprint(sliced_file)

    sliced_file.sort()
    print("\nSorted Output")
    pprint.pprint(sliced_file)

    first3 = sliced_file[:3]
    print("\nFirst 3 Entries Output")
    pprint.pprint(first3)

    myjoin = "\n".join(first3)
    print("\nFirst 3 Entries Joined")
    pprint.pprint(myjoin)

    with open("my_join.txt", 'w') as f:
        f.write(myjoin)

if __name__ == "__main__":
    main()
