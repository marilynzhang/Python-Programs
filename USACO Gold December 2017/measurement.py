f = open("measurement.in", "r")
w = open("measurement.out", "w")
ng = f.readline().split(" ")
n = int(ng[0])
g = int(ng[1])

cows_list = []

for i in range(n):
    cow = f.readline().rstrip()
    cows_list.append(cow)

cows_list = sorted(cows_list, key=lambda single_cow: int(single_cow[0])) #sort by date

cows_dict = dict()
cows_ids = [cow[0] for cow in cows_list]

for id in cows_ids:
    cows_dict[int(id)] = int(g)

maximum = int(g)
changes = int(0)



for triple in cows_list:
    triple = triple.split(" ")
    cowID = int(triple[1])
    change = int(triple[2])

    if cowID in cows_dict:
        oldValue = int(cows_dict[cowID])
    else:
        oldValue = int(g)

    newValue = int(oldValue + change)
    cows_dict[cowID] = int(newValue)

    if newValue == maximum and oldValue != maximum:
        changes +=1
    elif newValue > maximum and oldValue != maximum:
        maximum = newValue
        changes +=1
    elif newValue > maximum and oldValue == maximum:
        if sum(1 for maximum in cows_dict.values()) >= 1 or maximum == g:
            changes +=1
        maximum = newValue
    elif newValue < maximum and oldValue == maximum:
        if maximum > g:
            if sum(1 for maximum in cows_dict.values()) == 0:
                maxi = int(max(cows_dict.values()))
                numMax = int(sum(1 for maxi in cows_dict.values()))
                if maxi > g:
                    if numMax != 1 or maxi != newValue:
                        changes +=1
                    maximum = maxi
                else:
                    maximum = g
                    changes +=1

            else:
                changes +=1
        else:
            changes +=1

w.write(str(changes))
w.close()
