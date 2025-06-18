import matplotlib.pyplot as plt
import numpy as np

metrics = ['Macro Precision',  'Macro Recall', 'Macro F1', 'Weighted Precision', 'Weighted Recall',  'Weighted F1']
randomforest = [0.2499, 0.3927, 0.2850,  0.6143, 0.8651, 0.7048]
schematree = [0.3612, 0.3236, 0.3267, 0.5657, 0.5678, 0.5588]

x = np.arange(len(metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width/2, randomforest, width, label='Random Forest')
bars2 = ax.bar(x + width/2, schematree, width, label='SchemaTree')

ax.set_ylabel('Score')
#ax.set_title('Comparison of Models Across Metrics')
ax.set_xticks(x)
ax.set_xticklabels(metrics, rotation=45)
ax.legend()

plt.tight_layout()
plt.show()
