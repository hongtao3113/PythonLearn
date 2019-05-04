# 修改文件名称
# coding=utf-8
import os;


def rename():
    path = "E:\\mydata\\commonFiles\\2019\\03\\16";
    fileList = os.listdir(path);
    print("文件列表：", fileList);
    for file in fileList:
        oldFile = os.path.join(path, file);
        if os.path.isdir(oldFile):
            continue;
        filename = os.path.splitext(file)[0];
        print("oldFile:", filename)
        filetype = os.path.splitext(file)[1];
        newFile = os.path.join(path, "test" + filetype);
        os.rename(oldFile, newFile);


rename();
