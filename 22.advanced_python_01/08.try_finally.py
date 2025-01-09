def main():
    
    try :
        num = input("Enter a number: ")
        print(int(num))
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("inside finally")

    
main()