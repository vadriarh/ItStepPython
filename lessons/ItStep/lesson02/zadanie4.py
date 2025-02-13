dataPoezdki = int(input("V kakoi dzien\' miesiaca vi edziecie s Warszawy do Krakow: "))
if (1 <= dataPoezdki <= 12):
    if (dataPoezdki % 3 == 1):
        print("Poezd otpravlyaetsya s Zachodnaya v 12.00")
    elif (dataPoezdki % 3 == 2):
        print("Poezd otpravlyaetsya s Central/'naya v 14.00")
    elif (dataPoezdki % 3 == 0):
        print("Poezd otpravlyaetsya s Vostocznaya v 15.00")
else:
    print("V etot dzien\' poezda net")
