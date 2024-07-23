print("hello")

def decode(password):
    nums = []
    for i in password:
        num = int(i) - 3
        nums.append(str(num))
    decoded_pass = ''.join(nums)
    return decoded_pass
