import math
user_input = input("Anna suorakulmion kanta ja korkeus: ")
kanta, korkeus = map(float, user_input.split())
pintaala = kanta * korkeus
print(f"Suorakulmion pintaala on kanta {kanta} ja korkeus {korkeus} on: {pintaala}")