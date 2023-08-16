"""
bulls_cows.py: druhý projekt do Engeto Online Python Akademie
author: Zuzana Soudná
email: zuza.soudna@gmail.com
discord: Zuzana S.#3996
"""

import random

#pomocne promenne
odrazka = "-"
pocet_znaku = 45
delka_retezce_odrazek = odrazka * pocet_znaku

#uvodni text hry
print(
    """
    Hi there!
    """,
    delka_retezce_odrazek,
    """
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.
    """,
    delka_retezce_odrazek,
    """
    Enter a number:
    """,
    delka_retezce_odrazek
    )

#funkce generujici nahodne cislo, ktere musi hrac uhodnout
def vygeneruj_nahodne_cislo() -> str: 
    vygenerovane_cislo = []
    zasobnik_cislic = [0,1,2,3,4,5,6,7,8,9]

    index = 0

    while index < 4:
        nahodne_cislo = random.choice(zasobnik_cislic)
        vygenerovane_cislo.append(nahodne_cislo)
        if vygenerovane_cislo[0] == 0:
            vygenerovane_cislo.remove(0)
        else:
            zasobnik_cislic.remove(nahodne_cislo)
            index = index + 1

    vygenerovane_cislo_spravny_format = ''.join(str(item) for item in vygenerovane_cislo)
    return vygenerovane_cislo_spravny_format


zadani = vygeneruj_nahodne_cislo()


#funkce pro overeni duplicity cislice v hracem zadanem cisle
def najdi_duplicitu(string):
    slovnik = dict()
    for znak in string:
        if znak not in slovnik:
            slovnik[znak] = +1
        else:
            slovnik_pomocny = dict()
            slovnik_pomocny[znak] = int(slovnik.get(znak)) + 1
            slovnik.update(slovnik_pomocny)
    
    pocet_duplicit = 0
    for cislo in range(2,9):
        if cislo in slovnik.values():
            pocet_duplicit = pocet_duplicit + 1  
    return pocet_duplicit


#funkce overujici, ze hrac si tipnul cislo povoleneho formatu
number_of_guesses = 0
def over_hracem_zadane_cislo():
    if len(cislo_hrace) != 4:
        print("The entered number has wrong number of digits (", len(cislo_hrace), ").")
    elif not cislo_hrace.isdigit():
        print("Entered at least one character which is not a digit.")
    elif int(cislo_hrace[0]) == 0:
        print("Entered number starting with a zero.")    
    elif najdi_duplicitu(cislo_hrace) != 0 :
        print("Entered number contains multiple identical digits ")
    else:
        global number_of_guesses
        number_of_guesses += 1
        return True
    

#funkce vyhodnucujici cislo tipnute hracem
byk = 0
def vyhodnot_cislo_hrace(odhad, reseni):
    i=0
    cow = 0
    bull = 0
    for znak in odhad:
        if znak in reseni:
            if odhad[i] == reseni[i]:
                bull += 1
                global byk
                byk += 1
            else:
                cow +=1
        i +=1
    
    if bull != 4:
        if bull == 1:
            bull_koncovka = "bull"
        else:
            bull_koncovka = "bulls"
        if cow == 1:
            cow_koncovka = "cow"
        else:
            cow_koncovka = "cows"
        print(bull, bull_koncovka, ", ", cow, cow_koncovka)
        print(delka_retezce_odrazek)
   
    elif bull == 4:
        print("Correct, you've guessed the right number in ", number_of_guesses , "guesses!")
        

#funkce tela programu
def main():
    #print(zadani) #vytiskne nahodne vygenerovane cislo pro snazsi overeni funkcnosti programu
    while byk != 4:
        global cislo_hrace
        cislo_hrace = input(">>> ", )
        while type(over_hracem_zadane_cislo()) != bool:  
            cislo_hrace = input(">>> ", ) 
        vyhodnot_cislo_hrace(cislo_hrace, zadani)
        if cislo_hrace == zadani:
            break


#spusteni programu
main()
