# -*- coding: utf-8 -*-
#python3

from urllib import request, parse

class App:

    def __init__(self):
        self.proxies = []
        self.proxy = ''
        self.proxy_support = ''
        self.opener = ''
        self.start_proxies()
        self.run_num()

    def start_proxies(self):
        p = open('confirm_1120.json', 'r')
        for line in p:
            self.proxies.append(line.strip())
        p.close()

    def run_num(self):
        post_data = {'Id': '2217'}
        for i in range(len(self.proxies)):
            self.proxy = {'http': self.proxies[i]}
            self.proxy_support = request.ProxyHandler(self.proxy)
            self.opener = request.build_opener(self.proxy_support)
            request.install_opener(self.opener)

            print(self.proxy)

            try:
                res = request.urlopen('http://www.manyiaby.com/PhotoContest/Vote',
                                      parse.urlencode(post_data).encode('utf-8'))
                print(res.read())
            except IOError:
                print("Error,The proxy can't to do anything,try next...")
            else:
                print("pass")
                pass

if __name__ == '__main__':
    App()



