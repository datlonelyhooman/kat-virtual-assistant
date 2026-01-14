from src.assistant import handle_input

def main():
    print("KAT is online. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        response = handle_input(user_input)
        print("KAT:", response)

        if response == "Goodbye!":
            break

if __name__ == "__main__":
    main()
