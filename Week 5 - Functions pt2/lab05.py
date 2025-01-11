# takes date from another file
# prints it into the current file line by line

data_obj = open("data.txt")
data_obj_out = open("out.txt", "w")

count = 0

h_sum = 0
w_sum = 0
b_sum = 0

h_max = 0
w_max = 0
bmi_max = 0

h_min = 10 ** 6
w_min = 10 ** 6
bmi_min = 10 ** 6

print("{:<36s}{:<12s}".format(data_obj.readline().strip(),'BMI'))
for line in data_obj:
    

    name = line[0:12]
    height = float(line[12:24])
    weight = float(line[24:36])
    bmi = weight/height ** 2

    h_sum += height
    w_sum += weight
    b_sum += bmi

    if h_max < height:
        h_max = height
    if w_max < weight:
        w_max = weight
    if bmi_max < bmi:
        bmi_max = bmi

    if h_min > height:
        h_min = height
    if w_min > weight:
        w_min = weight
    if bmi_min > bmi:
        bmi_min = bmi


    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(name, height, weight, bmi))
    count += 1 
print('')

h_avrg = h_sum/8
w_avrg = w_sum/8
b_avrg = b_sum/8

print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Average', h_avrg, w_avrg, b_avrg))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Max', h_max, w_max, bmi_max))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Min', h_min, w_min, bmi_min))
data_obj_out.close()