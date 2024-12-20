from peli_tehdas import luo_peli

def main():
    print("Valitse pelityyppi:")
    print("(a) Ihminen vs. Ihminen")
    print("(b) Ihminen vs. Yksinkertainen tekoäly")
    print("(c) Ihminen vs. Monimutkainen tekoäly")
    tyyppi = input()

    peli = luo_peli(tyyppi)
    if peli:
        peli.pelaa()
    else:
        print("Virheellinen valinta")

if __name__ == "__main__":
    main()
