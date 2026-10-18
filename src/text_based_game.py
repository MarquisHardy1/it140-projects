
# Name: Marquis Hardy
# Course: Project Two - Text-Based Game
# Description: A cybersecurity adventure game where the player
# collects six security items before confronting a hacker.

def show_instructions():
    """Display the game instructions and available commands."""
    print("\nCybersecurity Adventure Game")
    print("Collect all 6 security items before confronting the hacker!")
    print("Move commands: go north, go south, go east, go west")
    print("Collect items: get [item name]")
    print("Type 'quit' to exit the game.")


def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and room item."""
    print("\n------------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])

    print("------------------------------")


def main():
    """Run the main gameplay loop."""

    # Dictionary connecting rooms and their items.
    rooms = {
        "Server Room": {
            "north": "Network Closet",
            "east": "Help Desk"
        },
        "Network Closet": {
            "south": "Server Room",
            "east": "Security Office",
            "item": "Router"
        },
        "Help Desk": {
            "west": "Server Room",
            "south": "Monitoring Center",
            "item": "Access Card"
        },
        "Security Office": {
            "west": "Network Closet",
            "north": "Hacker's Hideout",
            "east": "Database Vault",
            "south": "Monitoring Center",
            "item": "Firewall Rules"
        },
        "Database Vault": {
            "west": "Security Office",
            "south": "Backup Room",
            "item": "Encryption Key"
        },
        "Backup Room": {
            "north": "Database Vault",
            "west": "Monitoring Center",
            "item": "Backup Drive"
        },
        "Monitoring Center": {
            "east": "Backup Room",
            "north": "Help Desk",
            "item": "Audit Logs"
        },
        "Hacker's Hideout": {
            "south": "Security Office",
            "item": "Hacker"
        }
    }

    current_room = "Server Room"
    inventory = []
    total_items = 6

    show_instructions()

    # Continue playing until the player wins, loses, or quits.
    while True:
        show_status(current_room, inventory, rooms)

        command = input("Enter your move: ").strip().lower()

        # Allow the player to quit the game.
        if command == "quit":
            print("Thanks for playing the game. Goodbye!")
            break

        # Handle movement commands.
        elif command.startswith("go "):
            direction = command[3:].strip()

            if direction in rooms[current_room]:
                next_room = rooms[current_room][direction]

                # Check whether the player entered the villain's room.
                if next_room == "Hacker's Hideout":
                    if len(inventory) == total_items:
                        print(
                            "\nCongratulations! You collected all "
                            "six security items and defeated the hacker!"
                        )
                    else:
                        print(
                            "\nGAME OVER! You encountered the hacker "
                            "before collecting all six security items."
                        )

                    print("Thanks for playing the game. Hope you enjoyed it.")
                    break

                current_room = next_room

            else:
                print("You cannot go that way. Try another direction.")

        # Handle item collection commands.
        elif command.startswith("get "):
            item_name = command[4:].strip().lower()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if room_item.lower() == item_name:
                    inventory.append(room_item)
                    print("You collected:", room_item)

                    # Remove the item so it cannot be collected twice.
                    del rooms[current_room]["item"]

                else:
                    print("That item is not in this room.")

            else:
                print("There is no item to collect in this room.")

        # Handle invalid commands.
        else:
            print(
                "Invalid command. Enter 'go north', 'go south', "
                "'go east', 'go west', or 'get [item name]'."
            )


# Start the game.
if __name__ == "__main__":
    main()
