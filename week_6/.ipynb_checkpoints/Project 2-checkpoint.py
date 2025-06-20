def check_admission():
    admitted = []
    not_admitted = []

    print("🎓 University Admission Checker")
    print("----------------------------------\n")

    while True:
        name = input("Enter candidate's name (or type 'exit' to stop): ").strip()
        if name.lower() == 'exit':
            break

        department = input("Enter department (Computer Science / Mass Communication): ").strip().lower()
        try:
            jamb_score = int(input("Enter JAMB score: "))
            credits = int(input("Enter number of credits in 5 key subjects: "))
            interview = input("Did they pass the interview? (yes/no): ").strip().lower()
        except ValueError:
            print("❌ Invalid input. Try again.\n")
            continue

        passed = False

        if department == "computer science":
            if jamb_score >= 250 and credits >= 5 and interview == "yes":
                passed = True
        elif department == "mass communication":
            if jamb_score >= 230 and credits >= 5 and interview == "yes":
                passed = True
        else:
            print("❌ Unknown department. Please choose either Computer Science or Mass Communication.\n")
            continue

        if passed:
            admitted.append(name)
            print(f"✅ {name} has been admitted to {department.title()}.\n")
        else:
            not_admitted.append(name)
            print(f"❌ {name} did not meet the requirements.\n")

    print("\n📋 Final Summary:")
    print("Admitted Candidates:", admitted)
    print("Not Admitted Candidates:", not_admitted)
    print("\n✨ Program by: Ameerah <3💻 (hidden signature 😉)")

# Hidden signature (AO)
def _signature():
    return "Code crafted with care by Ameerah<3 🧠"

# Run the function
check_admission()