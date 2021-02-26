from tools import execl
from tools import sqltools
import os


class check(object):
    def scripts(self, filename):
        a = execl.RWExcel.readExcel(filename)
        # for i in range(len(a)):
        #     b = sqltools.tools.WechatIncome(a[i])
        #     execl.RWExcel().SaveExcel(filename, i+2, b)
        b = sqltools.tools.WechatIncome(a)
        for i in range(len(b)):
            execl.RWExcel().SaveExcel(filename, i+2, b[i])
        print("已经导入完成，开始对比数据")
        execl.RWExcel.readExcelToMoney(filename)
        print("运行结束，请打开excel查看结果")

    def chceckpath(self, filename):
        a = os.path.exists(filename)
        if a == True:
            print("对账excel存在，可以进行后续操作")
        else:
            print("对账文件不存在，请检查桌面是否存在此文件")

if __name__ == '__main__':
    filename = r"C:\Users\wanglexin\Desktop\对账.xlsx"
    a = check()
    a.chceckpath(filename)
