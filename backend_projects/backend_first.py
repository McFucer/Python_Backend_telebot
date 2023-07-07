import csv
import re
from backend_class import UserValidator

while True:
    reg = input('1. Login'
                    '\n2. Register'
                  '\n3. Log Out \n__')
    if reg != "1" and reg != "2" and reg != "3":
        print('Choose option\n'             
              '                            |like|\n'
              '                            | __1|')
        continue

    else :
        break


if reg == '3':
    print('out')


# def check_name(name):
#     with open("names.csv","r") as f:
#         users = f.read().splitlines()
#         for user in users:
#             args = user.split(",")
#
#         while True:
#             if args[0] == name:
#
#                 break
#             else:
#                 pass
#
#
#
# def check_email(email):
#     with open("names.csv","r") as f:
#         users = f.read().splitlines()
#         for user in users:
#             args = user.split(",")
#         while True:
#             if args[2] == email:
#
#                 break
#             else:
#                 pass
#
#
#
# def check_password(password):
#     with open("names.csv","r") as f:
#         users = f.read().splitlines()
#         for user in users:
#             args = user.split(",")
#         while True:
#             if args[1] == password:
#
#                 break
#             else:
#                 pass
#







while reg == '1':
    validator = UserValidator()
    # in_name = input('Ur name:\n')
    # in_email = input('Ur email:\n')
    # in_password = input('Ur password:\n')
    name_exists = validator.check_name(input('Ur name:\n'))
    email_exists = validator.check_email(input('Ur email:\n'))
    password_exists = validator.check_password(input('Ur password:\n'))

    if name_exists is False:
        continue
    elif email_exists is False:
        continue
    elif password_exists is False:
        continue
    else:
        print('U successfully enter')

    print(f'U successfully enter to ur account "{name_exists}"\n*********Hello*World***********')

    while True:
        main_menu = input('Okay, choose option'
                          '\n    1.Shop'
                          '\n    2.Balance'
                          '\n    3.Donate\n    4.Out\n__')
        # def user_money():
        with open('balance.csv', 'r') as f:
            users = f.read().splitlines()
            for user in users:
                args = user.split(",")




        # def check_money_gta5():
        #     with open('names.csv', 'r') as f:
        #         users = f.read().splitlines()
        #         for user in users:
        #             args = user.split(",")
        #         if args[3] >= 10:
        #             pass
        #


        if main_menu == '1':
            print('1. GTA 5 -> 10$'
                  '\n2. Detroit: Become Human -> 8$')
            choose_game = input('__')
            gta = 10
            detroit = 8

            if choose_game == '1':
                print('U sure that u want to buy GTA 5'
                      '\n1.yes'
                      '\n2.no'
                      f'\n                                                 (ur balance is: {args[0]})')
                gta_choose_yes_no = input('__')


                if gta_choose_yes_no == '1' and int(args[0]) >= 10:
                    print('U successfully bought the product')
                    result = int(args[0]) - gta
                    print(f'Money left: {result}')

                    with open('balance.csv', 'w', newline='') as scvfile:
                        fieldnam = ['Money']
                        writer_suck = csv.DictWriter(scvfile, fieldnames=fieldnam)

                        writer_suck.writeheader()
                        writer_suck.writerow({'Money': f'{result}'})



                elif gta_choose_yes_no != '1':
                    print('U cancelled the purchase')
                    continue
                else:
                    print('Unfortunately, u dont have 10$ in ur balance')
            elif choose_game == '2':
                with open('balance.csv', 'r') as f:
                    users = f.read().splitlines()
                    for user in users:
                        args = user.split(",")
                print('U sure that u want to buy Detroit'
                      '\n1.yes'
                      '\n2.no'
                      f'\n                                                 (ur balance is: {args[0]})')
                detroit_choose_yes_no = input('__')

                if detroit_choose_yes_no == '1' and int(args[0]) >= gta:
                    print('U successfully bought the product')
                    result = int(args[0]) - detroit
                    print(f'Money left: {result}')

                    with open('balance.csv', 'w', newline='') as scvfile:
                        fieldnam = ['Money']
                        writer_suck = csv.DictWriter(scvfile, fieldnames=fieldnam)

                        writer_suck.writeheader()
                        writer_suck.writerow({'Money': f'{result}'})


                elif detroit_choose_yes_no != '1':
                    print('U cancelled the purchase')
                    continue
                else:
                    print('Unfortunately, u dont have 8$ in ur balance')
        elif main_menu == '2':
            with open('balance.csv', 'r') as f:
                users = f.read().splitlines()
                for user in users:
                    args = user.split(",")
            print(f'Ur balance is {args[0]}')
        elif main_menu == '3':
            print('How much money u wanna donate:')
            while True:
                try:
                    donate_money = int(input(''))
                except ValueError:
                    print('Dont write any letters or symbols.')
                    continue

                with open('balance.csv', 'r') as f:
                    users = f.read().splitlines()
                    for user in users:
                        args = user.split(",")

                result4bal = int(args[0]) + donate_money

                with open('balance.csv', 'w', newline='') as scvfile:
                    fieldname = ['Money']
                    writer_suck = csv.DictWriter(scvfile, fieldnames=fieldname)

                    writer_suck.writeheader()
                    writer_suck.writerow({'Money': f'{result4bal}'})

                break


        elif main_menu == '4':
            break

        else :
            print('Dont write any letters or symbols')
            continue



    # in_name = input('Ur name:')
    # if check_name(in_name):
    #     print('a')
    # else :
    #     continue
    #
    # in_email = input('Ur email:')
    # if check_email(in_email):
    #     print('a')
    # else:
    #     continue
    #
    # in_password = input('Ur password:')
    # if check_password(in_password):
    #     print('a')
    # else :
    #     continue


    break

while reg == '2':




    name = input('Ur name:\n')

    if not name.isalpha():
        print('Dont write numbers or probels')
        continue
    email = input('Ur email:\n')
    if re.search('@', email):
        pass
    else :
        print('Email should have "@"')
        continue

    password = input('Ur password:\n')
    if len(password) < 6:
        print('Ur password must have more than 6 symbols!')
        continue

    card = input('Ur card:\n')

    if len(card) != 16 :
        print('Card must include 16 numbers, no more')
        continue
    print('User is appended successfully')

    while True:
        try:
            money = int(input('how much money u want to donate:\n'))
        except ValueError:
            print('Only numbers')
            continue
        with open('balance.csv','w',newline='') as scvfile:
            fieldname = ['Money']
            writer_sucka = csv.DictWriter(scvfile, fieldnames=fieldname)

            writer_sucka.writeheader()
            writer_sucka.writerow({'Money':f'{money}'})
        break




    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Password', 'Email', 'Money']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(
            {f'Name': f'{name}', 'Password': f'{password}', 'Email': f'{email}'})
    break



while reg == '2':
    main_menu = input('Okay, choose option'
                 '\n    1.shop'
                 '\n    2.balance'
                     '\n    3.Donate\n    4.Out\n__')
    with open('balance.csv','r') as f:
        users = f.read().splitlines()
        for user in users:
            args = user.split(",")



    if main_menu == '1' :
        print('1. GTA 5 -> 10$'
                  '\n2. Detroit: Become Human -> 8$')
        choose_game = input('__')
        gta = 10
        detroit = 8

        if choose_game == '1':
            print('U sure that u want to buy GTA 5'
                  '\n1.yes'
                  '\n2.no'
                  f'\n                                                 (ur balance is: {args[0]})')
            gta_choose_yes_no = input('__')


            if gta_choose_yes_no == '1' and int(args[0]) >= gta:
                print('U successfully bought the product')
                result4reg = int(args[0]) - 10

                with open('balance.csv', 'w', newline='') as scvfile:
                    fieldnam = ['Money']
                    writer_suck = csv.DictWriter(scvfile, fieldnames=fieldnam)

                    writer_suck.writeheader()
                    writer_suck.writerow({'Money': f'{result4reg}'})

            elif gta_choose_yes_no != '1':
                print('U cancelled the purchase')
                continue
            else :
                print('Unfortunately, u dont have 10$ in ur balance')
        elif choose_game == '2':
            with open('balance.csv', 'r') as f:
                users = f.read().splitlines()
                for user in users:
                    args = user.split(",")

            print('U sure that u want to buy Detroit'
                  '\n1.yes'
                  '\n2.no'
                  f'\n                                                 (ur balance is: {args[0]})')
            detroit_choose_yes_no = input('__')
            if detroit_choose_yes_no == '1' and int(args[0]) >= gta:
                print('U successfully bought the product')
                result = int(args[0]) - detroit
                with open('balance.csv', 'w', newline='') as scvfile:
                    fieldnam = ['Money']
                    writer_suck = csv.DictWriter(scvfile, fieldnames=fieldnam)

                    writer_suck.writeheader()
                    writer_suck.writerow({'Money': f'{result}'})


            elif detroit_choose_yes_no != '1':
                print('U cancelled the purchase')
                continue
            else :
                print('Unfortunately, u dont have 8$ in ur balance')
    elif main_menu == '2':
        with open('balance.csv', 'r') as f:
            users = f.read().splitlines()
            for user in users:
                args = user.split(",")

        print(f'Ur balance is {args[0]}')

    elif main_menu == '3':
        print('How much money u wanna donate:')
        while True:
            try:
                donate_money = int(input(''))
            except ValueError:
                print('Dont write any letters or symbols.')
                continue

            with open('balance.csv', 'r') as f:
                users = f.read().splitlines()
                for user in users:
                    args = user.split(",")

            result4bal = int(args[0]) + donate_money

            with open('balance.csv', 'w', newline='') as scvfile:
                fieldname = ['Money']
                writer_suck = csv.DictWriter(scvfile, fieldnames=fieldname)

                writer_suck.writeheader()
                writer_suck.writerow({'Money': f'{result4bal}'})

            break


    elif main_menu == '4':
        break

    else:
        print('Write only number')
        continue



print('      ______       ')
print('     /HELLO!\      ')
print('    /  BRUV  \     ')
print('   /|________|\     ')
print('    |   __   |      ')
print('    |  |__|  |      ')
print('    |________|      ')