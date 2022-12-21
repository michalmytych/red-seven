# Klasy

- Reguła()
___
- Kolor(wartość, nazwa, reguła)
  - czy_mocniejszy_od(kolor): bool
___
- Karta(kolor, liczba)
  - czy_mocniejsza_od(karta): bool
___
- Gracz(karty[])
  - _paleta (Stos)_
  - _ręka (Lista)_
  - zagraj_karte_z_ręki_do_palety(karta)
  - zmień_regułę(karta)
  - zagraj_do_palety_i_zmień_regułę(karta_do_palety, karta_reguły)
___
- Gra()
  - _stos_dobierania (Stos)_
  - _tło (Stos)_
  - _aktywny_gracz (Gracz)_
  - rozdaj_po_7_kart()
  - rozdaj_po_1_odkrytej_karcie()
  - wyłóż_kartę_rozpoczynającą()
  - wybierz_gracza_rozpoczynającego(): gracz
  - następny_gracz()
  - sprawdz_czy_gracze_maja_karty()
  - sprawdz_ręce_graczy()

