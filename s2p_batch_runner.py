import os
import sys
import pickle

s2p_batch_runner_path = "/n/data1/hms/neurobio/sabatini/gyu/data/mouse_g2FB/s2p_commander_20221215_172909.p"

with open(s2p_batch_runner_path, 'rb') as handle:
    s2p_batch_runner = pickle.load(handle)

# for cmd_mkdir in s2p_batch_runner['mkdir_list']:
#     os.system(cmd_mkdir)
    
for s2p_run in s2p_batch_runner['command_list']:
    os.system(s2p_run)

sys.exit(0)