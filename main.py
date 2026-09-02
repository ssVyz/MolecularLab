from objects import *



def main() -> None:


    ######### Placeholder tests ##########
    print("provisional test suite")

    print("Test 1: Make an object and check its contents")
    testobj1 = Lab_object()
    testobj1.quick_setup("test1", 5, 2, 2)
    testobj1.show_info()

    print("End of content")


if __name__ == "__main__":
    main()
