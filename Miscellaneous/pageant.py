import operator

#set up
r = open("pageantin.txt", "r")
w = open("pageantout.txt", "w")
nm = r.readline().split()
N, M = int(nm[0]), int(nm[1])
pattern = [[0 for x in range(M)] for y in range(N)]
for i in range(M):
   one_line = r.readline().strip()
   for j in range(len(one_line)):
       pattern[i][j] = one_line[j]

#functions
def find_spots(c_loc, pattern,spots_list):
    x = c_loc[0]
    y = c_loc[1]
    is_visited[x][y] = True
    if pattern[x][y] == "X":
        spots_list.append((x,y))
        if x+1 < N and not is_visited[x+1][y]:
            find_spots((x+1,y),pattern,spots_list)
        if y-1 > 0 and not is_visited[x][y-1]:
            find_spots((x,y-1),pattern,spots_list)
        if y+1 < M and not is_visited[x][y+1]:
            find_spots((x,y+1),pattern,spots_list)
        if x-1 > 0 and not is_visited[x-1][y]:
            find_spots((x-1,y),pattern,spots_list)

def find_boundaries(spots_list,boundaries):
    for i in spots_list:
        x = i[0]
        y = i[1]
        if not (x+1, y) in spots_list:
            boundaries.append((x,y))
        elif not (x-1, y) in spots_list:
            boundaries.append((x,y))
        elif not (x, y-1) in spots_list:
            boundaries.append((x,y))
        elif not (x, y+1) in spots_list:
            boundaries.append((x,y))


def compute_min_distances(list1, list2):
    minDist = float("inf")
    x1, y1, x2, y2 = -1, -1, -1, -1
    for i in list1:
        xi = i[0]
        yi = i[1]
        for j in list2:
            xj = j[0]
            yj = j[1]
            distance = abs(xi - xj) + abs(yi - yj)
            if distance < minDist:
                minDist = distance
                x1, y1, x2, y2 = xi, yi, xj, yj

    return [minDist, (x1, y1), (x2, y2)]

def compute_min_distances3(pattern, boundaries, spots, length, width):
    for i in length:
        for j in width:
            if (i,j) not in spots:
                trace_path((i,j),pattern,boundaries, length, width,0)


# def trace_path(tup,pattern,boundaries,length,width,distance):
#     x = tup[0]
#     y = tup[1]
#     if tup 



#initialize
is_visited = [[False for x in range(M)] for y in range(N)]
spots_list = [[],[],[]]
boundaries = [[],[],[]]


#finding the spots
count = 0
for i in range(N):
    for j in range(M):
        if pattern[i][j] == "X" and not is_visited[i][j]:
            find_spots((i,j),pattern,spots_list[count])
            count += 1

#find boundaries
for i in range(3):
    find_boundaries(spots_list[i], boundaries[i])


#minimize distances and compute answer
minlist1 = compute_min_distances(boundaries[0], boundaries[1])
minlist2 = compute_min_distances(boundaries[0], boundaries[2])
minlist3 = compute_min_distances(boundaries[1],boundaries[2])

min1 = minlist1[0] - 1
min2 = minlist2[0] - 1
min3 = minlist3[0] - 1

answer = 0
if min1 < min2:
    if min2 < min3:
        answer = min1 + min2
        points = minlist1[1:3]
    else:
        answer = min1 + min3
        points = minlist2[1:3]

else:
    if min3 < min1:
        answer = min2 + min3
        points = minlist3[1:3]
    else:
        answer = min1 + min2
        points = minlist1[1:3]





#submit
w.write(str(answer))
