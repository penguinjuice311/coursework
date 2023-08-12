from website import create_app

def main():
    app = create_app()

    print("running")

    app.run(debug = True)


if __name__ == "__main__":
    main()
