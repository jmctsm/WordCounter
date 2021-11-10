"""
 contains the function to generate the words to look up in the API

"""


def char_gen_func():
    print("here2")
    for i in range(10):
        print("here")
        print(f"{ i= }")
        yield


def test_pass():
    print("test_pass")


if __name__ == "__main__":
    print("Starting\n")
    test_pass()
    char_gen_func()
    test_pass()
    print("\nEnding\n")
