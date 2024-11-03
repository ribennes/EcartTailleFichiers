# fonction ecart type
def ecart_type(liste):
    n = len(liste)
    moy = sum(liste) / n
    somme = 0
    for i in liste:
        somme += (i - moy) ** 2
    return (somme / (n -1)) ** 0.5


# test
liste = [1, 2, 3, 4, 5]
print(ecart_type(liste))  # 1.5811388300841898
