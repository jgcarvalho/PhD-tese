

PATH='/home/jgcarvalho/zeca-results-analysis/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba/rose_special_charged/run_10000/tmp/'
FILE='2ccqA'

c = 0
with open(PATH+FILE) as f:
    f.readline()
    ca = f.readlines()
    for i in ca:
        l = i[3:-4].split(' ')
        print('<tr>')
        for j in l:
            if j[0] == '*':
                print("<td class='h'>{}</td>".format(j[1]))
            elif j[0] == '|':
                print("<td class='e'>{}</td>".format(j[1]))
            elif j[0] == '_':
                print("<td class='c'>{}</td>".format(j[1]))
            else:
                print("<td class='r'>{}</td>".format(j[0]))

        print('</tr>')
        c += 1
        if c > 5:
            break
        