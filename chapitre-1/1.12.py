# Orif section informatique
#
# Exercice 1.12
# Calcul de salaire avec déductions
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
salaire = int(input("Quel est votre salaire brut : "))
salaireBrut = salaire
salaire1 = salaire * (1 - 0.042)
salaire2 = salaire * (1 - 0.07)
salaire3 = salaire * (1 - 0.025)
salaire4 = salaire * (1 - 0.01)
salaire5 = salaire * (1 - 0.013)
salaire6 = salaire * (1 - 0.013)
salaire7 = salaire * (1 - 0.07)
dd1 = salaireBrut - salaire1
dd2 = salaireBrut - salaire2
dd3 = salaireBrut - salaire3
dd4 = salaireBrut - salaire4
dd5 = salaireBrut - salaire5
dd6 = salaireBrut - salaire6
print(f"""Fiche de salaire de Nom, Travail, né le Date
-------------------------------------------------------------------
 
Salaire mensuel brut : {salaireBrut}
 
Déductions :
- AVS (4.2%)  : {dd1}
- AI (0.7%)   : {dd2}
- APG (0.25%) : {dd3}
- AC (1.0%)   : {dd4}
- ANP (1.3%)  : {dd5}
- LPP (7%)    : {dd6}
----------------------------------
Total des déductions : {dd1 + dd2 + dd3 + dd4 + dd5 + dd6}
----------------------------------
Salaire net          : {salaireBrut - (dd1 + dd2 + dd3 + dd4 + dd5 + dd6)}
==================================
Salaire net annuel   : {(salaireBrut - (dd1 + dd2 + dd3 + dd4 + dd5 + dd6)) * 12}""")