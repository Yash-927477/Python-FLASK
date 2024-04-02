#************ Yash Narayan

import random

# Initialize game variables
current_location = "Starship"
health = 100
wallet = 0
backpack = ["spacesuit"]
inventory = []
dragon_visited = False

# Define room descriptions
room_descriptions = {
    "Starship":
    "You are inside your starship. It's equipped with essential tools for your journey.",
    "Enchanted Forest":
    "You enter the Enchanted Forest. Tall trees surround you.",
    "Dragon Village":
    "You arrive at the Dragon Village. The Elder Dragon greets you.",
    "Hidden Cave": "You enter the Hidden Cave. It's dark and mysterious.",
    "Nebula Market":
    "You're in the Nebula Market, surrounded by alien traders.",
}

# Define interactions
interactions = {
    "Elder Dragon":
    "The Elder Dragon greets you, 'Welcome, traveler. How may I assist you?'",
    "Market Trader":
    "The trader at the market stall offers you some items for sale.",
    "Dragon Village Representative":
    "The Dragon Village Representative warns you about the lurking dragon in the village.",
}

# Game loop
while True:
  # Display current location description
  print(room_descriptions[current_location])

  # Display player's status
  print(f"Health: {health}%")
  print(f"Wallet: {wallet} space credits")
  print(f"Backpack: {', '.join(backpack)}")
  if inventory:
    print(f"Inventory: {', '.join(inventory)}")

  # Check for interactions with characters
  if current_location == "Dragon Village" and not dragon_visited:
    print(interactions["Elder Dragon"])
    dragon_visited = True
  elif current_location == "Dragon Village":
    print(interactions["Dragon Village Representative"])

  # Handle player's actions based on the current location
  print("Options:")
  if current_location == "Starship":
    print(
        "[1] Explore the Enchanted Forest, [2] Visit the Dragon Village, [3] Enter the Hidden Cave, [4] Go to the Nebula Market"
    )
  elif current_location == "Enchanted Forest":
    print(
        "[1] Collect glowing mushrooms, [2] Explore deeper into the forest, [3] Return to the Starship"
    )
  elif current_location == "Dragon Village":
    print(
        "[1] Speak to the Elder Dragon, [2] Roam around the village, [3] Stay in the village, [4] Return to the Starship"
    )
  elif current_location == "Hidden Cave":
    print(
        "[1] Investigate the cave paintings, [2] Explore further into the cave, [3] Return to the Starship"
    )
  elif current_location == "Nebula Market":
    print(
        "[1] Trade items with a trader, [2] Explore the market, [3] Return to the Starship"
    )

  action = input("Enter your choice (e.g., '1' or '2', or 'quit' to exit): ")

  # Handle player's choices and location-specific logic
  if action == "quit":
    print("Thanks for playing!")
    break

  if current_location == "Starship":
    if action == "1":
      current_location = "Enchanted Forest"
      health -= 10  # Health deteriorates when exploring
    elif action == "2":
      current_location = "Dragon Village"
    elif action == "3":
      current_location = "Hidden Cave"
    elif action == "4":
      current_location = "Nebula Market"

  elif current_location == "Enchanted Forest":
    if action == "1":
      print("You collect glowing mushrooms and feel invigorated.")
      health += 15  # Health improves when collecting mushrooms
      inventory.append("glowing mushrooms")
    elif action == "2":
      print("You explore deeper into the forest.")
      health -= 20  # Health deteriorates when going deeper
    elif action == "3":
      current_location = "Starship"

  elif current_location == "Dragon Village":
    if action == "1":
      print("You had a conversation with the Elder Dragon.")
    elif action == "2":
      print("You roam around the village and discover a hidden dragon's lair.")
      if random.randint(1, 5) == 1:
        print(
            "A lurking dragon attacks you. You didn't survive the encounter. Game over!"
        )
        break
    elif action == "3":
      print("You decide to stay in the village, enjoying the serenity.")

  elif current_location == "Hidden Cave":
    if action == "1":
      print(
          "You investigate the cave paintings and discover a hidden passage.")
      inventory.append("ancient artifact")
    elif action == "2":
      print("You explore further into the cave.")
      health -= 30  # Health deteriorates when exploring further
    elif action == "3":
      current_location = "Starship"

  elif current_location == "Nebula Market":
    if action == "1":
      print("You trade items with a trader.")
      trade_item = input("Enter an item to trade: ")
      if trade_item in inventory:
        wallet += random.randint(5, 20)  # Random credits earned from trading
        inventory.remove(trade_item)
      else:
        print("You don't have that item in your inventory.")
    elif action == "2":
      print("You explore the market.")
    elif action == "3":
      current_location = "Starship"

  # Game over conditions
  if health <= 0:
    print("You've run out of health. Game over!")
    break
  elif current_location == "Dragon Village" and "key" in inventory:
    print("Congratulations! You found the key and completed your quest.")
    break
