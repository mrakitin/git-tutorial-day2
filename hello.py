def say_hello(say=False, msg="Hello, User!"):
    if say:
        print(f"{msg = }")


if __name__ == "__main__":
    say_hello(say=True, msg="Test")
