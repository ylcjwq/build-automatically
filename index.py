import subprocess
import os


def run_command(num):
    print("请输入目标文件夹绝对路径(拖入文件夹)，直接按下回车将默认在桌面生成一个新文件夹")
    path = input()
    fileName = "mg"
    name = input("请输入项目名：")
    while name == "":
        print("请输入项目名称！")
        name = input("请输入项目名：")
    tName = name
    counter = 1
    if path:
        folder_path = path
    else:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        folder_path = os.path.join(desktop_path, fileName)
    # 打开或创建指定的文件夹
    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)
    createPath = os.path.join(folder_path, name)
    # 检查项目名是否已在文件夹中存在
    while os.path.exists(createPath):
        name = f"{tName}({counter})"
        createPath = os.path.join(folder_path, name)
        counter += 1
    if num == 1:
        command = 'npm create vite@latest {} -- --template vue-ts'.format(name)
    elif num == 2:
        command = 'vue create {}'.format(name)
    else:
        command = 'create-react-app {}'.format(name)
    try:
        print("脚本执行中。。。请稍后")
        result = subprocess.run(command, shell=True, check=True)
        if result.returncode == 0:
            print("命令执行成功")
            # 在这里执行另一个命令
            another_command = "npm install"
            print("开始执行")
            subprocess.run(another_command, shell=True, check=True, cwd=name)
        else:
            print("命令执行失败")
    except subprocess.CalledProcessError as e:
        print(e)
    else:
        input("按下回车键退出")


def run_pip():
    zip = input("请输入想要安装的pip包：")
    while zip == "":
        zip = input("请输入想要安装的pip包：")
    command = "pip install {} -i https://pypi.tuna.tsinghua.edu.cn/simple".format(
        zip)
    try:
        print("脚本执行中。。。请稍后")
        result = subprocess.run(command, shell=True, check=True)
        if result.returncode == 0:
            print("命令执行成功")
        else:
            print("命令执行失败")
    except subprocess.CalledProcessError as e:
        print(e)


print("请选择需要启动的脚本：")
print("1.生成vue3项目  2.生成vue2项目  3.生成react项目  4.pip  5.退出")
a = int(input())
while a != 1 and a != 2 and a != 3 and a != 4 and a != 5:
    print("输入不合法，请输入1、2、3、4、5其中一个数字！")
    a = int(input())
if a == 1:
    run_command(1)
elif a == 2:
    run_command(2)
elif a == 3:
    run_command(3)
elif a == 4:
    run_pip()
else:
    exit()
