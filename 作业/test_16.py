'''题目：输出指定格式的日期。
程序分析：使用 datetime 模块。'''
import datetime
print(datetime.date.today().strftime('%d/%m/%y'))
# 输出今日日期
birthdate = datetime.date(1941,1,5)
print(birthdate.strftime('%d/%m/%y'))
# 创建日期对象
birthnextday = birthdate+datetime.timedelta(days=1)
print(birthnextday.strftime('%d/%m/%y'))
# 日期算数运算
firstbirthday = birthdate.replace(year=birthdate.year+1)
print(firstbirthday.strftime('%d/%m/%y'))
# 日期替换
