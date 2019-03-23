import mNakladnaya

if __name__ == "__main__":
    Nak = mNakladnaya.create()
    Nak.append_blank()
    Nak[0].title = "Penciles"
    Nak[0].unit = "piece"

    print(Nak)
