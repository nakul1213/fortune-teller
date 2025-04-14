import random

def main():
    
    print("🔮 Welcome to Nakul's Fortune Teller (21je0477)🔮")
    
    # Prompt for mood
    print("How are you feeling today? (happy/sad/neutral/stressed/excited): ")
    mood = input().lower()
    
    # Dictionary of fortunes for each mood (multiple options for randomization)
    fortunes = {
        "happy": [
            "✨ Your fortune: Great things await you, Nakul ! Keep smiling.✨",
            "✨ Your fortune: Your happiness will bring joy to others around you, Nakul.✨",
            "✨ Your fortune:  Nakul, a pleasant surprise is on its way to you!✨"
        ],
        "sad": [
            "✨ Your fortune: Nakul, Better days are coming. The sun will shine again soon.✨",
            "✨ Your fortune: A friend is thinking of you right now Nakul, and wishes you well.✨",
            "✨ Your fortune: This feeling is temporary Nakul. Joy awaits you tomorrow.✨"
        ],
        "neutral": [
            "✨ Your fortune: Balance leads to clarity Nakul. A decision awaits you.✨",
            "✨ Your fortune: Nakul, An interesting opportunity will present itself soon.✨",
            "✨ Your fortune: Nakul , your calm perspective will help solve a problem.✨"
        ],
        "stressed": [
            "✨ Your fortune: Relief is on the horizon. Take a deep breath Nakul.✨",
            "✨ Your fortune: Nakul , your strength will guide you through this challenge.✨",
            "✨ Your fortune: A moment of peace will bring you the answer you seek Nakul.✨"
        ],
        "excited": [
            "✨ Your fortune: Nakul, Your enthusiasm will lead to success in your endeavor!✨",
            "✨ Your fortune: The path ahead is as bright as your spirit, Nakul !✨",
            "✨ Your fortune: Your excitement is justified Nakul - good news is coming!✨"
        ]
    }
    

    if mood in fortunes:
        fortune = random.choice(fortunes[mood])
        print(fortune)
    else:
        print("I don't recognize that mood. Try happy, sad, neutral, stressed, or excited.")

if __name__ == "__main__":
    main()
