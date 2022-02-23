def ex_1_12_3():
    c = 0
    for f in range(50, 150, 1):
        c = 5/9 * (f-32)
        print("%.0f °F = %.2f °C" % (f, c))
