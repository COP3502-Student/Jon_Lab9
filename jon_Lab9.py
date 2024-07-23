
def encode(password):
    encoded = ''
    for i in range(len(password)):
        n = int(password[i])
        nn = (n + 3) % 10
        encoded = encoded + str(nn)
    return encoded

def decode(password):
    nums = []
    for i in password:
        num = int(i) - 3
        nums.append(str(num))
    decoded_pass = ''.join(nums)
    return decoded_pass

