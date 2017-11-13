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

def _read_all3(fn):
    with open(DATA_PATH+"/all3/"+fn) as f:
        f.readline()
        return f.readline()

def count(fn, c_aa, c_dissenso):
    seq = _read_seq(fn)
    dssp = _read_dssp(fn)
    all3 = _read_all3(fn)

    for i in range(len(seq)):
        # remove os residuos não anotados pelo dssp (não observado no cristal)
        if dssp[i] != '?':
            c_aa[seq[i]] += 1
            if dssp[i] != all3[i]:
                c_dissenso[seq[i]] += 1

def plot_bar(fractions, aa):
    x = np.array(list(aa))
    plt.figure(1)
    plt.subplot()
    sns.barplot(x, fractions, palette="muted")
    # plt.xticks(x, labels)
    plt.savefig("dissenso_aminoacido.svg")
    plt.show()

def main():
    aa = "ACDEFGHIKLMNPQRSTVWY"
    c_aa = {k: 0 for k in aa}
    c_dissenso = {k: 0 for k in aa}
    
    
    for i in glob(DATA_PATH+'/all3/*'):
        fn = basename(i)
        count(fn, c_aa, c_dissenso)


    print(c_aa)
    print(c_dissenso)

    fractions = [c_dissenso[k]/c_aa[k] for k in aa]
    labels = [k for k in aa]
 

    plot_bar(fractions, aa)

    # 
    #     points.append(count_notcons_and_length(fn))

if __name__ == '__main__':
    main()