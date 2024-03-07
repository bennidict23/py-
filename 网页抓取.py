import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 货币代号到中文名称的映射
currency_code_to_name = {
    "USD": "美元",
    "CHF": "瑞士法郎",
    "SGD": "新加坡元",
    "SEK": "瑞典克朗",
    "DKK": "丹麦克朗",
    "NOK": "挪威克朗",
    "JPY": "日元",
    "CAD": "加拿大元",
    "AUD": "澳大利亚元",
    "EUR": "欧元",
    "MOP": "澳门元",
    "PHP": "菲律宾比索",
    "THB": "泰国铢",
    "NZD": "新西兰元",
    "KRW": "韩元",
    "RUB": "卢布",
    "MYR": "林吉特",
    "TWD": "新台币",
    "ESP": "西班牙比塞塔",
    "ITL": "意大利里拉",
    "NLG": "荷兰盾",
    "BEF": "比利时法郎",
    "FIM": "芬兰马克",
    "IDR": "印尼卢比",
    "BRL": "巴西里亚尔",
    "AED": "阿联酋迪拉姆",
    "INR": "印度卢比",
    "ZAR": "南非兰特",
    "SAR": "沙特里亚尔",
    "TRY": "土耳其里拉",
    # ... 其他货币 ...
}

def get_exchange_rate(date, currency_code):
    driver = webdriver.Chrome()
    url = f"https://srh.bankofchina.com/search/whpj/search_cn.jsp?erectDate={date}&nothing={date}&pjname={currency_code_to_name[currency_code]}"
    driver.get(url)
    time.sleep(2)  # 等待页面加载完毕

    try:
        # 找到表格中的现汇卖出价
        cell_element = driver.find_element(By.XPATH, '//table/tbody/tr[2]/td[4]').text
        exchange_rate = cell_element
    except Exception as e:
        print(f"An error occurred: {e}")
        exchange_rate = None
    finally:
        driver.close()

    return exchange_rate

if __name__ == '__main__':
    date = sys.argv[1]
    currency_code = sys.argv[2]
    exchange_rate = get_exchange_rate(date, currency_code)
    if exchange_rate:
        print(exchange_rate)
        with open("result.txt", "w") as f:
            f.write(exchange_rate)
    else:
        print("未能获取到现汇卖出价。")
