import add
import os
import search
import list_word
def menus():
    while True:
        print()
        print("\t##### Menu #####\n\n1.Yangi so'z qo'shish\n2.So'z qidirish\n\tEn->Uz\n\tUz->En\n3.Mavjud so'zni o'zgartirish\n4.Ro'yhatni ko'rish\n5.Chiqish")
        n = int(input("Marhamat kerakli menuni tanlang👉 "))
        if n == 1:
            add.inp()
        elif n == 2:
            search.search()
            print("Chiqish.0")
            if input(">>> ") == 0:
                break
            else:
                search.search()
        elif n == 3:
            print()
            print("++++++++++++++++++++++++++++++")
            print("+ BU bo'lim hali qo'shilmagan+")
            print("++++++++++++++++++++++++++++++")
            print()

        elif n == 4:
            list_word.list_word()
            print("Chiqish.0")
            if input(">> ") == 0:
                break
            os.system("cls")
        elif n == 5:
            print("Bye Bye👋")
            break
        else:
            print("++++++++++++++++++++")
            print("||Bunday Menu yo'q||")
            print("++++++++++++++++++++")
            print()
menus()
