class Dog:

    kind = "krancis"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def speak(self, sound):
        return f"{self.name} saka {sound}"

d1 = Dog("Rembo", 3)
d2 = Dog("Tontons", 10)

print("Manu vienu sunīti sauc " + d1.name + ", modelis ir " + d1.kind + ", bet vecums ir " + str(d1.age) + " gadi.")
print("Mana otrā suņuka marka ir " + d2.kind + ", un to vienkārši sauc - " + d2.name)
print(d1.speak("Wau"))