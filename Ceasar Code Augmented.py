minuscules = "abcdefghijklmnopqrstuvwxyz"
minuscules = list(minuscules)
len_min = len(minuscules)

majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
majuscules = list(majuscules)
len_maj = len(majuscules)

autres_chara = ",.;'!?-()* "
autres_chara = list(autres_chara)
len_a_c = len(autres_chara)

phrase_base = input("Choisir votre message à cripter : ").split()
len_p_b = len(phrase_base)

liste_fini = []


# debut de la boucle :
for i in range(len_p_b):
    decal = len(phrase_base[i])
    if not i % 2 == 0:
        decal = -abs(decal)
    mot_de_i = list(phrase_base[i])
    len_m_de_i = len(mot_de_i)


    def decal_lettres_min(mot_phrase, decalage):  # decale les lettres minuscules
        def creat_dico(minuscules, decal):
            dico = {}
            for i in range(len_min):
                if i + decal >= len_min:
                    dico[minuscules[i]] = minuscules[i + decal - len_min]
                else:
                    dico[minuscules[i]] = minuscules[i + decal]
            return dico

        dico = creat_dico(mot_phrase, decalage)

        def codage(texte, dico):
            texte_code = []
            for lettre in texte:
                if not (lettre in dico):
                    texte_code.append(lettre)
                else:
                    texte_code.append(dico[lettre])
            return texte_code

        mot_code = codage(mot_phrase, dico)

        # mot_code=''.join(mot_code)

        return mot_code

    
    
    def decal_lettres_maj(mot_phrase, decalage):  # decale les lettres majuscules
        def creat_dico(majuscules, decal):
            dico = {}
            for i in range(len_min):
                if i + decal >= len_min:
                    dico[majuscules[i]] = majuscules[i + decal - len_min]
                else:
                    dico[majuscules[i]] = majuscules[i + decal]
            return dico

        dico = creat_dico(mot_phrase, decalage)

        def codage(texte, dico):
            texte_code = []
            for lettre in texte:
                if not (lettre in dico):
                    texte_code.append(lettre)
                else:
                    texte_code.append(dico[lettre])
            return texte_code

        mot_code = codage(mot_phrase, dico)

        # mot_code=''.join(mot_code)

        return mot_code


    decalelettres_min = decal_lettres_min(minuscules, decal)
    decalelettres_maj = decal_lettres_min(majuscules, decal)

    dico1 = {x: decalelettres_min[x] for x in range(len_min)}  # dict des lettres alphabetiques minuscules decalee
    dico2 = {x: minuscules[x] for x in range(len_min)}  # dict des lettres alphabetiques minuscules

    dico3 = {x: decalelettres_maj[x] for x in range(len_maj)}  # dict des lettres alphabetiques majuscules decalee
    dico4 = {x: majuscules[x] for x in range(len_maj)}  # dict des lettres alphabetiques majuscules

    dico5 = {x: mot_de_i[x] for x in range(len_m_de_i)}  # dict des caracteres speciaux
    dico6 = {x: autres_chara[x] for x in range(len_a_c)}

    resultat = []


    def transposition(phrase_voulu):
        for i in range(len_m_de_i):
            for y in range(len_min):
                if phrase_voulu[i] == dico2[y]:
                    resultat.insert(i, dico1[y])
                elif phrase_voulu[i] == dico4[y]:
                    resultat.insert(i, dico3[y])
            for w in range(len_a_c):
                if phrase_voulu[i] == dico6[w]:
                    resultat.insert(i, dico6[w])
        return resultat


    fin = transposition(dico5)

    fin = ''.join(resultat)
    if not i % 2 == 0:
        liste_fini.insert(i, str(decal) + fin)
    else:
        liste_fini.insert(i, fin + str(decal))

liste_fini = ' '.join(liste_fini)
print("Le resultat est :", liste_fini)
