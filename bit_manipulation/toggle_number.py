if __name__ == "__main__":
    num = int(raw_input("enter the number\n").strip())
    toggled_num = 0
    mask = 1
    while (num):
        last_bit = num & 1
        if not last_bit:
            toggled_num = toggled_num | mask
        num = num >> 1
        mask = mask << 1
    print toggled_num
