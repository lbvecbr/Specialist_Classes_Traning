import mNakladnaya, mDocument
import optparse
import sqlite3



if __name__ == "__main__":
    op = optparse.OptionParser()
    op.add_option("-i", "--initdb", dest="initdb",
                  action="store_true", default=False,
                  help="Initialise database")
    (options ,args) = op.parse_args()
    if(options.initdb):
        try:
            mDocument.Document.create_table()
        except sqlite3.OperationalError as Exc:
            print(Exc.message)
    else:
        Nak = mNakladnaya.create()
        Nak.append_blank()
        Nak[0].title = "Penciles"
        Nak[0].unit = "piece"

        print(Nak)
