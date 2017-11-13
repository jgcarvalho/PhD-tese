from glob import glob
from os.path import basename
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

DATA_PATH="/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba_times_mcc/rose_special_charged/run_10000"

def count_not_vis(fn):
    with open(DATA_PATH+"/dssp/"+basename(fn)) as f:
        f.readline()
        seq = f.readline()
        # print(seq.count('?'))
        return seq.count('?')


def count_notcons_and_length(fn):
    with open(fn) as f:
        f.readline()
        seq = f.readline()
        notcons = seq.count('?') - count_not_vis(fn)
        length = len(seq)
        # print(notcons/length)
        return [notcons, length, notcons/length]

def plot_scatter(m):
    plt.figure(1)
    gs = gridspec.GridSpec(1, 2,
                       width_ratios=[3, 1])
    plt.subplot(gs[0])
    plt.plot(m[:,1], m[:,0], '.')

    plt.subplot(gs[1])
    sns.boxplot(y=m[:,2], fliersize=3, showmeans=True)
    plt.savefig("not_consensus_vs_length.svg")
    plt.show()


def main():
    points = []
    for fn in glob(DATA_PATH+'/all3/*'):
        points.append(count_notcons_and_length(fn))
    m = np.array(points)
    plot_scatter(m)




if __name__ == '__main__':
    main()