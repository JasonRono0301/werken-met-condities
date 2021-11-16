
vraag = input('Bent u een man of een vrouw') #Input waarbij de gebruiker het geslacht kan intypen
antwoord = 'man' or 'vrouw' #Een variabele waarin het anwtoord moet voldoen.

if vraag == antwoord:
    ervaring = int(input('Hoelang heeft u ervaring met jongleren'))
    
    if ervaring > 4:
        ervaring = True
    else:
        ervaring = False
        
    diploma = input('Bent u in bezit van een diploma MBO-4 ondernemen?')
    if diploma == 'ja':
        diploma = True
    else:
        diploma = False
        
    rijbewijs = input('Bent u in bezit van een geldig vrachtwagen rijbewijs?')
    if rijbewijs == 'ja':
        rijbewijs = True
    else:
        rijbewijs = False
        
    snor = int(input('Hoe breed is uw snor?'))
    if snor > 10:
        snor = True
    else:
        snor = False
        
    lengte = int(input('Wat is uw lengte?'))
    if lengte > 150:
        lengte = True
    else:
        lengte = False
        
    gewicht = int(input('Wat is uw gewicht?'))
    if gewicht > 90:
        gewicht = True
    else:
        gewicht = False

    certificaat = input('Heeft u een Certificaat met Overleven met gevaarlijk personeel')
    if certificaat == 'ja':
        certificaat = True
    else:
        certificaat = False

    playstation = input('Bent u in bezit van een Playstation?') #Eigen vraag 1.
    if playstation == 'ja':
        playstaion = True
    else:
        playstation = False

    gamingtime = int(input('Hoeveel jaar gamet u al?')) #Eigen vraag 2.
    if gamingtime > 10:
        gamingtime = True
    else:
        gamingtime = False:

#Hieronder word de sollicitatie beoordeeld. 
aangenomen = ervaring and diploma and rijbewijs and snor and lengte and certificaat and playstation and gamingtime

if aangenomen:
    print('Welkom u bent aangenomen.')
else:
    print('Jammer u bent niet aangenomen.')
        
    





