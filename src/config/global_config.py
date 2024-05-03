"""
The collection of global configurations
"""
CONFIG = {
	'DATASETS':				[
								'amazon_books_60core_kg',
								'mind',
								'movielens',
								'movielens_1m'
							],
	'MODELS':				[
								# General Recommendation
								'ItemKNN',
								'Pop',
								'Random',
								'SimpleX',
								# Matrix fact & Linear
								'ADMMSLIM', # NOT_EXEC
								'BPR',
								'DMF',
								'ENMF',
								'FISM',
								'NCEPLRec',
								'SLIMElastic',
								# Deep Learning-based
								'CDAE',
								'ConvNCF', # NOT_EXEC
								'DiffRec',
								'EASE',
								'GCMC',
								'LDiffRec',
								'MacridVAE',
								'MultiDAE',
								'MultiVAE',
								'NAIS',
								'NeuMF',
								'NGCF',
								'NNCF', # NOT_EXEC
								'LightGCN',
								'RaCT', # NOT_EXEC
								'RecVAE',
								# Graph-based
								'DGCF',
								'LINE',
								'NCL',
								'SGL',
								'SpectralCF',
								# Knowledge-aware
								'CKE',
								'CFKG',
								'KGAT', # NOT_EXEC
								'KGCN',
								'KGIN',
								'KGNNLS',
								'KTUP',
								'MCCLK', # NOT_EXEC
								'MKR',
								'RippleNet'
							],
	'LOG_FILE':				'log/carbon_tuning.log',
	'LOG_FILE_DEFAULT':		'log/carbon_default.log',
	'DATASET_PATH':			'data/',
	'RESULT_PATH':			'results/',
	'RESULT_PATH_SHARED':	'results_shared/',
	'EMISSIONS_FILE':		'/emissions.csv',
	'METRICS_FILE':			'/metrics.csv',
	'PARAMS_FILE':			'/params.csv',
	'STATIC_CONFIG_FILE':	'src/config/_params.yaml',
	'HP_CONFIG_PATH':		'src/config/hyperparam/',
	'COUNTER':				1,
	'DATASET_FILE':			'notebooks/data/dataset.csv'
}

# add reduced datasets
CONFIG['DATASETS'].extend([f'amazon_books_60core_kg_split_{x}' for x in [2, 4, 6, 8, 10]])
CONFIG['DATASETS'].extend([f'mind_split_{x}' for x in [2, 4, 6, 8, 10]])
CONFIG['DATASETS'].extend([f'movielens_split_{x}' for x in [2, 4, 6, 8, 10]])
CONFIG['DATASETS'].extend([f'movielens_1m_split_{x}' for x in [2, 4, 6, 8, 10]])

def get_global_config():
	"""
	The getter method
	"""
	return CONFIG


def set_global_config(key, value):
	"""
	The setter method
	"""
	CONFIG.update({key: value})