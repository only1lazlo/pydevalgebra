#print("hello, world")
#ovo je komentar
from xml.sax.saxutils import prepare_input_source


ime = "Vatroslav"
prezime = "Veble"
god_rodjenja = 1991
drzava_rodjenja = "Hrvatska"
status_radnog_odnosa = "Zaposlen"
stranica_a = 25
stranica_b = 15
povrsina_cetverokuta = stranica_a * stranica_b

#print(ime,'\n', prezime,"\n", god_rodjenja, "\n", drzava_rodjednja,"\n", status_radnog_odnosa,"\n", stranica_a,"\n", stranica_b,"\n", povrsina_cetverokuta)

#print(ime, prezime, god_rodjenja,  drzava_rodjenja, status_radnog_odnosa, stranica_a, stranica_b, povrsina_cetverokuta, sep="\n")
"""
prezime_pa_ime = prezime + " " + ime + "\n" + str (god_rodjenja)
print(prezime_pa_ime)
"""

print("Ime i prezime:", ime, prezime, sep = " ")
print("Godina rođenja: ", god_rodjenja, ".", sep = "")
print("Zaposlen:", status_radnog_odnosa)