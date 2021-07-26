import requests
import json
from bs4 import BeautifulSoup
import sys
from datetime import datetime


def crawler_cn_investing(start_date, end_date):
    s = requests.Session()
    headers = {
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    }

    data = {
        "curr_id": "6408",
        "smlID": "1159963",
        "header": "AAPL历史数据",
        "st_date": start_date,
        "end_date": end_date,
        "interval_sec": "Daily",
        "sort_col": "date",
        "sort_ord": "DESC",
        "action": "historical_data",
    }
    response = s.post(
        "https://cn.investing.com/instruments/HistoricalDataAjax",
        headers=headers,
        data=data,
    )

    parsed = BeautifulSoup(response.text, features="lxml").find(id="curr_table")
    collections = []
    for row in parsed.find_all("tr"):
        res = {}
        td = row.find_all("td")
        if td:
            index = 0
            for field in ["日期", "收盤", "開盤", "高", "低", "交易量", "漲跌幅"]:
                res.update({field: td[index].text})
                index += 1
        if res:
            collections.append(res)

    return json.dumps(collections, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        start_date = sys.argv[1]
        end_date = sys.argv[2]
    else:
        start_date = end_date = datetime.now().strftime("%Y/%m/%d")
    result = crawler_cn_investing(start_date, end_date)
    print(result)
