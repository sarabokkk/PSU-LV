def total_euro():
    unos = int(input("Koliko radnih sati imate po tjednu?"))
    satnica = int(input("Koliko zaradujete po satu?"))
    ukupnaZarada = unos*satnica
    print(f"Vasa zarada je: {ukupnaZarada}$ tjedno.")


total_euro()