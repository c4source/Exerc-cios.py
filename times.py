def main():

    from datetime import datetime 

    dia = datetime.today().strftime('%d/%m')

    if dia == '11/05':
        print('Feliz dia das mães')


if __name__ == "__main__":
    main()    