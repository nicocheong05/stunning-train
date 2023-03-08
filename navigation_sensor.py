even_parity = []
parity_removed = []


def count_ones(num):
    one_count = num.count("1")
    if (one_count % 2) == 0:
        return True
    else:
        return False


f = open("navigation_data", "r")
while True:
    line = f.readline().strip()
    if line == "":
        break
    bin_value = bin(int(line))
    if count_ones(bin_value):
        even_parity.append(int(line))
f.close()

print(even_parity)


def remove_parity():
    for i in range(len(even_parity)):
        old_bin_value = bin(even_parity[i])
        if len(old_bin_value) > 16:
            new_bin_value = old_bin_value[3:]
        else:
            new_bin_value = old_bin_value
        parity_removed.append(int(new_bin_value, 2))


remove_parity()
print(parity_removed)


def average():
    total = sum(parity_removed)
    avg = total/len(parity_removed)
    return round(avg)


print(average())