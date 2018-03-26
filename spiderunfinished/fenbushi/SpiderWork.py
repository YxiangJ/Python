# HTML下载器


class SpiderWork(object):

    def __init__(self):
        # 初始化分布式进程中工作节点的连接工作
        # 1.使用BaseManager注册于获取Queue的方法名称
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')
        # 2.连接到服务器
        server_addr = '127.0.0.1'
        print('Connect to server %s...' % server_addr)
        # 注意保持端口和验证口令与服务进程设置的完全一致
        self.m = BaseManager(address=(server_addr, 8002),
                             authkey='baike'.encode('utf-8'))
        # 从网络连接
        self.m.connect()
        # 3.获取Queue的对象
        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()
        # 初始化网页下载器和解析器
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        print('init finish')

    def crawl(self):
        while True:
            try:
                if not self.task.empty():
                    url = self.task.get()

                    if url == 'end':
                        print('控制节点通知爬虫节点停止工作...')
                        # 接着通知其他节点停止工作
                        self.result.put({'new_urls': 'end', 'data': 'end'})
                        return
                    print('爬虫节点正在解析：%s' % url.encode('utf-8'))
                    content = self.downloader.download(url)
                    new_urls, data = self.parser.parser(url, content)
                    self.result.put({'new_urls': new_urls, 'data': data})
            except EOFError as e:
                print("连接工作节点失败")
                return
            except Exception as e:
                print(e)
                print('Crawl fail')
if __name__ == '__main__':
    spider = SpiderWork()
    spider.crawl()
