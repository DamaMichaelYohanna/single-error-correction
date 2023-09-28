def calculate_redundant_bits(m):
    # Use the formula 2 ^ r >= m + r + 1
    # to calculate the no of redundant bits.
    # Iterate over 0 .. m and return the value
    # that satisfies the equation

    for i in range(m):
        if 2 ** i >= m + i + 1:
            print(i)
            return i


def position_redundant_bits(data, r):
    # Redundancy bits are placed at the positions
    # which correspond to the power of 2.
    j = 0
    k = 1
    m = len(data)  # length of data
    res = ''  # result to be generated
    print("here we go", j, k, r, m)

    # If position is power of 2 then insert '0'
    # Else append the data
    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    # The result is reversed since positions are
    # counted backwards. (m + r+1 ... 1)
    return res[::-1]


def calculate_parity_bits(arr, r):
    n = len(arr)

    # For finding rth parity bit, iterate over
    # 0 to r - 1
    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            # If position has 1 in ith significant
            # position then Bitwise OR the array value
            # to find parity bit value.
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-1 * j])
            # -1 * j is given since array is reversed

        # String Concatenation
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr


def detect_error(arr, nr):
    n = len(arr)
    res = 0

    # Calculate parity bits again
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-1 * j])

        # Create a binary no by appending
        # parity bits together.

        res = res + val * (10 ** i)

    # Convert binary to decimal
    return int(str(res), 2), res


def find_word(word):
    j = 0
    res = ''
    strinify_word = str(word)
    for i in range(1, len(strinify_word)+1):
        if i == 2 ** j:
            j += 1
        else:
            res += strinify_word[::-1][i-1]

    return res
