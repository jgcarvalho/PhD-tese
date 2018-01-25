from glob import glob
from os.path import basename
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# DATA_PATH="/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba_times_mcc/rose_special_charged/run_10000"
DATA_PATH = "/home/jgcarvalho/zeca-results-analysis/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba/rose_special_charged/run_10000/outres"

def count_len_ss(fn, len_ss):
    with open(fn) as f:
        f.readline()
        res = f.readlines()

    init = 0
    for i in range(1, len(res)):
        if res[i-1][2] != res[i][2] and res[i-1][2] != '?':
            len_ss[res[i-1][2]].append(i-init)
            init = i
            # print('*')
        # print(res[i][2])
    # for i in range(1, len(ss)):
    #     if ss[i-1] != ss[i]:
    #         len_ss[ss[i-1]].append(i - init)
    #         init = i



def plot(len_model_hk):
    m = ['H','E','C']
    x = np.array(list(m))
    plt.figure(1)
    plt.subplot()
    sns.boxplot(data=[np.array(len_model_hk['H']),np.array(len_model_hk['E']),np.array(len_model_hk['C'])], palette="muted", showfliers=False)
    plt.ylim(ymin=0, ymax=15)
    # plt.xticks(x, labels)
    # plt.savefig("model_hk_len_ss.svg")
    plt.show()

def main():
    len_psipred = {'H':[], 'E':[], 'C':[]}

    for fn in glob(DATA_PATH+"/*"):
        # print(fn)
        count_len_ss(fn, len_psipred)
        # break
    print(len_psipred)
    plot(len_psipred)


if __name__ == '__main__':
    main()