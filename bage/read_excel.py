import pandas as pd

#读取测试数据
def load_testdata(filename, sheetname):
    try:
        df = pd.read_excel(filename, sheet_name=sheetname)
        df = df.fillna('')
        df = df.astype(str)
        return df.to_dict('records')
    except FileNotFoundError as e:
        print(f"文件 {filename} 未找到。请检查文件路径是否正确。")
        raise  # 或者选择其他处理方式，如返回空列表或None