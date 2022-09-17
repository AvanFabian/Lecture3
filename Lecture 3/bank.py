#Lecture3 Assignment

answer = input("Greeting : ").strip().lower()

if answer == "hello" or answer == "hello, Newman":
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")
