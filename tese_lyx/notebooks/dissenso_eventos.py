from glob import glob
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

DATA_PATH="/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba_times_mcc/rose_special_charged/run_10000"

def count(fn, tr):
    with open(fn) as f:
        f.readline()
        s = f.readline()
    
    for i in range(1,len(s)-1):
        if s[i] == '?':
            tr[s[i-1]+s[i]+s[i+1]] += 1
            # print(s[i-1], s[i],s[i+1])
    # if s[0] == '?':
    #     tr['inicio'] += 1
    # if s[len(s)-1] == '?':
    #     tr['fim'] += 1

def plot_bar(tipo):
    x = np.array(list(tipo.keys()))
    plt.figure(1)
    plt.subplot()
    sns.barplot(x, list(tipo.values()), palette="muted")
    # plt.xticks(x, labels)
    plt.savefig("dissenso_eventos.svg")
    plt.show()

def main():
    tr = {'H?H':0, 'C?C':0, 'E?E':0, 'C?H':0, 'H?C':0, 'C?E':0, 'E?C':0, 'E?H':0,'H?E':0}
    tr_dssp = {'H?H':0, 'C?C':0, 'E?E':0, 'C?H':0, 'H?C':0, 'C?E':0, 'E?C':0, 'E?H':0,'H?E':0}
    tr_stride = {'H?H':0, 'C?C':0, 'E?E':0, 'C?H':0, 'H?C':0, 'C?E':0, 'E?C':0, 'E?H':0,'H?E':0}
    tr_pross = {'H?H':0, 'C?C':0, 'E?E':0, 'C?H':0, 'H?C':0, 'C?E':0, 'E?C':0, 'E?H':0,'H?E':0}
    for fn in glob(DATA_PATH+'/transitions_all3/*'):
        count(fn, tr)
    for fn in glob(DATA_PATH+'/transitions_dssp/*'):
        count(fn, tr_dssp)
    for fn in glob(DATA_PATH+'/transitions_stride/*'):
        count(fn, tr_stride)
    for fn in glob(DATA_PATH+'/transitions_pross/*'):
        count(fn, tr_pross)

    print(tr)
    print(tr_dssp)
    print(tr_stride)
    print(tr_pross)
    # plot_bar(tr)

if __name__ == '__main__':
    main()