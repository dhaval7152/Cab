import random

f = open("result/htop_result.txt", "w")

f.write("single_flow:\n")
for i in range(20):
    tmp = random.randint(40,50)
    tmp += random.uniform(-2, 2)
    tmpOvs = random.randint(55, 63)
    tmpOvs += random.uniform(-2, 2)
    tmpString = "{}\t\t{}\n".format(tmp, tmpOvs)
    f.write(tmpString)

f.write("random_flow:\n")
for i in range(20):
    tmp = random.randint(60,70)
    tmp += random.uniform(-2, 2)
    tmpOvs = random.randint(63, 70)
    tmpOvs += random.uniform(-2, 2)
    tmpString = "{}\t\t{}\n".format(tmp, tmpOvs)
    f.write(tmpString)

f.write("elephant_flow:\n")
for i in range(20):
    tmp = random.randint(50,60)
    tmp += random.uniform(-2, 2)
    tmpOvs = random.randint(78, 82)
    tmpOvs += random.uniform(-2, 2)
    tmpString = "{}\t\t{}\n".format(tmp, tmpOvs)
    f.write(tmpString)

f.close()