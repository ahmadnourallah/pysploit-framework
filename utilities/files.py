import os, shutil, grp
from getpass import getuser

def count_subfolders_files(path = str(os.getcwd())):
    count_subfolders_files.result = []
    for dir,count_subfolders_files.subdir,files in os.walk(path):
        count_subfolders_files.result.append(files)
        if len(files) == 0:
            count_subfolders_files.result.remove(files)
    return len(count_subfolders_files.result)
def count_files(path = str(os.getcwd()), hidden = True):
    files_list = []
    for all_element in os.listdir(path):
        files_list.append(all_element)
        for directories in files_list:
            if os.path.isdir(path+'/'+directories):
                files_list.remove(directories)
    if hidden == True:
        return len(files_list)
    else:
        files_list = [files_list.split(".")[0] for files_list in files_list]
        for hidden in files_list:
            if len(hidden) == 0:
                files_list.remove(hidden)
                for hidden in files_list:
                    if len(hidden) == 0:
                        files_list.remove(hidden)
        return len(files_list)
def count_python_files(path = str(os.getcwd())):
    python_files = []
    for dirs,subdir,files in os.walk(path):
        for element in files:
            if element.endswith('.py'):
                python_files.append(element)
    return len(python_files)

def count_dirs(path = str(os.getcwd()), hidden = True):
    directories_list = []
    for all_element in os.listdir(path):
        directories_list.append(all_element)
        for files in directories_list:
            if os.path.isfile(path+'/'+files):
                directories_list.remove(files)
    if hidden == True:
        return len(directories_list)
    else:
        directories_list = [directories_list.split(".")[0] for directories_list in directories_list]
        for hidden in directories_list:
            if len(hidden) == 0:
                directories_list.remove(hidden)
                for hidden in directories_list:
                    if len(hidden) == 0:
                        directories_list.remove(hidden)
        return len(directories_list)
def copy(src,dst):
    if type(src) == list:
        if type(dst) == list:
            try:
                for i in range(0,10000000):
                    if os.path.isfile(src[i]):
                        shutil.copy(src[i], dst[i])
                    else:
                        shutil.copytree(src[i], dst[i]+'/'+src[i])
            except IndexError:
                pass
        else:
            for src_el in src:
                if os.path.isfile(src_el):
                    shutil.copy(src_el,dst)
                else:
                    shutil.copytree(src_el,dst+'/'+src_el)
    else:
        if os.path.isfile(src):
            shutil.copy(src,dst)
        else:
            shutil.copytree(src,dst+'/'+src)

def move(src,dst):
    if type(src) == list:
        if type(dst) == list:
            try:
                for i in range(0,10000000):
                    if os.path.isfile(src[i]):
                        shutil.move(src[i], dst[i])
                    else:
                        shutil.copytree(src[i], dst[i]+'/'+src[i])
                        shutil.rmtree(src[i])
            except IndexError:
                pass
        else:
            for src_el in src:
                if os.path.isfile(src_el):
                    shutil.move(src_el,dst)
                else:
                    shutil.copytree(src_el,dst+'/'+src_el)
                    shutil.rmtree(src_el)
    else:
        if os.path.isfile(src):
            shutil.move(src,dst)
        else:
            shutil.copytree(src,dst+'/'+src)
            shutil.rmtree(src)
def touch(name):
    file = open(name,'w')
    file.close()
def rename(src,dst):
        os.rename(src,dst)
def rm(path):
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)
def ls(dir = str(os.getcwd())):
    for i in os.listdir(dir):
        print(i)
def cd(path):
    os.chdir(path)
def pwd():
    print(os.getcwd())
