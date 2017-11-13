from glob import glob 
from os.path import basename

DATA_PATH="/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/cba_times_mcc/rose_special_charged/run_10000"

def count_tr(fn, m, tr):
    with open(DATA_PATH+"/transitions_"+m+'/'+fn) as f:
        f.readline()
        s = f.readline()
        # s = tmp.replace('?','')
        for k in tr.keys():
            tr[k] += s.count(k)
            # print(k, s.count(k))
        



def main():
    tr_dssp = {'CH':0, 'HC':0, 'CE':0, 'EC':0, 'EH':0, 'HE':0}
    tr_stride = {'CH':0, 'HC':0, 'CE':0, 'EC':0, 'EH':0, 'HE':0}
    tr_kaksi = {'CH':0, 'HC':0, 'CE':0, 'EC':0, 'EH':0, 'HE':0}
    tr_pross = {'CH':0, 'HC':0, 'CE':0, 'EC':0, 'EH':0, 'HE':0}

    for i in glob(DATA_PATH+'/all3/*'):
        fn = basename(i)
        # print(fn)
        count_tr(fn, 'dssp', tr_dssp)
        count_tr(fn, 'stride', tr_stride)
        count_tr(fn, 'kaksi', tr_kaksi)
        count_tr(fn, 'pross', tr_pross)
        

    print("DSSP", tr_dssp)
    print("STRIDE", tr_stride)
    print("KAKSI", tr_kaksi)
    print("PROSS", tr_pross)

if __name__ == '__main__':
    main()