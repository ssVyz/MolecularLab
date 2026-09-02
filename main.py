from objects import *



def main() -> None:


    ######### Placeholder tests ##########
    print("provisional test suite")

    print("Test 1: rooms and objects")
    daRoom = Room()
    daRoom.quick_setup(50)
    obj1 = Lab_object("Megablaster 5000")
    obj1.quick_setup("test1", 5, 2, 2)
    obj1.show_info()
    ret = daRoom.place_lab_object(obj1)
    print(ret)
    daRoom.show_info()

    print("End of content")


if __name__ == "__main__":
    main()
