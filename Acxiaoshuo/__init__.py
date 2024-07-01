# _*_coding:utf-8
# @Time      :2023/11/23 0:27
# @Author    :DQ
# @FileName: __init__.py
import time

# 导入获取图片链接模块
import Acxiaoshuo.get_img.god_img
import Acxiaoshuo.get_img.hot_img
import Acxiaoshuo.get_img.newest_img
import Acxiaoshuo.get_img.novel_img
import Acxiaoshuo.get_img.sortvisit_img

# 导入获取页面链接模块
import Acxiaoshuo.get_link.god
import Acxiaoshuo.get_link.hot
import Acxiaoshuo.get_link.newest
import Acxiaoshuo.get_link.newest_novel
import Acxiaoshuo.get_link.sortvisit_link

# 导入工具模块，有封装好的一些方法可以直接调用
import Acxiaoshuo.tool.ua


def hot_all_download():
    # 获取热门链接对象
    hot = Acxiaoshuo.get_link.hot.hot()
    # 获取热门小说链接列表
    links_list = hot.get_links()
    # 创建ua类对象
    ua = Acxiaoshuo.tool.ua.Ua()
    if links_list:
        for index, i in enumerate(links_list, start=1):
            ua.set_url(i)
            h1_title = f'hot/{ua.get_h1_title()}'
            # 下载HTML并显示状态信息
            if ua.download_html(h1_title):
                print(f'第{index}个网页已经下载完成')
            # 反爬，延时2s
            time.sleep(2)
        print('全部下载完成.')


def god_all_html_download():
    # 获取大神推荐链接对象
    god = Acxiaoshuo.get_link.god.god()
    # 获取大神推荐链接列表
    link_list = god.get_links()
    # 创建ua类对象
    ua = Acxiaoshuo.tool.ua.Ua()
    if link_list:
        for index, i in enumerate(link_list, start=1):
            ua.set_url(i)
            h1_title = f'god/{ua.get_h1_title()}'
            # 下载HTML并显示状态信息
            if ua.download_html(h1_title):
                print(f'第{index}个网页已经下载完成')
            # 反爬，延时2s
            time.sleep(2)
        print('全部下载完成.')


def sort_all_html_download():
    # 获取分类链接对象
    sort_obj = Acxiaoshuo.get_link.sortvisit_link.sortvisit_link()
    # 获取分类链接列表
    links_list = sort_obj.get_links()
    # 创建ua类对象
    ua = Acxiaoshuo.tool.ua.Ua()
    if links_list:
        for index, i in enumerate(links_list, start=1):
            ua.set_url(i)
            h1_title = f'sort/{ua.get_h1_title()}'
            # 下载HTML并显示状态信息
            if ua.download_html(h1_title):
                print(f'第{index}个网页已经下载完成')
            # 反爬，延时2s
            time.sleep(2)
        print('全部下载完成.')


def newest_all_html_download():
    # 获取最新章节链接对象
    newest_obj = Acxiaoshuo.get_link.newest.newest()
    # 获取最新章节链接列表
    links_list = newest_obj.get_links()[0]
    # 创建ua类对象
    ua = Acxiaoshuo.tool.ua.Ua()
    if links_list:
        for index, i in enumerate(links_list, start=1):
            ua.set_url(i)
            h1_title = f'newest/{ua.get_h1_title()}'
            # 下载HTML并显示状态信息
            if ua.download_html(h1_title):
                print(f'第{index}个网页已经下载完成')
            # 反爬，延时2s
            time.sleep(2)
        print('全部下载完成.')


def novel_all_html_download():
    # 获取最新小说链接对象
    novel_obj = Acxiaoshuo.get_link.newest_novel.novel()
    # 获取最新小说链接列表
    links_list = novel_obj.get_links()[0]
    # 创建ua类对象
    ua = Acxiaoshuo.tool.ua.Ua()
    if links_list:
        for index, i in enumerate(links_list, start=1):
            ua.set_url(i)
            h1_title = f'novel/{ua.get_h1_title()}'
            # 下载HTML并显示状态信息
            if ua.download_html(h1_title):
                print(f'第{index}个网页已经下载完成')
            # 反爬，延时2s
            time.sleep(2)
        print('全部下载完成.')


if __name__ == '__main__':
    # 网站有更新,需要下载的时候,就将他们取消注释

    # AC小说首页
    # ua = Acxiaoshuo.tool.ua.Ua()
    # ua.download_html(ua.get_h1_title())

    # 热门小说板块 列表html文件下载
    # hot_all_download()

    # 大神小说板块 列表html文件下载
    # god_all_html_download()

    # 分类板块 列表html文件下载
    # sort_all_html_download()

    # 最新章节板块 列表html文件下载
    # newest_all_html_download()

    # 最新小说板块 列表html文件下载
    # novel_all_html_download()

    # ---------大神小说板块----------
    obj_god = Acxiaoshuo.get_link.god.god()  # 创建god对象
    obj_god.get_content()  # 调用get_content方法将数据写入excel
    obj_god.get_url_with_title()  # 调用get_url_with_title方法将数据写入excel
    obj_god_img = Acxiaoshuo.get_img.god_img.God_img()  # 创建god_img对象
    obj_god_img.input_date()  # 调用input_date方法将图片链接写入excel
    obj_god_img.download_all_img()  # 调用download_all_img方法将图片下载下来

    # # ---------热门小说板块----------
    # obj_hot = Acxiaoshuo.get_link.hot.hot()  # 创建hot对象
    # obj_hot.get_content()  # 调用get_content方法将数据写入excel
    # obj_hot.get_url_with_title()  # 调用get_url_with_title方法将数据写入excel
    # obj_hot_img = Acxiaoshuo.get_img.hot_img.Hot_img()  # 创建hot_img对象
    # obj_hot_img.input_date()  # 调用input_date方法将图片链接写入excel
    # obj_hot_img.download_all_img()  # 调用download_all_img方法将图片下载下来
    #
    # # -----------分类板块------------
    # obj_sort = Acxiaoshuo.get_link.sortvisit_link.sortvisit_link()  # 创建sort对象
    # obj_sort.get_content()  # 调用get_content方法将数据写入excel
    # obj_sort.get_url_with_title()  # 调用get_url_with_title方法将数据写入excel
    # obj_sort_img = Acxiaoshuo.get_img.sortvisit_img.Sortvisit_img()  # 创建sort_img对象
    # obj_sort_img.input_date()  # 调用input_date方法将图片链接写入excel
    # obj_sort_img.download_all_img()  # 调用download_all_img方法将图片下载下来
    #
    # # ---------最新章节板块----------
    # obj_newest = Acxiaoshuo.get_link.newest.newest()  # 创建newest对象
    # obj_newest.get_content()  # 调用get_content方法将数据写入excel
    # obj_newest.get_url_with_title()  # 调用get_url_with_title方法将数据写入excel
    # obj_newest_img = Acxiaoshuo.get_img.newest_img.Newest_img()  # 创建newest_img对象
    # obj_newest_img.input_date()  # 调用input_date方法将图片链接写入excel
    # obj_newest_img.download_all_img()  # 调用download_all_img方法将图片下载下来
    #
    # # ---------最新小说板块----------
    # obj_novel = Acxiaoshuo.get_link.newest_novel.novel()  # 创建novel对象
    # obj_novel.get_content()  # 调用get_content方法将数据写入excel
    # obj_novel.get_url_with_title()  # 调用get_url_with_title方法将数据写入excel
    # obj_novel_img = Acxiaoshuo.get_img.novel_img.Novel_img()  # 创建novel_img对象
    # obj_novel_img.input_date()  # 调用input_date方法将图片链接写入excel
    # obj_novel_img.download_all_img()  # 调用download_all_img方法将图片下载下来
