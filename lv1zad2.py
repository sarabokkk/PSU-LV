while True:
    try:
        unos = float(input("Unesite ocjenu unutar intervala [0.0-1.0]: "))
        if 0.0 <= unos <= 1.0:
            break
        else:
            print("Greska! Potrebno je unesti broj unutar trazenog intervala!")
    except ValueError:
        print("Greska! Potrebno je unijeti broj!")

    if unos >= 0.9:
        print("Ocjena je A!")
    elif unos < 0.9 and unos >= 0.8:
        print("Ocjena je  B!")
    elif unos < 0.8 and unos >= 0.7:
        print("Ocjena je  C!")
    elif unos < 0.7 and unos >= 0.6:
        print("Ocjena je  D!")
    else:
        print("Ocjena je F!")