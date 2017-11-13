from glob import glob 
from os.path import basename
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

DATA_PATH="/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba_times_mcc/rose_special_charged/run_10000"

def count_n_ss(fn, m, n):
    with open(DATA_PATH+"/transitions_"+m+'/'+fn) as f:
        f.readline()
        s = f.readline()
        for k in n.keys():
            n[k] += s.count(k)
            # print(k, s.count(k))

def plot_bar(n_dssp, n_stride, n_kaksi, n_pross):
    x = np.array(list(n_dssp.keys()))
    plt.figure(1)
    plt.subplot(221)
    g = sns.barplot(x, list(n_dssp.values()), palette="muted")
    g.set_ylim(0, 150000)
    # g=sns.barplot(x='day',y='tip',data=groupedvalues, palette=np.array(pal[::-1])[rank])
    for i in range(len(list(n_dssp.values()))):
        g.text(i,list(n_dssp.values())[i], list(n_dssp.values())[i], color='black', ha="center")

    plt.subplot(222)
    g = sns.barplot(x, list(n_stride.values()), palette="muted")
    g.set_ylim(0, 150000)
    for i in range(len(list(n_stride.values()))):
        g.text(i,list(n_stride.values())[i], list(n_stride.values())[i], color='black', ha="center")

    plt.subplot(223)
    g = sns.barplot(x, list(n_kaksi.values()), palette="muted")
    g.set_ylim(0, 150000)
    for i in range(len(list(n_kaksi.values()))):
        g.text(i,list(n_kaksi.values())[i], list(n_kaksi.values())[i], color='black', ha="center")

    plt.subplot(224)
    g = sns.barplot(x, list(n_pross.values()), palette="muted")
    g.set_ylim(0, 150000)
    for i in range(len(list(n_pross.values()))):
        g.text(i,list(n_pross.values())[i], list(n_pross.values())[i], color='black', ha="center")
    # plt.xticks(x, labels)
    plt.savefig("atribuicao_n_ss.svg")
    plt.show()
        
def main():
    n_dssp = {'H':0, 'E':0, 'C':0}
    n_stride = {'H':0, 'E':0, 'C':0}
    n_kaksi = {'H':0, 'E':0, 'C':0}
    n_pross = {'H':0, 'E':0, 'C':0}

    for i in glob(DATA_PATH+'/all3/*'):
        fn = basename(i)
        # print(fn)
        count_n_ss(fn, 'dssp', n_dssp)
        count_n_ss(fn, 'stride', n_stride)
        count_n_ss(fn, 'kaksi', n_kaksi)
        count_n_ss(fn, 'pross', n_pross)

        

    print("DSSP", n_dssp)
    print("STRIDE", n_stride)
    print("KAKSI", n_kaksi)
    print("PROSS", n_pross)
    plot_bar(n_dssp, n_stride, n_kaksi, n_pross)

if __name__ == '__main__':
    main()