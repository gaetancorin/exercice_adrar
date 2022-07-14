global dico_grade_a, dico_grade_b, dico_grade_c

dico_grade_a = {}
dico_grade_b = {}
dico_grade_c = {}

dico_grade_a["id"] = 1
dico_grade_b["id"] = 2
dico_grade_c["id"] = 3

dico_grade_a["Nom formule"] = "Min"
dico_grade_b["Nom formule"] = "Sup"
dico_grade_c["Nom formule"] = "Max"

dico_grade_a["Max Emprunts"] = 3
dico_grade_b["Max Emprunts"] = 5
dico_grade_c["Max Emprunts"] = 10

dico_grade_a["Max Taille"] = 3
dico_grade_b["Max Taille"] = 4
dico_grade_c["Max Taille"] = 4

liste_des_formules = [dico_grade_a, dico_grade_b, dico_grade_c]

def defautGrade():
    return dico_grade_a

def voirGrades():
    print('\n')
    for i in liste_des_formules:
        print(f'----Grade {i["Nom formule"]} ----\nMax Emprunts : {i["Max Emprunts"]}\nTaille max de livre : {i["Max Taille"]}\n')
        print(f'Pour selectioner cette formule entrez : {i["id"]}\n\n')
