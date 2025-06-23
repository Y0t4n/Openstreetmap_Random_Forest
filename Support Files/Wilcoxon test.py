from scipy.stats import wilcoxon

# Stochastic model scores (e.g., from 5 runs)
random_forest_macro_prec = [0.2499, 0.2560, 0.2602, 0.2450, 0.2479, 0.2508, 0.2587, 0.2483, 0.2519, 0.2482]
random_forest_macro_rec = [0.3927, 0.4029, 0.3948, 0.3856, 0.3873, 0.3841, 0.3855, 0.3900, 0.4024, 0.3874]
random_forest_macro_f1 = [0.2850, 0.2907, 0.2890, 0.2804, 0.2822, 0.2787, 0.2842, 0.2810, 0.2880, 0.2816]

random_forest_weighted_prec = [0.6143, 0.6188, 0.6094, 0.6109, 0.6078, 0.6171, 0.6174, 0.6124, 0.6121, 0.6140]
random_forest_weighted_rec = [0.8651, 0.8687, 0.8641, 0.8598, 0.8629, 0.8640, 0.8631, 0.8628, 0.8662, 0.8675]
random_forest_weighted_f1 = [0.7048, 0.7068, 0.6985, 0.6997, 0.6985, 0.7029, 0.7034, 0.7013, 0.7022, 0.7031]

# Deterministic model score (constant)
schema_tree_macro_prec = 0.3612
schema_tree_macro_rec = 0.3236
schema_tree_macro_f1 = 0.3267

schema_tree_weighted_prec = 0.5657
schema_tree_weighted_rec = 0.5678
schema_tree_weighted_f1 = 0.5588

# Compute differences from the constant
differences_macro_prec = [x - schema_tree_macro_prec for x in random_forest_macro_prec]
differences_macro_rec = [x - schema_tree_macro_rec for x in random_forest_macro_rec]
differences_macro_f1 = [x - schema_tree_macro_f1 for x in random_forest_macro_f1]

differences_weighted_prec = [x - schema_tree_weighted_prec for x in random_forest_weighted_prec]
differences_weighted_rec = [i - schema_tree_weighted_rec for i in random_forest_weighted_rec]
differences_weighted_f1 = [fk - schema_tree_weighted_f1 for fk in random_forest_weighted_f1]

# Perform one-sample Wilcoxon signed-rank test
stat, p_m_p = wilcoxon(differences_macro_prec)
print("p-value macro prec:", p_m_p)

stat, p_m_r = wilcoxon(differences_macro_rec)
print("p-value macro rec:", p_m_r)

stat, p_m_f1 = wilcoxon(differences_macro_f1)
print("p-value macro f1:", p_m_f1)

stat, p_w_p = wilcoxon(differences_weighted_prec)
print("p-value weieghted prec:", p_w_p)

stat, p_w_r = wilcoxon(differences_weighted_rec)
print("p-value weighted rec:", p_w_r)

stat, p_w_f1 = wilcoxon(differences_weighted_f1)
print("p-value weighted f1:", p_w_f1)