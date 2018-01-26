

PATH='/home/jgcarvalho/zeca-results-analysis/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba/rose_special_charged/run_10000/tmp/'
FILE='2ccqA'

header = """
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    font-family: "Courier New";
}
th, td {
    padding: 0px;
    text-align: center;    
}
.h {
	background: red;
}
.e {
	background: yellow;
}
.c {
	background: green;
}
.r {
	font-weight: bold;
}
.
</style>
</head>
<body>

<table>
"""

footer = """
</table>
</body>
</html>
"""
print(header)
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
        if c > 15:
            break
print(footer)