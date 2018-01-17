from glob import glob
from os.path import basename
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# DATA_PATH="/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba_times_mcc/rose_special_charged/run_10000"
DATA_PATH = "/home/jgcarvalho/cnnss/pytorch/model_HK/results_32"

def count_len_ss(ss, len_ss):
    # with open(fn) as f:
    #     f.readline()
    #     ss = f.readline()

    init = 0
    for i in range(1, len(ss)):
        if ss[i-1] != ss[i]:
            len_ss[ss[i-1]].append(i - init)
            init = i

def q_count(pred_ss, true_ss, q_dict):
    n_h = 0.0
    t_h = 0.0
    n_e = 0.0
    t_e = 0.0
    n_c = 0.0
    t_c = 0.0
    for i in range(len(true_ss)):
        if true_ss[i] != '?':
            if true_ss[i] == 'H':
                n_h += 1.0
                if pred_ss[i] == 'H':
                    t_h += 1.0
            if true_ss[i] == 'E':
                n_e += 1.0
                if pred_ss[i] == 'E':
                    t_e += 1.0
            if true_ss[i] == 'C':
                n_c += 1.0
                if pred_ss[i] == 'C':
                    t_c += 1.0

    v = 0.0
    q3 = 0.0
    if n_h > 0:
        q_dict['QH'].append(t_h/n_h) 
        q3 += t_h/n_h
        v += 1.0
    if n_e > 0:
        q_dict['QE'].append(t_e/n_e) 
        q3 += t_e/n_e
        v += 1.0
    if n_c > 0:
        q_dict['QC'].append(t_c/n_c) 
        q3 += t_c/n_c
        v += 1.0

    q_dict['Q3'].append(q3/v) 


def plot(q):
    m = ['Q3','QH','QE','QC']
    x = np.array(list(m))
    plt.figure(1)
    plt.subplot()
    sns.boxplot(data=[np.array(q['Q3']),np.array(q['QH']),np.array(q['QE']),np.array(q['QC'])], palette="muted", showfliers=False)
    plt.ylim(ymin=0, ymax=1)
    # plt.xticks(x, m)
    plt.savefig("model_hk_32_q_ss.svg")
    plt.show()

def main():
    # len_model_hk = {'H':[], 'E':[], 'C':[]}]
    q_model_resnet = {'Q3':[], 'QH':[], 'QE':[], 'QC':[]}
    with open(DATA_PATH) as f:
        f.readline()
        lines = f.readlines()
        for i in range(0,len(lines),3):
            print(lines[i+1])
            # count_len_ss(lines[i+1], len_model_hk)
            q_count(lines[i+1],lines[i+2], q_model_resnet)
    print(q_model_resnet)
    plot(q_model_resnet)

   

if __name__ == '__main__':
    main()