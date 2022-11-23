from random import choice, sample, shuffle
cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
} 

print(f"Los valores y sus cartas son las siguientes: {cartas}")



lista_de_cartas = list(cartas) 
carta1 = choice(list(cartas))
carta2 = choice(list(cartas))
puntuacion1 = cartas[carta1]
puntuacion2 = cartas[carta2]
score_jugador = puntuacion1 + puntuacion2
carta3 = choice(list(cartas))
carta4 = choice(list(cartas))
puntuacion3 = cartas[carta3]
puntuacion4 = cartas[carta4]
score_crupier = puntuacion3 + puntuacion4

print("Tus cartas son : {} y {}" .format(carta1[0], carta2[0]))

print("Cartas del crupier son : {} y {}" .format(carta3[0], carta4[0])) 


if score_jugador < score_crupier: 
    print(score_jugador, "<", score_crupier, "LA BANCA HA GANADO") 
elif score_jugador > score_crupier: 
    print(score_jugador, ">", score_crupier, "HAS GANADO") 
else: 
    print(score_jugador, "==", score_crupier, "NO TE QUITA EL MONEY") 

