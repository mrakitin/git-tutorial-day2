def say_hello(say=True, msg=""):
    if say:
        print(f"{msg = }")


if __name__ == "__main__":
    say_hello(msg="Test")
