import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
from util.gmm import gmm as gmm_class


from quat_ds import quat_ds as quat_ds_class
from util import plot_tools, traj_generator, quat_tools, load_tools, process_tools



"""####### LOAD AND PROCESS DATA ########"""
q_in, index_list                        = load_tools.load_clfd_dataset(task_id=2, num_traj=1, sub_sample=1)
q_in, q_out, q_init, q_att, index_list  = process_tools.pre_process(q_in, index_list, opt= "slerp")


"""############ PERFORM QUAT-DS ############"""

gmm = gmm_class(q_in, q_att, index_list, K_init=4)
label = gmm.begin()


w_train = np.zeros((len(q_in), gmm.K))
# w_train = np.zeros((1, gmm.K))

for i in range(len(q_in)):
    w_train[i, :] = gmm.postLogProb(q_init).T
plot_tools.plot_gmm_prob(w_train, title="GMM Posterior Probability of Original Data")




# quat_ds.begin()

# q_init = R.from_quat(-q_init.as_quat())

# q_test, w_test = quat_ds.sim(q_init)


# """############ PLOT RESULTS #############"""

# plot_tools.plot_quat(q_test, title='q_test')
# plot_tools.plot_gmm_prob(w_test, title="GMM Posterior Probability of Reproduced Data")

plt.show()