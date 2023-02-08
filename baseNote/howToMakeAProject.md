1 创建一个文件夹 projectSample

2 在文件夹里面，使用命令 `python -m venv myvenv` 生成一个 虚拟环境

3 激活这个虚拟环境

> 激活脚本路径是 `.\myvenv\Scripts\activate.bat`，如果是 `powershell` 命令行，脚本换成 `Activate.ps1` , 注意将 `myvenv`换成你自己的虚拟环境目录

4 可以在这个虚拟环境里面 下载任意包

5 退出虚拟环境很简单，只需要执行 `deactivate` 命令就行

6 如果使用的是 vscode 的话 就可以在 解释器 里面选择 虚拟环境

7 创建以下目录的文件

projectSample/

- projectSample/
  - `__init__.py`
- bin/
- docs/
- `setup.py`
- tests/
  - `projectSample_tests.py`
  - `__init__.py`
