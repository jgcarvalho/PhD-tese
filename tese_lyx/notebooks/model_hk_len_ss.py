from glob import glob
from os.path import basename
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# DATA_PATH="/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba_times_mcc/rose_special_charged/run_10000"
DATA_PATH = "/home/jgcarvalho/cnnss/pytorch/model_resnet/results_21_32"

def count_len_ss(ss, len_ss):
    # with open(fn) as f:
    #     f.readline()
    #     ss = f.readline()

    init = 0
    for i in range(1, len(ss)):
        if ss[i-1] != ss[i]:
            len_ss[ss[i-1]].append(i - init)
            init = i

def plot_H(len_dssp, len_stride, len_kaksi, len_pross):
    m = ['DSSP','STRIDE','KAKSI','PROSS']
    x = np.array(list(m))
    plt.figure(1)
    plt.subplot()
    sns.boxplot(data=[np.array(len_dssp['H']),np.array(len_stride['H']),np.array(len_kaksi['H']),np.array(len_pross['H'])], palette="muted", showfliers=False)
    plt.ylim(ymin=0)
    # plt.xticks(x, labels)
    plt.savefig("atribuicao_len_ss_H.svg")
    plt.show()

def plot_E(len_dssp, len_stride, len_kaksi, len_pross):
    m = ['DSSP','STRIDE','KAKSI','PROSS']
    x = np.array(list(m))
    plt.figure(1)
    plt.subplot()
    sns.boxplot(data=[np.array(len_dssp['E']),np.array(len_stride['E']),np.array(len_kaksi['E']),np.array(len_pross['E'])], palette="muted", showfliers=False)
    plt.ylim(ymin=0)
    # plt.xticks(x, labels)
    plt.savefig("atribuicao_len_ss_E.svg")
    plt.show()

def plot(len_model_hk):
    m = ['H','E','C']
    x = np.array(list(m))
    plt.figure(1)
    plt.subplot()
    sns.boxplot(data=[np.array(len_model_hk['H']),np.array(len_model_hk['E']),np.array(len_model_hk['C'])], palette="muted", showfliers=False)
    plt.ylim(ymin=0, ymax=31)
    # plt.xticks(x, m)
    plt.savefig("model_resnet_21_32_len_ss.svg")
    plt.show()

def main():
    len_model_hk = {'H':[], 'E':[], 'C':[]}
    with open(DATA_PATH) as f:
        f.readline()
        lines = f.readlines()
        for i in range(0,len(lines),3):
            print(lines[i+1])
            count_len_ss(lines[i+1], len_model_hk)
    print(len_model_hk)
    plot(len_model_hk)


     
    # len_dssp = {'H':[], 'E':[], 'C':[], '?':[]}
    # len_stride = {'H':[], 'E':[], 'C':[], '?':[]}
    # len_kaksi = {'H':[], 'E':[], 'C':[], '?':[]}
    # len_pross = {'H':[], 'E':[], 'C':[], '?':[]}
    # len_all3 = {'H':[], 'E':[], 'C':[], '?':[]}

    # for fn in glob(DATA_PATH+'/all3/*'):
    #     # print(fn)
    #     count_len_ss(fn, len_all3)
    # #     break
    # # print(len_all3)

    # for fn in glob(DATA_PATH+'/dssp/*'):
    #     # print(fn)
    #     count_len_ss(fn, len_dssp)
    # #     break
    # # print(len_dssp)

    # for fn in glob(DATA_PATH+'/stride/*'):
    #     # print(fn)
    #     count_len_ss(fn, len_stride)
    # #     break
    # # print(len_stride)

    # for fn in glob(DATA_PATH+'/kaksi/*'):
    #     # print(fn)
    #     count_len_ss(fn, len_kaksi)
    # #     break
    # # print(len_kaksi)

    # for fn in glob(DATA_PATH+'/pross/*'):
    #     # print(fn)
    #     count_len_ss(fn, len_pross)
    # #     break
    # # print(len_kaksi)

    # plot_E(len_dssp, len_stride, len_kaksi, len_pross)
    # plot_H(len_dssp, len_stride, len_kaksi, len_pross)
if __name__ == '__main__':
    main()