from distutils.core import setup
import py2exe

# 脚本文件名
script = 'index.py'

# 配置py2exe
setup(
    options={
        'py2exe': {
            'bundle_files': 1,  # 将所有文件打包成一个exe文件
            'compressed': True,  # 压缩生成的exe文件
            'optimize': 2  # 优化生成的exe文件
        }
    },
    console=[{'script': script}],  # 要打包的脚本文件
    zipfile=None  # 不生成zip文件
)
