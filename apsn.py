# Define functions for different topics
def mythical_creatures():
    print("Mythical Creatures:")
    print("1. Centaur")
    print("2. Griffin")
    print("3. Minotaur")
    sub_choice = input("Enter the number of the creature to learn more or 'b' to go back: ")

    if sub_choice == "1":
        print("Centaur:")
        print("   In Greek mythology, centaurs were creatures with the upper body of a human and the lower body of a horse.")
        print("   They were often depicted as wild and unruly, symbolizing the struggle between civilization and instinct.")
    elif sub_choice == "2":
        print("Griffin:")
        print("   A mythical creature with the body of a lion and the head of an eagle, representing strength and majesty.")
        print("   Griffins were often associated with guarding valuable treasures.")
    elif sub_choice == "3":
        print("Minotaur:")
        print("   The Minotaur was a half-human, half-bull creature trapped in the labyrinth of King Minos of Crete.")
        print("   It was eventually slain by the hero Theseus.")
    elif sub_choice.lower() == "b":
        return
    else:
        print("Invalid choice.")

def heroic_ethics():
    print("Heroic Ethics:")
    print("1. Hubris")
    print("2. Xenia")
    print("3. Arete")
    sub_choice = input("Enter the number of the ethic to learn more or 'b' to go back: ")

    if sub_choice == "1":
        print("Hubris:")
        print("   Hubris refers to excessive pride or arrogance that often led to the downfall of heroes in Greek myths.")
        print("   Examples include Icarus flying too close to the sun and the story of Niobe.")
    elif sub_choice == "2":
        print("Xenia:")
        print("   Xenia is the concept of hospitality and guest-friendship in Greek culture.")
        print("   It was considered a sacred duty to welcome and provide for guests, often with elaborate feasts.")
    elif sub_choice == "3":
        print("Arete:")
        print("   Arete means excellence and virtue. Heroes were expected to strive for arete in both physical and moral aspects.")
        print("   Notable examples of arete include Achilles and Odysseus.")
    elif sub_choice.lower() == "b":
        return
    else:
        print("Invalid choice.")

def architectural_legacy():
    print("Architectural Legacy:")
    print("1. Parthenon")
    print("2. Amphitheaters")
    print("3. Columns")
    sub_choice = input("Enter the number of the architectural feature to learn more or 'b' to go back: ")

    if sub_choice == "1":
        print("Parthenon:")
        print("   The Parthenon is a temple on the Acropolis of Athens dedicated to the goddess Athena.")
        print("   It is a symbol of classical Greek architecture and is known for its Doric columns and intricate sculptures.")
    elif sub_choice == "2":
        print("Amphitheaters:")
        print("   Ancient Greeks built amphitheaters like the Theater of Epidaurus for performances and festivals.")
        print("   The most famous amphitheater is the Colosseum in Rome.")
    elif sub_choice == "3":
        print("Columns:")
        print("   Greek architecture features three main column styles: Doric, Ionic, and Corinthian, each with distinct designs.")
    elif sub_choice.lower() == "b":
        return
    else:
        print("Invalid choice.")

# Define a dictionary to map user input to functions
topic_functions = {
    "1": mythical_creatures,
    "2": heroic_ethics,
    "3": architectural_legacy,
}

# Main loop of the CLI
while True:
    # Display menu
    print("\nWelcome to the Greek Mythology CLI!")
    print("Choose a topic:")
    print("1. Mythical Creatures")
    print("2. Heroic Ethics")
    print("3. Architectural Legacy")
    print("4. Quit")

    choice = input("Enter the number of your choice: ")

    if choice == "4":
        print("Goodbye!")
        break
    elif choice in topic_functions:
        # Call the appropriate function based on user input
        topic_functions[choice]()
    else:
        print("Invalid choice. Please select a valid option.")
