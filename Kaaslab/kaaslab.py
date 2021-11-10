kaas = input('Is de kaas geel?')

if kaas == "ja":
    kaas = input('Zitten er gaten in?')
    if kaas == "ja":
        kaas = input('Is de kaas de kaas belachelijk duur?')
        if kaas == "nee":
            print('Jij bent de leerdammer')
        elif kaas == "ja":
            print('Jij bent de Emmenthaler')
    elif kaas == "nee":
        kaas = input('Is de kaas hard als steen?')
        if kaas == "ja":
            print('Jij bent de Pamigiano Reggiano')
        elif kaas == "nee":
            print('Jij bent de Goudse kaas')
elif kaas == "nee":
    kaas = input('Heeft de kaas blauwe schimmels?')
    if kaas == "ja":
        kaas = input('Heeft de kaas een korst?')
        if kaas == "ja":
            print('Jij bent de Bleu de Rochbaron')
        elif kaas == "nee":
            print('Jij bent de Foume d,Ambert')
    elif kaas == "nee":
        kaas = input('Heeft de kaas een korst?')
        if kaas == "ja":
            print('Jij bent de Camembert')
        elif kaas == "nee":
            print('Jij bent de Mozzarella')
    
