# Junnan Shimizu
# CS337 - Project 8
# 5/1/22

import random


def ref_strings_noloc(length):
    results = []
    while len(results) < length:
        results.append(random.randrange(0, length))
    return results


def ref_strings_loc(length):
    results = []
    for i in range(length):
        temp = i + random.randrange(-3, 3)
        while temp <= 0 or temp >= length:
            temp = i + random.randrange(-3, 3)
        results.append(temp)
    return results


def fifo(reference):
    print("FIFO:")
    hits = 0
    frame = []
    for i in reference:
        if i in frame:
            hits += 1
            print(i, frame, "Hit")
        else:
            if len(frame) < 5:
                frame.append(i)
                print(i, frame, "Miss")
            else:
                frame.pop(0)
                frame.append(i)
                print(i, frame, "Miss")

    faults = len(reference) - hits
    return faults


def lru(reference):
    print("LRU:")
    counts = [0] * len(reference)
    frame = []
    hits = 0
    for i in reference:
        counts[i] += 1
        if i in frame:
            hits += 1
            print(i, frame, "Hit")
        else:
            if len(frame) < 5:
                frame.append(i)
                print(i, frame, "Miss")
            else:
                temp_list = []
                for index in frame:
                    temp_list.append(counts[index])
                min_value = min(temp_list)
                frame.remove(frame[min_value])
                frame.append(i)
                print(i, frame, "Miss")

    faults = len(reference) - hits
    return faults


def optimal(reference):
    print("Optimal:")
    frame = []
    hits = 0
    for i in reference:
        if i in frame:
            hits += 1
            print(i, frame, "Hit")
        else:
            if len(frame) < 5:
                frame.append(i)
                print(i, frame, "Miss")
            else:
                temp = []
                for x in range(reference.index(i) + 1, len(reference)):
                    temp.append(reference[x])
                for x in frame:
                    if x not in temp:
                        frame.remove(x)
                        frame.append(i)
                        break
                    else:
                        counts = [0] * 5
                        for x2 in frame:
                            count = 0
                            for x3 in temp:
                                if x2 != x3:
                                    count += 1
                                else:
                                    counts[frame.index(x2)] = count
                        frame.pop(counts.index(min(counts)))
                        frame.append(i)
                print(i, frame, "Miss")

    faults = len(reference) - hits
    return faults


if __name__ == '__main__':
    ref_string_noloc = ref_strings_noloc(100)
    ref_string_loc = ref_strings_loc(100)
    print(ref_string_noloc)
    print("# of Page Faults:", fifo(ref_string_noloc))
    print("# of Page Faults:", lru(ref_string_noloc))
    print("# of Page Faults:", optimal(ref_string_noloc))

    print(ref_string_loc)
    print("# of Page Faults:", fifo(ref_string_loc))
    print("# of Page Faults:", lru(ref_string_loc))
    print("# of Page Faults:", optimal(ref_string_loc))
