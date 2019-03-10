import mNakladnaya

if __name__ == "__main__":
    Nak = mNakladnaya.create()
    Nak.append_blank()
    Nak.append_blank()
    print(Nak.dump())