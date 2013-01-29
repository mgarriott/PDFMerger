from cx_Freeze import setup, Executable

setup (
			name = 'PDFMerge',
			version = '0.1',
			description = 'Program for merging pages in a pdf doc.',
			executables = [Executable('merge.py')])
