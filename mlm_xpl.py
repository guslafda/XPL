import argparse
import sys
from tensor2tensor.data_generators import text_encoder
import torch
import torch.nn.functional as F
from torch import nn
from transformers import BertForMaskedLM

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#This line is to import a revised version of the LatinWordTokenizer, to fix the enclitic issue.
sys.path.append("xxx")
from tokenizer_debug import LatinWordTokenizer as WordTokenizer

class LatinBERT():

	def __init__(self, tokenizerPath=None, bertPath=None):
		encoder = text_encoder.SubwordTextEncoder(tokenizerPath)
		if model_name in ['latinbert', 'xpl']:
			self.wp_tokenizer = LatinTokenizer_latinBERT(encoder)
		self.model = BertLatin(bertPath=bertPath)
		self.model.to(device)

	def predict_masked_word(self, sents, mask_word, top_k=5):

		tokens = convert_to_toks(sents)

		for sent in tokens:
			masked_sentence = [tok if tok != mask_word.lower() else "[MASK]" for tok in sent]

			masked_sentence_str = " ".join(masked_sentence)

			tokenized_sentence = self.wp_tokenizer.tokenize(masked_sentence_str)

			input_ids = self.wp_tokenizer.convert_tokens_to_ids(tokenized_sentence)

			masked_idx = input_ids.index(self.wp_tokenizer.convert_tokens_to_ids(["[MASK]"])[0])

			input_ids = torch.tensor([input_ids]).to(device)
			
			attention_mask = torch.ones(input_ids.shape).to(device)
			

			with torch.no_grad():
				outputs = self.model(input_ids, attention_mask=attention_mask)
				predictions = outputs[0]

			predicted_logits = predictions[masked_idx]

			probs = F.softmax(predicted_logits, dim=-1)
		
			top_k_probs, top_k_ids = torch.topk(probs, top_k)

			top_k_tokens = self.wp_tokenizer.convert_ids_to_tokens(top_k_ids.tolist())

			top_predictions = [(token, prob.item()) for token, prob in zip(top_k_tokens, top_k_probs)]

			return top_predictions
		

class LatinTokenizer_latinBERT():
	def __init__(self, encoder):
		self.vocab={}
		self.reverseVocab={}
		self.encoder=encoder

		self.vocab["[PAD]"]=0
		self.vocab["[UNK]"]=1
		self.vocab["[CLS]"]=2
		self.vocab["[SEP]"]=3
		self.vocab["[MASK]"]=4

		for key in self.encoder._subtoken_string_to_id:
			self.vocab[key]=self.encoder._subtoken_string_to_id[key]+5
			self.reverseVocab[self.encoder._subtoken_string_to_id[key]+5]=key

	def convert_tokens_to_ids(self, tokens):
		wp_tokens=[]
		for token in tokens:

			if token == "[PAD]":
				wp_tokens.append(0)
			elif token == "[UNK]":
				wp_tokens.append(1)
			elif token == "[CLS]":
				wp_tokens.append(2)
			elif token == "[SEP]":
				wp_tokens.append(3)
			elif token == "[MASK]":
				wp_tokens.append(4)

			else:
				wp_tokens.append(self.vocab[token])

		return wp_tokens

	def tokenize(self, text):
		tokens=text.split(" ")
		wp_tokens=[]
		for token in tokens:

			if token in {"[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"}:
				wp_tokens.append(token)
			else:

				wp_toks=self.encoder.encode(token)

				for wp in wp_toks:
					wp_tokens.append(self.reverseVocab[wp+5])

		return wp_tokens

	def convert_ids_to_tokens(self, ids):
		tokens = []
		for id_ in ids:
			if id_ in self.reverseVocab:
				tokens.append(self.reverseVocab[id_])
			else:
				tokens.append("[UNK]")  # Handle unknown token IDs
		return tokens

def convert_to_toks(sents):

	word_tokenizer = WordTokenizer()

	all_sents=[]

	for sent in sents:
		text=sent.lower()

		tokens=word_tokenizer.tokenize(text)
		filt_toks=[]
		filt_toks.append("[CLS]")
		for tok in tokens:
			if tok != "":
				filt_toks.append(tok)
		filt_toks.append("[SEP]")

		all_sents.append(filt_toks)

	return all_sents


class BertLatin(nn.Module):

	def __init__(self, bertPath=None):
		super(BertLatin, self).__init__()

		self.bert = BertForMaskedLM.from_pretrained(bertPath)
		self.bert.eval()
		
	def forward(self, input_ids, attention_mask=None):
		outputs = self.bert(input_ids, attention_mask=attention_mask)
		return outputs.logits


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--model', choices=['latinbert', 'xpl'], help='Choose the model to load.', required=True)
	parser.add_argument('-s', '--sentence', help='Enter a sentence.', required=True)
	parser.add_argument('-w', '--word', help='Enter a word to mask.', required=True)
	
	args = vars(parser.parse_args())
	model_name = args["model"]

	if model_name == 'latinbert':
		bertPath = "xxx\\latin_bert"
		tokenizerPath = "xxx\\latin.subword.encoder"

	if model_name == 'xpl':
		bertPath = "xxx\\XPL"
		tokenizerPath = "xxx\\latin.subword.encoder"

	bert=LatinBERT(tokenizerPath=tokenizerPath, bertPath=bertPath)

	sents=[args["sentence"]]
	mask_word=args["word"]

	print(f'\n\nRunning {model_name}...\n')
	print(f'Sentence: {sents[0]}\n\nMasked word: {mask_word}. \n\nComputing prediction...\n')
	
	predicted_words = bert.predict_masked_word(sents, mask_word, top_k=5)

	print("\nPredicted words (Top 5) with probabilities:\n")
	for word, prob in predicted_words:
		print(f"{word.replace('_', '')}: {prob:.4f}") 
	print('\n')
	

