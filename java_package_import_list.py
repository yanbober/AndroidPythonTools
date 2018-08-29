import os


# 找出指定包下面哪些类引用了另一个包下面的类
# 结果输出到文件
# JavaPackageImportRef().start(package_root_dir, used_dir)

class JavaPackageImportRef:
    __result_file = 'result.txt'
    __total_used_files = 0


    def __append_result_line(self, content, need_tab):
        with open(self.__result_file, 'a+') as f:
            if need_tab:
                f.write('\t'+content+'\n')
                self.__total_used_files = self.__total_used_files + 1
                print('\t'+content)
            else:
                f.write('\n'+content + '\n')
                print('\n'+content)


    def __is_contains_in_file(self, file, match):
        try:
            with open(file, "r") as fp:
                content = fp.read()
                if (content.find(match) != -1):
                    return True
        except Exception:
            return False
        return False


    def __find_package_used_in_target_dir(self, target_dir, package):
        for dir_path, dirs, files in os.walk(target_dir):
            for name in files:
                file_name = os.path.join(dir_path, name)
                if file_name.endswith('.java'):
                    if self.__is_contains_in_file(file_name, package):
                        self.__append_result_line(file_name, True)


    def __path_2_package(self, package_root_dir, path):
        path = path.replace(package_root_dir + os.sep, '')
        return path.replace(os.sep, '.')


    def total(self):
        return self.__total_used_files


    def start(self, package_root_dir, used_dir):
        os.remove(self.__result_file)
        for package_dir, dirs, files in os.walk(package_root_dir, topdown=False):
            for name in dirs:
                dir_path = os.path.join(package_dir, name)
                package = self.__path_2_package(package_root_dir, dir_path)
                if not self.__is_contains_in_file(self.__result_file, package):
                    self.__append_result_line(package, False)
                    self.__find_package_used_in_target_dir(used_dir, package)
        self.__append_result_line(('Total usage is: ' + str(self.__total_used_files)), False)


if __name__ == '__main__':
    find_process = JavaPackageImportRef()
    find_process.start('./moduleA/src', './src')
    print('start....')