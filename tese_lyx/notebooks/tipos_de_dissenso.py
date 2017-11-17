from glob import glob
from os.path import basename
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

DATA_PATH="/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba_times_mcc/rose_special_charged/run_10000"

def _read_seq(fn):
    with open(DATA_PATH+"/seq/"+fn) as f:
        f.readline()
        return f.readline()

def _read_dssp(fn):
    with open(DATA_PATH+"/dssp/"+fn) as f:
        f.readline()
        return f.readline()

def _read_stride(fn):
    with open(DATA_PATH+"/stride/"+fn) as f:
        f.readline()
        return f.readline()

def _read_kaksi(fn):
    with open(DATA_PATH+"/kaksi/"+fn) as f:
        f.readline()
        return f.readline()

def _read_pross(fn):
    with open(DATA_PATH+"/pross/"+fn) as f:
        f.readline()
        return f.readline()

def _read_all3(fn):
    with open(DATA_PATH+"/all3/"+fn) as f:
        f.readline()
        return f.readline()

def qual_tipo(s):
    if 'H' in s and 'E' in s and 'C' in s:
        return "HEC"
    elif 'H' in s and 'E' in s:
        return "HE"
    elif 'H' in s and 'C' in s:
        return "HC"
    elif 'E' in s and 'C' in s:
        return "EC"
    else:
        print(s)

def count(fn, tipo):
    seq = _read_seq(fn)
    dssp = _read_dssp(fn)
    stride = _read_stride(fn)
    kaksi = _read_kaksi(fn)
    pross = _read_pross(fn)
    all3 = _read_all3(fn)

    for i in range(len(seq)):
        if dssp[i] != all3[i] and stride[i] != all3[i] and kaksi[i] != all3[i] and pross[i] != all3[i]:
            tipo["Total"] += 1
            t = qual_tipo(dssp[i]+stride[i]+kaksi[i]+pross[i])
            tipo[t] += 1

def plot_bar(tipo):
    x = np.array(list(tipo.keys()))
    plt.figure(1)
    plt.subplot()
    sns.barplot(x, list(tipo.values()), palette="muted")
    # plt.xticks(x, labels)
    plt.savefig("tipos_de_dissenso.svg")
    plt.show()

def main():
    tipo = {"HC":0, "HE":0, "EC":0, "HEC":0, "Total":0}

    for i in glob(DATA_PATH+'/all3/*'):
        fn = basename(i)
        count(fn, tipo)

    print(tipo)
    total = tipo.pop("Total")
    for k in tipo.keys():
        tipo[k] /= total
    print(tipo)
    # plot_bar(tipo)
    

if __name__ == '__main__':
    main()