def test(func, a):
    try:
        assert func == a
    except Exception:
        print("{} != {}".format(func, a))


def mul(x, y):
    return int(bin(int(str(x), 2) * (int(str(y), 2)))[2:])


if __name__ == "__main__":
    test(mul(1100, 1010), 1111000)
    test(mul(110, 1010), 111100)
    test(mul(11, 1010), 11110)
    test(mul(1, 1010), 1010)
    test(mul(0, 1010), 0)
    test(mul(111, 111), 110001)
    test(mul(11, 11), 1001)
    print("Ok tested")
    input()
