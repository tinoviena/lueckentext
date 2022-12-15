def count_correct_answers():
    global x
    x = 1
    def inc():
        print(x+1)
    inc()
    return inc

if __name__ == '__main__':
    f = count_correct_answers()
    f()
    f()
    f()
