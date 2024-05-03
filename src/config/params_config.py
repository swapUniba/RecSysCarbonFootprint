"""
The collection of static params configurations

https://recbole.io/docs/v0.1.2/user_guide/config_settings.html

"""
DEFAULT_PARAMS = {
	# Environment Setting
	'gpu_id': 0,
	'worker': 0,
	'use_gpu': 'True',
	'seed': 42,
	'state': 'INFO', # ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']
	'encoding': 'utf-8',
	'reproducibility': True,
	'data_path': 'data/',
	'checkpoint_dir': 'saved/',
	'show_progress': True,
	'shuffle': True,

	# Training Setting
	'epochs': 10,
	'train_batch_size': 2048,
	'learner': 'adam', # ['adam', 'sgd', 'adagrad', 'rmsprop', 'sparse_adam']
	'learning_rate': .001,
	'train_neg_sample_args': {
		'distribution': 'uniform', # ['uniform', 'popularity']
		'sample_num': 1,
		'dynamic': False,
		'candidate_num': 0
	},
	'eval_step': 1,
	'stopping_step': 10,
	'clip_grad_norm': None,
	'loss_decimal_place': 4,
	'weight_decay': .0,
	'require_pow': False,
	'enable_amp': False,
	'enable_scaler': False,

	# Evaluation Setting
	'eval_args': {
		'group_by': 'user', # ['user', 'none']
		'order': 'RO', # ['RO', 'TO']
		'split': {'RS': [0.8,0.1,0.1]}, # ['RS','LS']
		'mode': 'full' # ['full','unixxx','popxxx','labeled']
	},
	'repeatable': False,
	'metrics': ['Recall', 'MRR', 'NDCG', 'Hit', 'MAP', 'Precision', 'GAUC', 'ItemCoverage', 'AveragePopularity', 'GiniIndex', 'ShannonEntropy', 'TailPercentage'],
	'topk': 10,
	'valid_metric': 'MRR@10',
	'eval_batch_size': 4096,
	'metric_decimal_place': 4
}


def get_params():
	"""
	The getter method
	"""
	return DEFAULT_PARAMS


def set_param(key, value):
	"""
	The setter method
	"""
	DEFAULT_PARAMS.update({key: value})