takimlar = ["galatasaray", "fenerbahce", "besiktas", "trabzonspor"]

for i in range(len(takimlar)):
    for j in range(len(takimlar)):
        if i != j:
            print(takimlar[i], "-", takimlar[j])
