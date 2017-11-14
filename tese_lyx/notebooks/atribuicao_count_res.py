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

def pattern(dict_count_res, r_seq, r_dssp, r_stride, r_kaksi, r_pross, r_all3):
    p = [r_seq, r_dssp, r_stride, r_pross, r_kaksi, r_all3]
    if p[1:4].count('?') == 3:
        dict_count_res["not_vis"] += 1
    elif p[1:4].count('?') > 0 and  p[1:4].count('?') < 3:
        dict_count_res["error"] += 1
    elif p[1:5] == ['H','H','H','H']:
        dict_count_res['H'] += 1
    elif p[1:5] == ['E','E','E','E']:
        dict_count_res['E'] += 1
    elif p[1:5] == ['C','C','C','C']:
        dict_count_res['C'] += 1
    else:
        dict_count_res['?'] += 1

def count_pattern(fn, count_res):
    seq = _read_seq(fn)
    dssp = _read_dssp(fn)
    stride = _read_stride(fn)
    kaksi = _read_kaksi(fn)
    pross = _read_pross(fn)
    all3 = _read_all3(fn)

    for i in range(len(seq)):
        pattern(count_res,seq[i], dssp[i], stride[i],kaksi[i],pross[i],all3[i])

def plot_bar(tipo):
    x = np.array(list(tipo.keys()))
    plt.figure(1)
    plt.subplot()
    sns.barplot(x, list(tipo.values()), palette="muted")
    # plt.xticks(x, labels)
    plt.savefig("atribuicao_count_res.svg")
    plt.show()

def main():
    count_res = {"H":0, "E":0, "C":0, "?":0, "not_vis":0, "error":0}
    for i in glob(DATA_PATH+'/all3/*'):
        fn = basename(i)
        count_pattern(fn, count_res)
        # break
    print(count_res)
    total=0
    for c in count_res.values():
        total += c 
    
    count_res_frac = {k: count_res[k]/(total-count_res['not_vis']) for k in count_res.keys()}
    print(count_res_frac)
    print(total)
    # plot_bar(count_res_frac)


if __name__ == '__main__':
    main()