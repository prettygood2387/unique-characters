if __name__ = '__main__':
    import random
    lower = 'abcdertwqazxcbnmkopuiyglur'
    upper = lower.upper()
    special = '!@#$%^&*()_+<>?/:;'
    digits = '123456789'
    all = lower + upper + special + digits

    password = ""

    for m in range(1,16):
        password = "".join([password,random.choice(all)])
    print(password)
