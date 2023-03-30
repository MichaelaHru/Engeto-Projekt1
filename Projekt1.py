
#author = Michaela Hrušková
#email = michaela.siruckova@seznam.cz
#discord = Míša H.#9905



TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


users = ['bob','ann','mike','liz']
password = ['123','pass123','password123','pass123']
oddelovac = '-' * 50

uzivatel_heslo = dict(zip(users,password))
#print(uzivatel_heslo)

print(oddelovac)
name = input('Hello, what is your name?:')
password_vlozeni = input('Enter your password, please:')
print(oddelovac)

if not name in uzivatel_heslo or uzivatel_heslo[name] != password_vlozeni:
    print('Unregistered user, terminating the program..')
    quit()
else:
    print('Welcome,',name, 'you may continue.')
    print('We have 3 text to be analyzed.')
    print(oddelovac)

##########################################################################

slovnik_texty = dict(enumerate(TEXTS,start=1))

vyber_textu = input('Choose number of the text from 1 to 3:')
print(oddelovac)

if not vyber_textu.isdigit():
    print('You may choose only numbers')
else:
    vyber_textu = int(vyber_textu)
    if vyber_textu > 3:
        print('You can only choose a number between 1 and 3')
        quit()
    else:
        text = slovnik_texty.get(vyber_textu)
        for key, value in slovnik_texty.items():
            if key == vyber_textu:
                slovo = value.split()
                pocet_slov = len(slovo)
                print('There are',pocet_slov,'words in selected text.')
        
        pocet_velka = 0
        for slovo in slovnik_texty[vyber_textu].split():
            if slovo[0].isupper():
                pocet_velka = pocet_velka + 1
        print('There are',pocet_velka,'titlecase words.')

        jen_velka = 0
        for slovo in slovnik_texty[vyber_textu].split():
            if slovo.isupper() and slovo.isalpha():
                jen_velka = jen_velka + 1
        print('There are',jen_velka, 'uppercase words.')

        jen_mala = 0
        for slovo in slovnik_texty[vyber_textu].split():
            slovo = slovo.strip('.')
            if slovo.isalpha() and slovo.islower():              
                jen_mala = jen_mala + 1
        print('There are',jen_mala,'lowercase words.')

        pocet_cisel = 0
        for slovo in slovnik_texty[vyber_textu].split():
            if slovo.isdigit():
                pocet_cisel = pocet_cisel + 1
        print('There are',pocet_cisel,'numeric strings.')

        jen_cisla = []
        for slovo in slovnik_texty[vyber_textu].split():
            if slovo.isdigit():
                jen_cisla.append(int(slovo))
                soucet = sum(jen_cisla)

        print('The sum of all the numbers',soucet)

print(oddelovac)

########################################################################
nadpis_tabulky = ('LEN','OCCURENCES','NR.')
sirka = 21
odd = '|'
print(f"{nadpis_tabulky[0]}{odd}{nadpis_tabulky[1].center(sirka)}{odd}" \
      f"{nadpis_tabulky[2]}")
print(oddelovac)

###############################################################
delky_slov = {}
text = slovnik_texty.get(vyber_textu)
slova = text.split()

for slovo in slova:
    delka_slova = len(slovo)
    if delka_slova in delky_slov:
        delky_slov[delka_slova] = delky_slov[delka_slova] + 1
    else:
        delky_slov[delka_slova] = 1

for por_cislo,(delka, pocet) in enumerate(sorted(delky_slov.items())):
    hvezda = '*' * (pocet)
    print(f"{str(delka).rjust(3)}{odd}{hvezda.ljust(21)}{odd}" \
          f"{str(pocet).rjust(1)}")
   
   
   
   
   
   



    
    


        

        




        








