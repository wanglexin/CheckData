import pymysql
from decimal import *


class tools(object):
    def Connectsql(sql, sid):
            connect = pymysql.connect(
                host='',
                port=3306,
                user='',
                password='',
                db='',
                charset='utf8'
            )
            cursor = connect.cursor()
            cursor.execute(sql, (sid))
            #result = cursor.fetchone()只查询单条数据
            result = cursor.fetchall()#查询多条数据
            cursor.close()
            connect.close()
            return result

    def toMoneyConnectsql(sql, toid):
        connect = pymysql.connect(
            host='',
            port=3306,
            user='',
            password='',
            db='',
            charset='utf8'
        )
        cursor = connect.cursor()
        cursor.execute(sql, (toid, toid))
        #result = cursor.fetchone()#只查询单条数据
        result = cursor.fetchall()#查询多条数据
        cursor.close()
        connect.close()
        return result

    #以下是统计原始订单库商户收入数据
    def WechatIncome(sid):
        print("开始执行sql语句了")
        arrs = ', '.join(list(map(lambda x: '%s', sid)))
        sql = "SELECT w.sub_mch_id,sub_mch_id,ROUND(SUM(t.feel_fact_money - t.mobi_num) / 100,2) feel_fact_money,DATE_FORMAT(pay_success_time,'%%Y-%%m') sumtime FROM w_orders t INNER JOIN w_wechat_pay_info w ON t.w_order_id = w.w_order_id WHERE t.pay_state IN (2, 3, 5)AND w.sub_mch_id IN ({arrs}) AND t.pay_success_time >= '2019-07-01 00:00:00'AND t.pay_success_time < '2019-08-01 00:00:00' GROUP BY w.sub_mch_id,sumtime".format(arrs=arrs)
        result = tools.Connectsql(sql, (sid))
        print("已经结束执行sql了")
        resultlist = []
        for r in result:
            resultlist.append(str(Decimal(r[2]).quantize(Decimal('0.00'))))
        return resultlist

    #以下是统计原始订单库商户收入数据
    def lastmonth(toid):
        sql = "SELECT ifnull(sum(pay_amount)/100,0) FROM ********* w WHERE 1=1 AND w.sub_mch_id = %s and trade_no IN(SELECT trade_no FROM cp_scan_orders_201908 WHERE 1=1 AND w.sub_mch_id  = %s and trade_type = 'R')"
        result = tools.toMoneyConnectsql(sql, toid)
        return result
        #以下是统计原始订单库商户收入数据
    def nextmonth(toid):
        sql = "SELECT ifnull(sum(pay_amount)/100,0) FROM ******** w WHERE 1=1 AND w.sub_mch_id = %s and trade_no IN(SELECT trade_no FROM cp_scan_orders_201907 WHERE 1=1 AND w.sub_mch_id  = %s and trade_type = 'R')"
        result = tools.toMoneyConnectsql(sql, toid)
        return result

