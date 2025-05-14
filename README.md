# XPLatinBERT

This model is a fine-tuned version of LatinBERT for the purpose of my MA thesis.
LatinBERT was fine-tuned in an unsupervised MLM-task on the Patrologia Latina corpus from the Corpus Corporum project,
kindly made available to me by Philip Roelli at the University of Zürich (https://mlat.uzh.ch/browser?path=/38).

For details about the model, refer to:

Lafage, D. (2025). *Corpus Christi. En diakron korpuslingvistisk studie av kristendomens påverkan på latinsk semantik.* Göteborgs Universitet.

Note that XPL is not trained on [CLS] or [SEP], so if you want to retrieve sentence embeddings,
you need to compute them yourself (e.g. by calculating an average sentence embedding).

**Benchmark**

XPL coupled with an Average Pairwise Distances algorithm outperforms the models for Latin documented in Schlechtweg et al. (2020)
on the task of graded semantic change detection (Lafage 2025:37–39). 
