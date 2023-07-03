def check_name(name):
    with open("names.csv","r") as f:
        users = f.read().splitlines()
        for user in users:
            args = user.split(",")

        while True:
            if args[0] == name:

                break
            else:
                pass



def check_email(email):
    with open("names.csv","r") as f:
        users = f.read().splitlines()
        for user in users:
            args = user.split(",")
        while True:
            if args[2] == email:

                break
            else:
                pass



def check_password(password):
    with open("names.csv","r") as f:
        users = f.read().splitlines()
        for user in users:
            args = user.split(",")
        while True:
            if args[1] == password:

                break
            else:
                pass



while True:

    in_name = input('Ur name:\n')
    in_email = input('Ur email:\n')
    in_password = input('Ur password:\n')

    if check_name(in_name):
        pass
    elif check_email(in_email):
        pass
    elif check_password(in_password):
        pass
    else :
        print('U successfully enter')

    print(f'U successfully enter to ur account "{in_name}"\n*********Hello*World***********')