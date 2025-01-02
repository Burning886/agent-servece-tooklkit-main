import os


def list_directory_structure(startpath='.'):
    # 获取当前目录名
    current_dir = os.path.basename(os.path.abspath(startpath))
    print(current_dir)

    for root, dirs, files in os.walk(startpath):
        # 计算当前层级
        level = root.replace(startpath, '').count(os.sep)
        # 跳过第一层，因为我们已经打印了当前目录名
        if level == 0:
            prefix = ""
        else:
            prefix = "│  " * (level - 1) + "├--"

            # 打印目录名
        if level > 0:  # 不打印顶级目录名（因为已经打印过了）
            print(f"{prefix}{os.path.basename(root)}")

            # 打印文件
        file_prefix = "│  " * level + "├--"
        for f in files:
            print(f"{file_prefix}{f}")

        # 执行函数


list_directory_structure()
