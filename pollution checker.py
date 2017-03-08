with open('pm10.csv', 'r') as f:
    x = f.readlines()
plik = open('dane.txt', 'w')
counter_krk = 0
sum_krk = 0
counter_slk = 0
sum_slk = 0
counter_ck = 0
sum_ck = 0
counter_troj = 0
sum_troj = 0
year = 2000

print("PM 10")
plik.writelines("PM 10")
for i in x:
    if float(i.split(';')[0]) == year + 1:
        print("\n")
        plik.write("\n")
        if counter_krk != 0:
            print("\nYear = " + str(year) + " Kraków " + str(sum_krk / counter_krk))
            plik.writelines("\nYear = " + str(year) + " Kraków " + str(sum_krk / counter_krk))
            counter_krk = 0
            sum_krk = 0
        if counter_slk != 0:
            print("Year = " + str(year) + " Katowice " + str(sum_slk / counter_slk))
            plik.writelines("\nYear = " + str(year) + " Katowice " + str(sum_slk / counter_slk))
            counter_slk = 0
            sum_slk = 0
        if counter_ck != 0:
            print("Year = " + str(year) + " Kielce " + str(sum_ck / counter_ck))
            plik.writelines("\nYear = " + str(year) + " Kielce " + str(sum_ck / counter_ck))
            counter_ck = 0
            sum_ck = 0
        if counter_troj != 0:
            print("Year = " + str(year) + " Trójmiasto " + str(sum_troj / counter_troj))
            plik.writelines("\nYear = " + str(year) + " Trójmiasto " + str(sum_troj / counter_troj))
            counter_troj = 0
            sum_troj = 0
        year = year + 1
    if float(i.split(';')[0]) == year and i.split(';')[3] == 'Aglomeracja Krakowska':
        counter_krk += 1
        sum_krk += float(i.split(';')[8].replace(",","."))
    if float(i.split(';')[0]) == year and i.split(';')[3] == 'Aglomeracja Górnośląska':
        counter_slk += 1
        sum_slk += float(i.split(';')[8].replace(",","."))
    if float(i.split(';')[0]) == year and i.split(';')[3] == 'miasto Kielce':
        counter_ck += 1
        sum_ck += float(i.split(';')[8].replace(",","."))
    if float(i.split(';')[0]) == year and i.split(';')[3] == 'Aglomeracja Trójmiejska':
        counter_troj += 1
        sum_troj += float(i.split(';')[8].replace(",","."))
f.close()


with open('pm2,5.csv', 'r') as f:
    x = f.readlines()
counter_krk = 0
sum_krk = 0
counter_slk = 0
sum_slk = 0
counter_ck = 0
sum_ck = 0
counter_troj = 0
sum_troj = 0
year = 2002
print("\n\n\nPM 2,5")
plik.writelines("\n\n\nPM 2,5")
for i in x:
    if float(i.split(';')[0]) == year + 1:
        year = year + 1
        print("\n")
        plik.write("\n")
        if counter_krk != 0:
            print("\nYear = " + str(year) + " Kraków " + str(sum_krk / counter_krk))
            plik.writelines("\nYear = " + str(year) + " Kraków " + str(sum_krk / counter_krk))
            counter_krk = 0
            sum_krk = 0
        if counter_slk != 0:
            print("Year = " + str(year) + " Katowice " + str(sum_slk / counter_slk))
            plik.writelines("\nYear = " + str(year) + " Katowice " + str(sum_slk / counter_slk))
            counter_slk = 0
            sum_slk = 0
        if counter_ck != 0:
            print("Year = " + str(year) + " Kielce " + str(sum_ck / counter_ck))
            plik.writelines("\nYear = " + str(year) + " Kielce " + str(sum_ck / counter_ck))
            counter_ck = 0
            sum_ck = 0
        if counter_troj != 0:
            print("Year = " + str(year) + " Trójmiasto " + str(sum_troj / counter_troj))
            plik.writelines("\nYear = " + str(year) + " Trójmiasto " + str(sum_troj / counter_troj))
            counter_troj = 0
            sum_troj = 0
    if float(i.split(';')[0]) == year and i.split(';')[3] == 'Aglomeracja Krakowska':
        counter_krk += 1
        sum_krk += float(i.split(';')[8].replace(",","."))
    if float(i.split(';')[0]) == year and i.split(';')[3] == 'Aglomeracja Górnośląska':
        counter_slk += 1
        sum_slk += float(i.split(';')[8].replace(",","."))
    if float(i.split(';')[0]) == year and i.split(';')[3] == 'miasto Kielce':
        counter_ck += 1
        sum_ck += float(i.split(';')[8].replace(",","."))
    if float(i.split(';')[0]) == year and i.split(';')[3] == 'Aglomeracja Trójmiejska':
        counter_troj += 1
        sum_troj += float(i.split(';')[8].replace(",","."))
f.close()
plik.close()
