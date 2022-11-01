def say_hello(say=False, msg=""):
    if say:
        print(f"{msg = }")


if __name__ == "__main__":
    say_hello(msg="Test")
