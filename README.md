# XPLatinBERT

This model is a fine-tuned version of LatinBERT for the purpose of my MA thesis.
LatinBERT was fine-tuned in an unsupervised MLM-task on the *Patrologia Latina* corpus from the *Corpus Corporum* project,
kindly made available to me by Philip Roelli at the University of Zürich (https://mlat.uzh.ch/browser?path=/38). I am 
publishing the resulting model in case it can be useful to anyone interested in "Christian Latin".

For details about the model, including training and validation, as well as a problematization of the
concept of Christian Latin, refer to Lafage (2025) below (I will soon publish a short version in English).

For information about the original LatinBERT model, visit:

https://github.com/dbamman/latin-bert

Note that XPL is not trained on [CLS] or [SEP], so if you want to retrieve sentence embeddings,
you need to compute them yourself (e.g. by calculating an average sentence embedding).

**Benchmark**

XPL coupled with an Average Pairwise Distances algorithm outperforms the models for Latin documented in Schlechtweg et al. (2020)
on the task of graded semantic change detection (Lafage, 2025:37–39). It also outperforms LatinBERT on MLM on a testset
of unseen documents from the *Patrologia Latina*, showing its sensitivity to Christian Latin (Lafage, 2025:32–33).

**Installation**

1. Install the requirements listed on https://github.com/dbamman/latin-bert/blob/master/requirements.txt.
2. Download the subword encoder from here: https://github.com/dbamman/latin-bert/blob/master/models/subword_tokenizer_latin/latin.subword.encoder
3. Download tokenizer_debug.py from this repository. It is a revised version of Patrick J. Burns's and Todd Cooks's Wordtokenizer, which did not tokenize enclitic *-que*, as per bug fix described in https://github.com/cltk/cltk/issues/1190.
4. If you're running Powershell like me, download and run the download.ps1 file, in order to download the model, or download the model manually by visiting:

https://drive.google.com/file/d/{FILE_ID}/view (replace {FILE_ID} with the file_id in the download.ps1 file).

**MLM task**

To verify that you have imported the model correctly, you can try to perform a simple MLM task with the mlm_xpl.py script. Modify the script by adding:

1. The system path where you have saved tokenizer_debug.py (sys.path.append).
2. The path to the downloaded model (bertPath) and to the subword tokenizer (tokenizerPath) under the arguments part (note that you have the possibility to import LatinBERT as well and select it as an argument):

if model_name == 'latinbert':
    bertPath = "xxx\\latin_bert"
    tokenizerPath = "xxx\\latin.subword.encoder"

if model_name == 'xpl':
    bertPath = "xxx\\XPL"
    tokenizerPath = "xxx\\latin.subword.encoder"

The script takes 3 arguments: a sentence, a word to mask and the model to use (LatinBERT or XPL). Example query (Powershell):

*python mlm_xpl.py -s 'Si vis pacem, para bellum.' -w 'pacem' -m 'xpl'*

**References**

Lafage, D. (2025). *Corpus Christi. En diakron korpuslingvistisk studie av kristendomens påverkan på latinsk semantik.* Göteborgs Universitet.

Schlechtweg, D., McGillivray, B., Hengchen, S., Dubossarsky, H. & Tahmasebi, N. (2020). SemEval-2020 Task 1: Unsupervised Lexical Semantic Change Detection. 
  In Herbelot et al. (Red.), *Proceedings of the Fourteenth Workshop on Semantic Evaluation* (pp. 1–23). Barcelona.
