"""
A collection of utility functions
"""
import os
from pathlib import Path
import torch
import csv
from datetime import datetime
from functools import reduce
from sys import platform
import pandas as pd


def create_folders(datasets, models, first_level_folders):
	"""Create folder structure in this order:
		│
		├── first_level_folders
		│   │
		│   └── datasets
		│   	│
		│   	└── models
	Args:
		first_level_folders (list): Folders root in which create structure.
		datasets (list): First level subfolders.
		models (list): Second level subfolders.
	Returns:
		None.
	"""
	for f in first_level_folders:
		for d in datasets:
			path_base = os.path.join(f, d)
			if not os.path.isdir(path_base):
				Path(path_base).mkdir(parents=True, exist_ok=True)
			for m in models:
				path_full = os.path.join(path_base, m)
				if not os.path.isdir(path_full):
					Path(path_full).mkdir(parents=True, exist_ok=True)


def get_device():
	"""Check the device available on the current machine.
	Args:
		None.
	Returns:
		str: The device name.
	"""
	device = 'cpu'
	# Macos GPU
	if torch.backends.mps.is_available():
		device = 'mps'
	# Cuda GPU
	elif torch.cuda.is_available():
		device = 'cuda'
	return device


def write_dict_to_csv(file, my_dict):
	"""Write to csv file the given dictionary.
	Args:
		file (str): The file's path.
		my_dict (dict): Data to be written as a Python dictionary.
	Returns:
		None.
	"""
	if os.path.isfile(file):
		with open(file, 'a', encoding='utf-8') as outfile:
			csvwriter = csv.writer(outfile, delimiter=',')
			csvwriter.writerow(my_dict.values())
	else:
		with open(file, 'w', encoding='utf-8') as outfile:
			csvwriter = csv.writer(outfile, delimiter=',')
			csvwriter.writerow(my_dict)
			csvwriter.writerow(my_dict.values())


def get_date_time():
	"""Convert the current date in standard datetime format.
	Args:
		None.
	Returns:
		str: The datetime formatted.
	"""
	ts = datetime.timestamp(datetime.now())
	date_time = datetime.fromtimestamp(ts)
	return date_time.strftime("%Y-%m-%d %H:%M:%S")


def get_total_iterations(file):
	"""Compute the total number of iterations according to the grid-search parameters.
	Args:
		file (str): The configuration's file path (.hyper)
	Return:
		int: The total number of iterations.
	"""
	lenghts = []
	with open(file, "r") as fp:
		for line in fp:
			para_list = line.strip().split(" ")
			if len(para_list) < 3:
				continue
			lenghts.append(len(eval("".join(para_list[2:]))))
	return reduce(lambda x, y: x * y, lenghts)


def get_ds_statistics(dataset):
	"""Compute the dataset statistics.
	Args:
		dataset (str): The dataset path.
	Returns:
		dict: The statistics in this order:
		{
			# Related to all dataset
			'n_users': int,
			'n_items': int,
			'n_inter': int,
			'sparsity': float,

			# Related to KG dataset otherwise set to zero
			'kg_entities': int,
			'kg_relations': int,
			'kg_triples': int,
			'kg_items': int,
		}
	Raises:
    	ValueError: if 'ds.inter' file is missing.
	"""
	ds_statistics = {}
	d = dataset.split('\\')[-1] if platform == 'win32' else dataset.split('/')[-1]
	if os.path.isdir(dataset) and d+'.inter' in os.listdir(dataset):
		inter = pd.read_csv(os.path.join(dataset, d+'.inter'), sep='\t')
		ds_statistics['n_users'] = len(inter["user_id:token"].unique())
		ds_statistics['n_items'] = len(inter["item_id:token"].unique())
		ds_statistics['n_inter'] = len(inter)
		ds_statistics['sparsity'] = 1 - ds_statistics['n_inter'] / ds_statistics['n_users'] / ds_statistics['n_items']
		if d+'.kg' in os.listdir(dataset):
			kg = pd.read_csv(os.path.join(dataset, d+'.kg'), sep='\t')
			link = pd.read_csv(os.path.join(dataset, d+'.link'), sep='\t')
			head = kg["head_id:token"].to_list()
			tail = kg["tail_id:token"].to_list()
			ds_statistics['kg_entities'] = len(set(head + tail))
			ds_statistics['kg_relations'] = len(kg["relation_id:token"].unique())
			ds_statistics['kg_triples'] = len(kg)
			ds_statistics['kg_items'] = len(link["item_id:token"].unique())
		else:
			ds_statistics['kg_entities'] = 0
			ds_statistics['kg_relations'] = 0
			ds_statistics['kg_triples'] = 0
			ds_statistics['kg_items'] = 0
		return ds_statistics
	else:
		missing = (d+'.inter').upper()
		raise ValueError('DATASET ERROR: missing required file ' + missing)


def get_model_type(model):
	"""Check the model type according to RecBole classification.
	Args:
		model (str): The model name. Case sensitive.
	Returns:
		str: The model type among ['general', 'sequential', 'context', 'knowledge']
	TODO:
		Currently managed only 'general' and 'knowledge'
	"""
	kg = ['CKE','CFKG','KGAT','KGCN','KGIN','KGNNLS','KTUP','MCCLK','MKR','RippleNet']
	return 'knowledge' if model in kg else 'general'
