import matplotlib.pyplot as plt
import time

grid_size = 10
grid = []
start_point = (1,0)
end_point = (5,9)
obs_list = [(3,2), (3,3), (3,4), (3,1), (2,4), (1,4), (0,4)]

#funcions
def calc_distance(node_a, node_b): #node(x, y)
    
    x_d = abs(node_a[0] - node_b[0])
    y_d = abs(node_a[1] - node_b[1])
    
    delta_diff = abs(x_d - y_d)
    cost = 10 * delta_diff + 14 * (max(x_d, y_d) - delta_diff)
    
    return cost


def calc_successors(node, start_point, end_point, open_list):
    ans = []
    for x in range(node[0] - 1, node[0] + 2, 1):
        for y in range(node[1] - 1, node[1] + 2, 1):
           # print(f'scaning points {x} {y}')
            if x > grid_size - 1 or y > grid_size - 1 or x < 0 or y < 0:
                pass
            else:
                if (x, y) in open_list:
                    g = calc_distance((x, y), start_point)
                    h = calc_distance((x, y), end_point)
                    f = g + h 
                    #print(f'{x} {y}, cost_f = {f}')
                    ans.append((x,y,f,h))
                else:
                   # print(f'no here {x} {y}')
                   pass
       
    
    return ans #x, y, f-cost, cost to end point

#inital 
for row in range(0, grid_size):
        grid.append([0 for el in range(0, grid_size)])


grid[start_point[0]][start_point[1]] = 'S'
grid[end_point[0]][end_point[1]] = 'E'

#create open and closed list
open_list = [(x,y) for x in range(0, grid_size) for y in range(0, grid_size) if (x,y) not in obs_list]
close_list = []

q = start_point
#main loop
while len(open_list) > 0:
    local_q = (q[0],q[1])


    if local_q in open_list:
        open_list.remove(local_q)


    new_q_list = calc_successors(local_q, start_point, end_point, open_list) 
    #print(new_q_list)
    try:
        q = new_q_list[0]

        
        for el in new_q_list:
            if el[2] < q[2]:
                q = el
            if el[2] == q[2]:
                if el[3] < q[3]:
                    q = el
        close_list.append(local_q)
        if local_q == end_point:
            break
        #time.sleep(0.2)

    except IndexError:
        print("no way")
        
        
        
    print(calc_successors(local_q, start_point, end_point, close_list))  
    print(calc_successors(local_q, start_point, end_point, open_list)) 
    

print(q)


#visualizattion
for point in close_list:
    grid[point[0]][point[1]] = '1'
    
for obs in obs_list:
    grid[obs[0]][obs[1]] = '#'

#vistualization
for row in grid:
    for col in row:
        print(col, end = ' ')
    print('')
    
