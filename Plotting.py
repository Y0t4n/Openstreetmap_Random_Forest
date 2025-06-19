import matplotlib.pyplot as plt
import numpy as np

# Stochastic model scores (e.g., from 5 runs)
random_forest_macro_prec = [0.2499, 0.2560, 0.2602, 0.2450, 0.2479, 0.2508, 0.2587, 0.2483, 0.2519, 0.2482]
random_forest_macro_rec = [0.3927, 0.4029, 0.3948, 0.3856, 0.3873, 0.3841, 0.3855, 0.3900, 0.4024, 0.3874]
random_forest_macro_f1 = [0.2850, 0.2907, 0.2890, 0.2804, 0.2822, 0.2787, 0.2842, 0.2810, 0.2880, 0.2816]

random_forest_weighted_prec = [0.6143, 0.6188, 0.6094, 0.6109, 0.6078, 0.6171, 0.6174, 0.6124, 0.6121, 0.6140]
random_forest_weighted_rec = [0.8651, 0.8687, 0.8641, 0.8598, 0.8629, 0.8640, 0.8631, 0.8628, 0.8662, 0.8675]
random_forest_weighted_f1 = [0.7048, 0.7068, 0.6985, 0.6997, 0.6985, 0.7029, 0.7034, 0.7013, 0.7022, 0.7031]

metrics = ['Macro Precision',  'Macro Recall', 'Macro F1', 'Weighted Precision', 'Weighted Recall',  'Weighted F1']
randomforest = [np.average(random_forest_macro_prec), np.average(random_forest_macro_rec), np.average(random_forest_macro_f1), np.average(random_forest_weighted_prec), np.average(random_forest_weighted_rec), np.average(random_forest_weighted_f1)]
schematree = [0.3612, 0.3236, 0.3267, 0.5657, 0.5678, 0.5588]
print(np.average(random_forest_macro_prec), np.average(random_forest_macro_rec), np.average(random_forest_macro_f1), np.average(random_forest_weighted_prec), np.average(random_forest_weighted_rec), np.average(random_forest_weighted_f1))
x = np.arange(len(metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width/2, randomforest, width, label='Random Forest Mean')
bars2 = ax.bar(x + width/2, schematree, width, label='SchemaTree')

ax.set_ylabel('Score')
#ax.set_title('Comparison of Models Across Metrics')
ax.set_xticks(x)
ax.set_xticklabels(metrics, rotation=45)
ax.legend()

plt.tight_layout()
plt.show()
