# _*_coding:utf-8
# @Time      :2023/11/26 4:04
# @Author    :DQ
# @FileName: sortvisit_img.py

import os
import time

import openpyxl

import Acxiaoshuo.tool.ua
from lxml import html


class Sortvisit_img:

    def get_srcs_with_alts(self):
        # 分析本地网页
        tf = Acxiaoshuo.tool.isTureF.Tf()
        tf.set_dir('sort/')
        title_list = tf.get_title()

        ua = Acxiaoshuo.tool.ua.Ua()
        src_list = []
        alt_list = []

        for title in title_list:
            html_content = ua.read_html('sort/', title)
            tree = html.fromstring(html_content)
            src_values = tree.xpath('/html/body/div[2]/section/div[1]/img/@src')
            alt_values = tree.xpath('/html/body/div[2]/section/div[1]/img/@alt')
            src_list.append(src_values)
            alt_list.append(alt_values)

        return src_list, alt_list

    def input_date(self):
        all_list = self.get_srcs_with_alts()
        src_list, alt_list = all_list
        file_path = 'C:/Users/86132/PycharmProjects/pythonProject/Acxiaoshuo/download/html/excel/分类数据.xlsx'
        # 打开已存在的工作簿
        wb = openpyxl.load_workbook(file_path)
        # 获取活动的工作表
        sheet = wb.active

        for index, link in enumerate(src_list, start=2):
            src_values_str = ' '.join(link)
            # 在工作表第10列添加新数据
            sheet.cell(row=index, column=10, value=src_values_str)
        # 关闭工作簿
        wb.close()
        # 保存工作簿
        wb.save(file_path)

    def download_all_img(self):
        all_list = self.get_srcs_with_alts()
        src_list, alt_list = all_list
        ua = Acxiaoshuo.tool.ua.Ua()

        for src, alt in zip(src_list, alt_list):
            ua.set_url(src[0])
            save_path = os.path.join(r'C:/Users/86132/PycharmProjects/pythonProject/Acxiaoshuo/download/html/img/sort',
                                     f'{alt[0]}.jpg')
            ua.download_img(save_path)
            time.sleep(1)
            print('下载中---')
        print('下载完成！')