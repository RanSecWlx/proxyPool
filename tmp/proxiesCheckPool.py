import os
import re
import sys
import shutil
from randomProxy import randomProxy
from multiprocessing import Queue, Process, Manager

class proxiesCheckPool(object):
    def __init__(self, fpath):
        self._randomProxyData = randomProxy(fpath)

    # 定义消费者任务，处理队列中的数据
    def consumer_task(self, task_queue, result_queue):
        while True:
            item = task_queue.get()  # 获取任务
            if item is None:  # 如果为 None 表示无更多任务
                break
            # 处理任务
            result = self._randomProxyData.is_network_reachable(item)
            #print("consumer_task:", result)
            if result.endswith("failed") is True:
                continue
            result_queue.put(result)  # 将结果放入结果队列

    # 定义生产者任务，将任务放入队列
    def producer_task(self, task_queue, num_consumers):
        for item in self._randomProxyData._proxiesList:
            task_queue.put(item)  # 将任务放入队列
    
        print(f"proxies pool:{task_queue.qsize()} proxies accessible")
        # 放入结束标记
        for _ in range(num_consumers):
            task_queue.put(None)
    
    # 结果处理进程
    def result_task(self, result_queue):
        count = 0
        fpath = self._randomProxyData._readFile
        while True:
            result = result_queue.get()
            if result is None:  # 退出标记
                break
            #print(result)
            proxy = result.strip().replace(" ok", "")
            res = f"{proxy}\r\n"
            
            if res.lower().startswith("http://"):
                proxy_type = "http"
            elif res.lower().startswith("https://"):
                proxy_type = "https" 
            elif res.lower().startswith("socks4://"):
                proxy_type = "socks4"
            elif res.lower().startswith("socks5://"):
                proxy_type = "socks5"
            else:
                continue
            #print(res.strip())
            with open(f"{self._randomProxyData._outDir}/{proxy_type}.txt", "a") as tf:
                tf.write(res)
            count += 1
            #print(count)
        #shutil.move(f"{fpath}.new", fpath)
        print(f"proxies pool:{count} proxies ok")
    
    def do_proxies_load(self):
        # 初始化任务队列和结果队列
        task_queue = Queue()
        result_queue = Queue()
        
        # 定义消费者进程数量
        num_consumers = 300
        
        # 创建并启动消费者进程
        consumers = [Process(target=self.consumer_task, args=(task_queue, result_queue)) for _ in range(num_consumers)]
        for consumer in consumers:
            consumer.start()
        
        # 启动生产者任务
        #self.producer_task(task_queue, num_consumers)
        producer_processor = Process(target=self.producer_task, args=(task_queue, num_consumers))
        producer_processor.start()

        # 启动结果处理进程
        result_processor = Process(target=self.result_task, args=(result_queue,))
        result_processor.start()
       
        producer_processor.join()
        # 等待所有消费者完成任务
        for consumer in consumers:
            consumer.join()
        
        # 发送退出信号给结果处理进程并等待其完成
        result_queue.put(None)
        result_processor.join()
        
        # 在主进程中打印所有结果
        #print("所有任务处理结果:", len(shared_results))
        #print("结果示例:", list(shared_results)[:10])  # 打印前10个结果

if __name__ == "__main__":
   
    if len(sys.argv) != 2:
        print(f"Usage: python3 {os.path.basename(__file__)} proxyfile")
        sys.exit(1)
    proxiesCheckPoolData = proxiesCheckPool(sys.argv[1])
    proxiesCheckPoolData.do_proxies_load()
