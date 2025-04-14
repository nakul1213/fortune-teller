 
def main():
    # Welcome message with your name and admission number
    # Replace "YOUR NAME" and "YOUR_ADMISSION_NUMBER" with your actual details
    print("🔮 Welcome to Nakul's Fortune Teller (21je0477)🔮")
    
    # Prompt for mood
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()
    
    # Fortune based on mood
    if mood == "happy":
        print("✨ Your fortune: Great things await you, Nakul! Keep smiling.✨")
    elif mood == "sad":
        print("✨ Your fortune: Nakul, Better days are coming. The sun will shine again soon.✨")
    elif mood == "neutral":
        print("✨ Your fortune: Nakul, Balance leads to clarity. A decision awaits you.✨")
    else:
        print("I don't understand that mood. Please enter 'happy', 'sad', or 'neutral'.")

if __name__ == "__main__":
    main()
