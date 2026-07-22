from timer import start_timer, stop_timer, view_sessions

while True:
    print("\n" + "=" * 40)
    print("⏱️ DevTimerX")
    print("=" * 40)
    print("1. Start Timer")
    print("2. Stop Timer")
    print("3. View Sessions")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        project = input("Project Name: ")
        start_timer(project)

    elif choice == "2":
        stop_timer()

    elif choice == "3":
        view_sessions()

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
