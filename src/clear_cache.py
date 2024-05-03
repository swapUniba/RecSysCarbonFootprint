import sys
import os
import shutil


def clear_cache(path):
	for filename in os.listdir(path):
		if filename != '.gitignore':
			file_path = os.path.join(path, filename)
			try:
				if os.path.isfile(file_path) or os.path.islink(file_path):
					os.unlink(file_path)
				elif os.path.isdir(file_path):
					shutil.rmtree(file_path)
			except Exception as e:
				print('WARNING: failed to delete %s. Reason: %s' % (file_path, e))
	print(f'\033[95m{path:<16}\033[0mfolder successfully deleted!')


if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) == 0:
		print('\nWARNING: missing required parameters!')
		print('\n' + ''.join(['> ' for i in range(25)]))
		print(f'\n{"PARAM":<16}{"DESCRIPTION":<18}\n')
		print(''.join(['> ' for i in range(25)]))
		print(f'{"--log":<16}Delete \033[95mlog\033[0m folder.')
		print(f'{"--tb":<16}Delete \033[95mlog_tensorboard\033[0m folder.')
		print(f'{"--results":<16}Delete \033[95mresults\033[0m folder.')
		print(f'{"--saved":<16}Delete \033[95msaved\033[0m folder.')
		print(f'{"--all":<16}Delete \033[95mall\033[0m the previous folders.')
		print(''.join(['> ' for i in range(25)]) + '\n')
	else:
		values = [i[2:] for i in args]
		if 'all' in values and len(values) > 1:
			print('WARNING: parameters conflict!')
			print(values)
		else:
			if 'log' in values:
				clear_cache('log')
			if 'tb' in values:
				clear_cache('log_tensorboard')
			if 'results' in values:
				clear_cache('results')
				clear_cache('results_shared')
			if 'saved' in values:
				clear_cache('saved')
			if 'all' in values:
				clear_cache('log')
				clear_cache('log_tensorboard')
				clear_cache('results')
				clear_cache('results_shared')
				clear_cache('saved')
	sys.exit(0)
