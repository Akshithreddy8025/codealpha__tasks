print("🤖 bot: hey! 👋 nice to chat with you")
print("🤖 bot: we can talk like normal (type bye to exit)")

step = 0
mood = ""

while True:
    user = input("you: ").lower()

    if user == "bye":
        print("🤖 bot: bye 👋 take care")
        break

    if step == 0:
        print("🤖 bot: how are you?")
        step = 1

    elif step == 1:
        if user in ["good", "fine", "great", "okay"]:
            mood = "good"
            print("🤖 bot: nice 😊 what are you doing now?")
        elif user in ["sad", "bad", "not good"]:
            mood = "bad"
            print("🤖 bot: oh 😔 hope things get better. what are you doing now?")
        else:
            print("🤖 bot: okay 👍 what are you doing now?")
        step = 2

    elif step == 2:
        print("🤖 bot: do you like technology?")
        step = 3

    elif step == 3:
        print("🤖 bot: cool 👍 now you can ask me general questions")
        step = 4

    else:
        if "your name" in user:
            print("🤖 bot: yes, i am a simple rule based chatbot 🤖")

        elif "how are you" in user:
            if mood == "good":
                print("🤖 bot: yes, i am feeling good too 😊")
            elif mood == "bad":
                print("🤖 bot: yes, i am okay now 👍")
            else:
                print("🤖 bot: yes, i am doing fine 😊")

        elif "what can you do" in user or "help" in user:
            print("🤖 bot: yes, i can chat, answer simple questions and respond politely")

        elif "python" in user:
            print("🤖 bot: yes, python is an easy and powerful programming language 🐍")

        elif "technology" in user:
            print("🤖 bot: yes, technology helps solve real world problems")

        elif "weather" in user:
            print("🤖 bot: no, i can’t check live weather information")

        elif "ai" in user or "machine learning" in user:
            print("🤖 bot: no, i can’t answer advanced ai topics")

        elif user in ["thanks", "thank you"]:
            print("🤖 bot: yes 😊 you are welcome")

        elif user in ["good", "nice"]:
            print("🤖 bot: yes 👍 glad you feel that way")

        else:
            print("🤖 bot: no, i can’t answer that right now")
