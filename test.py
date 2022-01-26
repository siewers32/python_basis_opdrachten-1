
vraag_1 = "Wat is je voornaam\n"
vraag_2 = "Wat is je achternaam\n"
vraag_3 = "Wat neem je mee aan drank\n"
vraag_4 = "Wat neem je mee om te eten\n"

vn = input(vraag_1)
an = input(vraag_2)
d = input(vraag_3)
e = input(vraag_4)

my_dict = {"voornaam": vn, "achternaam": an, "drank": d, "eten": e}

fo = open('party.txt', 'wt')
fo.write("===================================\n")
for i in my_dict.keys():
      print(i + ":" + my_dict[i])
      fo.write(i + ":" + my_dict[i] + "\n")
fo.write("===================================\n\n")
fo.close()