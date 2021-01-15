import os

def get_type(name):
    """给定文件名，打印文件内容和后缀"""
    try:
        if os.path.exists(name):
            # 相关操作 如打印文件内容
            with open(name,"r+",encoding="utf-8") as f:
                print(f.read())
            # 处理后缀
            file = os.path.splitext(name)
            filename, type = file
            print(f"文件名:{filename} 后缀:{type}")
        else:
            print(f"{name}：文件不存在")
    except Exception as e:
        print(f"发生异常错误:{e}")


if __name__ == "__main__":
    get_type('11.py')