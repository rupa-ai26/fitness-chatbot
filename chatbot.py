print("====================================")
print("      FITNESS AI CHATBOT 💪")
print("====================================")

print("Hello! I'm your Fitness Assistant.")
print("I can help you with workouts, food, water, sleep, and fitness goals.")
print("Type 'bye' to exit.")

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye! Stay healthy and keep moving! 💪")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! 👋 How can I help you with your fitness today?")

    elif "weight loss" in user_input or "lose weight" in user_input:
        print("\nBot: For weight loss, try this beginner workout:")
        print("1. Brisk walking - 20 minutes")
        print("2. Squats - 10 reps")
        print("3. Lunges - 8 reps each leg")
        print("4. Jumping jacks - 15 reps")
        print("5. Plank - 20 seconds")
        print("Bot: Start slowly and increase gradually.")

    elif "muscle" in user_input or "muscle building" in user_input:
        print("\nBot: For muscle building, try this beginner workout:")
        print("1. Squats - 10 reps")
        print("2. Push-ups or wall push-ups - 8 reps")
        print("3. Lunges - 8 reps each leg")
        print("4. Glute bridges - 12 reps")
        print("5. Plank - 20 seconds")
        print("Bot: Focus on proper form and allow recovery between workouts.")

    elif "fitness" in user_input or "fit" in user_input:
        print("\nBot: For general fitness, try:")
        print("1. Walking - 15 minutes")
        print("2. Squats - 10 reps")
        print("3. Wall push-ups - 10 reps")
        print("4. Lunges - 8 reps each leg")
        print("5. Stretching - 5 minutes")

    elif "workout" in user_input or "exercise" in user_input:
        print("Bot: Tell me your goal: weight loss, muscle building, or general fitness.")

    elif "food" in user_input or "diet" in user_input:
        print("Bot: Try including vegetables, fruits, whole grains, pulses, and adequate protein.")

    elif "water" in user_input:
        print("Bot: Staying hydrated is important. Drink water regularly throughout the day.")

    elif "sleep" in user_input:
        print("Bot: Good sleep supports recovery and overall health. Try maintaining a regular sleep schedule.")

    else:
        print("Bot: I'm still learning! Try asking me about workouts, food, water, sleep, or fitness goals.")