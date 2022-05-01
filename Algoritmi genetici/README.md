# Algoritmi_Avansati
  1. ### Algoritmi genetici 
     Algoritm genetic care calculeaza maximul unei functii pe un interval dat (f : [st, dr] -> R+).
     - Generarea initiala a populatiei
     - Etapa de selectie (indivizilor li se asociaza o probabilitate direct proportionala cu fitness-ul lor, iar apoi se selecteaza indivizi conform probabilitatilor)
     - Etapa de incrucisare (crossing-over, 2 indivizii de la etapa de seletie se combina, pentru a genera in locul lor 2 noi indivizi)
     - Etapa de mutatie (pentru indivizii de la incrucisare, fiecare gena are sansa de a se schimba (bitul respectiv se neaga), astfel generandu-se material genetic nou)
     - Criteriul elitist (individul cu fitness-ul maxim trece automat in etapa urmatoare, pentru a se garanta ca valoarea functiei va fi crescatoare)
