def prime(n):
    # Judge whether n is a prime or not
    if n == 2:
        return True
    elif n == 1:
        return False
    else:
        for i in xrange(1, n + 1):
            if n % i == 0 and i != 1 and i != n:
                return False
        return True


def f(n):
    p = 0
    q = 1
    if n <= 0:
        print "Invalid"
        return
    for i in range(n):
        t = q
        p, q = q, p + q
        if t % 15 == 0:
            print "FizzBuzz"
        elif t % 3 == 0:
            print "Buzz"
        elif t % 5 == 0:
            print "Fizz"
        elif prime(t):
            print "BuzzFizz"
        else:
            print t

# get n from the std in
n = int(raw_input("Input n:" + '\n'))
f(n)
