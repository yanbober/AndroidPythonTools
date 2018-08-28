import os
import re
import shutil


class FileUtils(object):
	def delete_file_reg_content(file_path=None, reg_str=None, replace_as_str=''):
		'''
        文件字符串替换工具类
        :param file_path:	文件路径
        :param reg_str: 	要替换的文本正则表达式
        :param replace_as_str:	要替换成的新内容
        '''
		if file_path is None or reg_str is None:
			print('delete_file_reg_content params error!')
			return

		try:
			with open(file_path, 'r') as open_file:
				content = open_file.read()

			bak_file_path = file_path + '.bak'
			with open(bak_file_path, 'w') as out_file:
				result_content = re.sub(re.compile(reg_str, re.S), replace_as_str, content, 1)
				out_file.write(result_content)
			shutil.copy(bak_file_path, file_path)
		finally:
			os.remove(bak_file_path)



if __name__ == '__main__':
	reg_remove_str = r'<test.*?name="ABC">.*?</test>'
	FileUtils.delete_file_reg_content('file', reg_remove_str)
