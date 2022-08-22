
def getMaxFreqDeviation(s):
    # Write your code here
    substring = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    deviation = []

    print("deviation: ", deviation)
    for string in substring:
        frequency = []
        print("frequency: ",  frequency)
        print("string: ", string)
        distinct_values = list(set(string))
        for i in range(len(distinct_values)):
            count = string.count(distinct_values[i])
            print(f"count {count} - frequency {frequency}")
            frequency.append(count)
        dev = max(frequency) - min(frequency)
        dev = abs(dev)

        deviation.append(dev)
        print("_______________________")
    print(deviation)
    return max(deviation)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = getMaxFreqDeviation(s)
    print(str(result) + '\n')