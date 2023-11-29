from website import create_app


SCHOOL_CON_STRING = ( "Driver={SQL Server};"
                    "Server=svr-cmp-01;"
                    "Database=22Stocksc858")

HOME_CON_STRING = ( "Driver={SQL Server};"
                    "Server=LAPTOP-D9N8OC65;"
                    "Database=Coursework")


def main():
    Input = input("school or home (s/h)? ")
    while Input not in ("s", "h"):
        Input = input("school or home (s/h)? ")

    constring = SCHOOL_CON_STRING if Input == "s" else HOME_CON_STRING



    app = create_app(constring)

    app.config["SECRET_KEY"] = "ILOVESPONGEBOB"


    app.run(debug = True)


if __name__ == "__main__":
    main()
