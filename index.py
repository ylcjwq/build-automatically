import subprocess
import os
import json


# 构建vue3项目
def construct_vue3():
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
    command = 'npm create vite@latest {} -- --template vue-ts'.format(name)
    try:
        print("脚本执行中。。。请稍后")
        result = subprocess.run(command, shell=True, check=True)
        if result.returncode == 0:
            print("项目构建成功")
            # 在这里执行另一个命令
            initialize = "npm install"
            print("开始安装依赖")
            res = subprocess.run(initialize, shell=True,
                                 check=True, cwd=name)
            if res.returncode == 0:
                print("依赖安装成功")
                os.chdir(createPath)
                vueItem = "npm install vue-router@next pinia axios @types/node"
                rs = subprocess.run(vueItem, shell=True, check=True)
                print("开始安装路由")
                if rs.returncode == 0:
                    print("路由安装成功")
                    print("开始生成路由文件")
                    router()
                    print("开始生成路由页面")
                    views()
                    print("开始生成仓库文件")
                    store()
                    print("开始修改main文件")
                    revise()
                    print("开始修改配置文件")
                    ts_json()
                else:
                    print("路由安装失败！")
            else:
                print("依赖安装失败！")
        else:
            print("项目构建失败")
    except subprocess.CalledProcessError as e:
        print(e)
    else:
        input("按下回车键退出")


# 构建vue2项目
def construct_vue2():
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
    command = 'vue create {}'.format(name)
    try:
        print("脚本执行中。。。请稍后")
        result = subprocess.run(command, shell=True, check=True)
        if result.returncode == 0:
            print("项目构建成功")
            # 在这里执行另一个命令
            initialize = "npm install"
            print("开始安装依赖")
            subprocess.run(initialize, shell=True, check=True, cwd=name)
        else:
            print("项目构建失败")
    except subprocess.CalledProcessError as e:
        print(e)
    else:
        input("按下回车键退出")


# 构建react项目
def construct_react():
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
    command = 'create-react-app {}'.format(name)
    try:
        print("脚本执行中。。。请稍后")
        result = subprocess.run(command, shell=True, check=True)
        if result.returncode == 0:
            print("项目构建成功")
            # 在这里执行另一个命令
        else:
            print("项目构建失败")
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


# 生成router文件夹
def router():
    router_path = os.path.join(os.getcwd(), "src", "router")
    print(router_path)
    os.makedirs(router_path, exist_ok=True)
    os.chdir(router_path)
    file_path = os.path.join(os.getcwd(), "index.ts")
    with open(file_path, "w") as file:
        content = """
import {
  createRouter,
  createWebHashHistory,
  RouterOptions,
  Router,
  RouteRecordRaw,
} from "vue-router";

const routes: RouteRecordRaw[] = [
  { path: "/", name: "Home", component: () => import("@/views/Home.vue") },
  {
    path: "/about",
    name: "About",
    component: () => import("@/views/About.vue"),
  },
];

const options: RouterOptions = {
  history: createWebHashHistory(),
  routes,
};

const router: Router = createRouter(options);

export default router;
        """
        file.write(content.lstrip())
    os.chdir("..")


# 生成views文件夹
def views():
    views_path = os.path.join(os.getcwd(), "views")
    print(views_path)
    os.makedirs(views_path, exist_ok=True)
    os.chdir(views_path)
    # 生成Home页面文件
    file_path = os.path.join(os.getcwd(), "Home.vue")
    with open(file_path, "w") as file:
        content = """
<template>
  <h1>Home页面</h1>
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>
        """
        file.write(content.lstrip())
    # 生成About页面文件
    file_path = os.path.join(os.getcwd(), "About.vue")
    with open(file_path, "w") as file:
        content = """
<template>
  <h1>About页面</h1>
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>
        """
        file.write(content.lstrip())
    os.chdir("..")


# 生成store文件夹
def store():
    store_path = os.path.join(os.getcwd(), "store")
    print(store_path)
    os.makedirs(store_path, exist_ok=True)
    os.chdir(store_path)
    file_path = os.path.join(os.getcwd(), "index.ts")
    with open(file_path, "w") as file:
        content = """
import { defineStore } from "pinia"
import { ref } from "vue"

export const useIndexStore = defineStore("index", () => {
    const content = ref<number>(1)
    return { content }
})
        """
        file.write(content.lstrip())
    os.chdir("..")


# 修改main.ts文件
def revise():
    try:
        file_path = os.path.join(os.getcwd(), "main.ts")
        print(file_path)

        # 修改main.ts文件内容
        new_content = """
import { createApp } from 'vue'
import router from '../src/router' 
import { createPinia } from 'pinia'
import App from './App.vue'

const pinia = createPinia()
const app = createApp(App)
app.use(router).use(pinia).mount('#app')
        """
        with open(file_path, 'w') as file:
            file.write(new_content.lstrip())

    except FileNotFoundError:
        print('文件未找到')

    except Exception as e:
        print('出现错误：', e)


# 修改配置文件
def ts_json():
    try:
        # 在src下新建vue.d.ts配置文件
        file_path = os.path.join(os.getcwd(), "vue.d.ts")
        new_content = """
declare module "*.vue" {
  import { defineComponent } from "vue";
  const Component: ReturnType<typeof defineComponent>;
  export default Component;
}
        """
        with open(file_path, 'w') as file:
            # lstrip 去除首行空行
            file.write(new_content.lstrip())

        # 修改vite.config.ts的内容
        os.chdir("..")
        file_path = os.path.join(os.getcwd(), "vite.config.ts")

        new_content = """
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import * as path from "path";

export default defineConfig({
  plugins: [vue()],
  build: {
    emptyOutDir: false,
  },
  resolve: {
    dedupe: ["vue"],
    alias: {
      "@": path.join(__dirname, "src"),
    },
  },
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:3300",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
})
        """

        with open(file_path, 'w') as file:
            file.write(new_content.lstrip())

        # 修改package.json文件
        file_path = os.path.join(os.getcwd(), "package.json")
        with open(file_path, 'r') as file:
            data = json.load(file)

        data['scripts']['dev'] = 'vite --open'

        with open('package.json', 'w') as file:
            json.dump(data, file, indent=2)

    except FileNotFoundError:
        print('文件未找到')

    except Exception as e:
        print('出现错误：', e)


print("请选择需要启动的脚本：")
print("1.生成vue3项目  2.生成vue2项目  3.生成react项目  4.pip  5.退出")
a = int(input())
while a != 1 and a != 2 and a != 3 and a != 4 and a != 5:
    print("输入不合法，请输入1、2、3、4、5其中一个数字！")
    a = int(input())
if a == 1:
    construct_vue3()
elif a == 2:
    construct_vue2()
elif a == 3:
    construct_react()
elif a == 4:
    run_pip()
else:
    exit()
