sentence = input("enter a sentence or title: ").lower()
chances = int(input("enter number of attempts: "))

used_letters = []

print("\n🎮 hangman game started")

while chances > 0:
    output = ""

    for letter in sentence:
        if letter == " ":
            output = output + " "
        elif letter in used_letters:
            output = output + letter
        else:
            output = output + "_"

    print("\n🔤", output)
    print("❤️ attempts left:", chances)

    if output == sentence:
        print("🎉 you guessed the sentence correctly!")
        break

    guess = input("guess a letter ✍️: ").lower()

    if len(guess) != 1:
        print("⚠️ please enter only one letter")
        continue

    if guess in used_letters:
        print("🔁 you already guessed this letter")
        continue

    if guess in sentence:
        used_letters.append(guess)
        print("✅ correct guess")
    else:
        used_letters.append(guess)
        chances = chances - 1
        print("❌ wrong guess")

if chances == 0:
    print("💀 you lost")
    print("📌 correct sentence was:", sentence)