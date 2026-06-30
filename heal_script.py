import requests
import time
import subprocess
import datetime

PROMETHEUS_URL = "http://localhost:9090/api/v1/query"
THRESHOLD = 0.6
CHECK_INTERVAL = 15

def query_prometheus(query):
    try:
        response = requests.get(PROMETHEUS_URL, params={'query': query}, timeout=5)
        result = response.json()
        if result['data']['result']:
            value = result['data']['result'][0]['value'][1]
            return float(value)
    except Exception as e:
        print(f"[{datetime.datetime.now()}] 查询 Prometheus 失败: {e}")
    return None

def restart_order_service():
    try:
        print(f"[{datetime.datetime.now()}] ⚠️ 触发自愈：响应时间超限，正在重启 order-service...")
        subprocess.run(["docker", "restart", "order-service"], check=True, capture_output=True)
        with open("heal_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} | 自愈操作：容器重启成功\n")
        print(f"[{datetime.datetime.now()}] ✅ 自愈完成，容器已重启")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] ❌ 自愈失败: {e}")

if __name__ == "__main__":
    print("🚀 AIOps 自愈监控已启动，正在监控 order-api 响应时间...")
    while True:
        avg_time = query_prometheus(
            'rate(order_request_duration_seconds_sum[1m]) / rate(order_request_duration_seconds_count[1m])'
        )
        if avg_time is not None:
            print(f"[{datetime.datetime.now()}] 当前平均响应时间: {avg_time:.3f}s", end="")
            if avg_time > THRESHOLD:
                print(" 🔴 超标！")
                restart_order_service()
            else:
                print(" 🟢 正常")
        time.sleep(CHECK_INTERVAL)