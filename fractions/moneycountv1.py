import random

a = 'DCNP'

def get_rand(a,b):
    return str(random.randint(a,b))

for i in range(20):
    print(get_rand(1,100)+" D + " + get_rand(1,10)+" C + " + get_rand(1,10)+" N + " +get_rand(1,100) + " P =")

for j in range(int(input())):
    print("money-counting")
    print()
    for i in range(20):
        r = get_rand(2,4)
        l = random.sample(a,int(r))
        z = ""
        k = []
        if 'D' in l:
            k.append('D')
        if 'C' in l:
            k.append('C')
        if 'N' in l:
            k.append('N')
        if 'P' in l:
            k.append('P')

        for i in k:
            if i == 'D' or i=='P':
                z+=get_rand(1,100) +" "+ i + " + "
            else:
                z+=get_rand(1,10) +" "+ i +" + "
        z = z[:-2]
        print(z+"=")
    print()