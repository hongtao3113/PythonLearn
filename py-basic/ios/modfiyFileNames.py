# 修改文件名称
# coding=utf-8
# /bin/py3.6
import os


def rename():
    path = "F:\\idea_workspace\\scm-hegang\\scm-std-ap\\scm-std-admin\\src\\main\\webapp\\bank\\offLineFact\\apply\\js"
    fileList = os.listdir(path)
    print("文件列表：", fileList)
    for file in fileList:
        oldFile = os.path.join(path, file)
        if os.path.isdir(oldFile):
            continue
        filename = os.path.splitext(file)[0]
        if 'msFact' in filename:
            filename = filename.replace('msFact', 'offLineFact')
            pass
        print("oldFile:", filename)  # 文件名
        filetype = os.path.splitext(file)[1]
        print("filetype:", filetype)  # 文件类型 .tpl
        newFile = os.path.join(path, filename + filetype)
        os.rename(oldFile, newFile)


rename()
