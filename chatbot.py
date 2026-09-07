def get_bot_response(user_input):
    user_input = user_input.lower()

    if user_input == "bye":
        return "Goodbye! Stay healthy and keep moving! 💪"

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 How can I help you with your fitness today?"

    elif "weight loss" in user_input or "lose weight" in user_input:
        return """For weight loss, try this beginner workout:

1. Brisk walking - 20 minutes
2. Squats - 10 reps
3. Lunges - 8 reps each leg
4. Jumping jacks - 15 reps
5. Plank - 20 seconds

Start slowly and increase gradually. 💪"""

    elif "muscle" in user_input or "muscle building" in user_input:
        return """For muscle building, try this beginner workout:

1. Squats - 10 reps
2. Push-ups or wall push-ups - 8 reps
3. Lunges - 8 reps each leg
4. Glute bridges - 12 reps
5. Plank - 20 seconds

Focus on proper form and allow recovery between workouts. 💪"""

    elif "fitness" in user_input or "fit" in user_input:
        return """For general fitness, try:

1. Walking - 15 minutes
2. Squats - 10 reps
3. Wall push-ups - 10 reps
4. Lunges - 8 reps each leg
5. Stretching - 5 minutes"""

    elif "workout" in user_input or "exercise" in user_input:
        return """Here is a simple beginner workout plan:

🏃 Warm-up - 5 minutes

💪 Main Workout:
1. Squats - 3 sets × 10 reps
2. Push-ups - 3 sets × 8 reps
3. Lunges - 3 sets × 8 each leg
4. Glute bridges - 3 sets × 12 reps
5. Plank - 3 × 20 seconds

🧘 Cool-down - 5 minutes

Take rest between sets and focus on proper form."""

    elif "food" in user_input or "diet" in user_input:
        return """🥗 Beginner Healthy Diet Plan

🌅 Breakfast:
• Oats or whole-grain breakfast
• 1 fruit
• Milk or curd

🍎 Mid-Morning:
• One fruit or a handful of nuts

🍛 Lunch:
• Rice or roti
• Dal/pulses
• Plenty of vegetables
• Curd

☕ Evening:
• Fruit or roasted nuts

🌙 Dinner:
• Roti or a moderate portion of rice
• Vegetables
• Dal/paneer/another protein source

💧 Drink water regularly throughout the day.

Focus on balanced, nutritious foods and appropriate portions."""

    elif "water" in user_input or "hydration" in user_input:
        return """💧 Daily Hydration Guide

• Drink water regularly throughout the day
• Have a glass of water after waking up
• Drink water with meals
• Drink more during exercise or hot weather
• Keep a water bottle with you

Your exact water needs depend on your body, activity level, climate, and other factors."""

    elif "sleep" in user_input:
        return """😴 Sleep & Recovery Guide

• Aim for a consistent sleep schedule
• Keep your bedroom comfortable and quiet
• Reduce phone/screen use before bedtime
• Avoid heavy meals close to bedtime
• Give your body enough time to recover after workouts

Good sleep supports recovery, energy, and overall health."""

    else:
        return "I'm still learning! Try asking me about workouts, food, water, sleep, or fitness goals."