import os
from pathlib import Path


def print_directory_structure(root_dir, prefix="", exclude_dirs=None):
    """
    递归生成目录结构的每行内容列表
    :param root_dir:
    :param prefix:
    :param exclude_dirs:
    :return:
    """
    result = []
    if exclude_dirs is None:
        exclude_dirs = []
    try:
        # 获取当前目录下的所有文件和文件夹
        items = os.listdir(root_dir)
    except PermissionError:
        result.append(f"没有权限访问 {root_dir}，跳过该目录。")
        return result
    for index, item in enumerate(items):
        # 拼接当前项的完整路径
        item_path = os.path.join(root_dir, item)
        # 判断是否为需要排除的目录
        if os.path.isdir(item_path) and item in exclude_dirs:
            continue
        # 判断是否为最后一个项
        is_last = index == len(items) - 1
        # 根据是否为最后一个项选择不同的前缀符号
        connector = "└── " if is_last else "├── "
        # 生成当前项的显示内容
        line = prefix + connector + item
        result.append(line)
        # 如果当前项是文件夹，则递归调用函数
        if os.path.isdir(item_path):
            # 根据是否为最后一个项选择不同的子前缀
            new_prefix = prefix + ("    " if is_last else "│   ")
            sub_result = print_directory_structure(item_path, new_prefix, exclude_dirs)
            result.extend(sub_result)
    return result


def main():
    root_dir = r'D:\A\assistant\src\server'
    # root_dir = r'.'
    result = print_directory_structure(root_dir=root_dir, exclude_dirs=[
        '.git',
        '.next',
        '.idea',
        'node_modules',
    ])
    result = [Path(root_dir).absolute().name] + result
    result = '\n'.join(result)
    print(result)


main()
