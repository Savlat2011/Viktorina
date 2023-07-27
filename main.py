
def quiz_question(question, correct_answer):
    user_answer = input(question)
    if user_answer.strip().lower() == correct_answer.lower():
        print("Rätt svar!")
        return True
    else:
        print("Fel svar! Rätt svar är", correct_answer)
        return False

def main():
    namn = input("Vad heter du? ")
    print("Hej " + namn + " och välkommen till viktorinan om huvudstäder. Du ska svara på några frågor för att vinna.")

    score = 0

    if quiz_question("Vad heter Sveriges huvudstad? ", "Stockholm"):
        score += 1

    if quiz_question("Vad heter Serbiens huvudstad? ", "Belgrad"):
        score += 1

    if quiz_question("Vad heter Russlands huvudstad? ", "Moskva"):
        score += 1

    if quiz_question("Vad heter Greklands huvudstad? ", "Athen"):
        score += 1

    if quiz_question("Vad heter Finlands huvudstad? ", "Helsingfors"):
        score += 1

    print("Ditt resultat:", score, "av 5 möjliga.")

if __name__ == "__main__":
    main()
