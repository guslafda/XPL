# XPLatinBERT

This model is a fine-tuned version of LatinBERT for the purpose of my MA thesis.
LatinBERT was fine-tuned in an unsupervised MLM-task on the *Patrologia Latina* corpus from the *Corpus Corporum* project,
kindly made available to me by Philip Roelli at the University of Zürich (https://mlat.uzh.ch/browser?path=/38). I am 
publishing the resulting model in case it can be useful to anyone interested in "Christian Latin".

For details about the model, including training and validation, as well as a problematization of the
concept of Christian Latin, refer to Lafage (2025) below.

For information about the original LatinBERT model, visit:

https://github.com/dbamman/latin-bert

Note that XPL is not trained on [CLS] or [SEP], so if you want to retrieve sentence embeddings,
you need to compute them yourself (e.g. by calculating an average sentence embedding).

**Benchmark**

XPL coupled with an Average Pairwise Distances algorithm outperforms the models for Latin documented in Schlechtweg et al. (2020)
on the task of graded semantic change detection (Lafage, 2025:37–39). It also outperforms LatinBERT on MLM on a testset
of unseen documents from the *Patrologia Latina*, showing its sensitivity to Christian Latin (Lafage, 2025:32–33).

**Installation**

To install the model, follow the instructions on https://github.com/dbamman/latin-bert.

**References**

Lafage, D. (2025). *Corpus Christi. En diakron korpuslingvistisk studie av kristendomens påverkan på latinsk semantik.* Göteborgs Universitet.

Schlechtweg, D., McGillivray, B., Hengchen, S., Dubossarsky, H. & Tahmasebi, N. (2020). SemEval-2020 Task 1: Unsupervised Lexical Semantic Change Detection. 
  In Herbelot et al. (Red.), *Proceedings of the Fourteenth Workshop on Semantic Evaluation* (pp. 1–23). Barcelona.
