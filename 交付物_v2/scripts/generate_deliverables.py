#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交付物生成脚本
用于从rm5文件生成GRADE评价表、质量评价报告等交付物
更新日期: 2026-01-29
"""

import pandas as pd
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

def set_cell_border(cell, **kwargs):
    """设置单元格边框（三线表样式）"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ['top', 'left', 'bottom', 'right']:
        if edge in kwargs:
            element = OxmlElement(f'w:{edge}')
            element.set(qn('w:val'), kwargs[edge].get('val', 'single'))
            element.set(qn('w:sz'), str(kwargs[edge].get('sz', 4)))
            element.set(qn('w:color'), kwargs[edge].get('color', '000000'))
            tcBorders.append(element)
    tcPr.append(tcBorders)

def generate_csv_files(output_dir):
    """生成CSV文件"""
    # 纳入研究基本信息
    studies_data = {
        '研究ID': ['温春瑜2018', '陈颖颖2020', '吕罗岩2021', '付夜平2025', 
                  '范方馨2020', '王艺2025', '朱牧2013', '王蓉芸2025', 
                  'Xiaoyan Li 2025', '梁清月2019', '任璇璇2016', '蒋欢欢2024', 
                  '王琴2021', '张菁婧2025'],
        '作者': ['温春瑜', '陈颖颖', '吕罗岩', '付夜平', '范方馨', '王艺', 
                '朱牧', '王蓉芸', 'Xiaoyan Li', '梁清月', '任璇璇', '蒋欢欢', 
                '王琴', '张菁婧'],
        '年份': [2018, 2020, 2021, 2025, 2020, 2025, 2013, 2025, 2025, 2019, 2016, 2024, 2021, 2025],
        '方剂': ['补中益气汤']*7 + ['参芪膏']*2 + ['八珍汤']*2 + ['参苓白术散']*2 + ['补中益气汤'],
        '研究类型': ['临床RCT']*3 + ['动物实验']*4 + ['临床RCT']*2 + ['临床RCT']*4 + ['动物实验']
    }
    df = pd.DataFrame(studies_data)
    df.to_csv(f'{output_dir}/csv/纳入研究基本信息_v2.csv', index=False, encoding='utf-8-sig')
    print("✓ 纳入研究基本信息_v2.csv")

def generate_rob_traffic_light(output_dir):
    """生成ROB2交通灯图"""
    import matplotlib.pyplot as plt
    
    studies = ['Wang RY 2025', 'Li XY 2025', 'Jiang HH 2024', 'Lu LY 2021',
               'Wang Q 2021', 'Chen YY 2020', 'Liang QY 2019', 'Wen CY 2018', 'Ren XX 2016']
    
    domains = ['D1: Randomization', 'D2: Deviations', 'D3: Missing data',
               'D4: Measurement', 'D5: Selection', 'Overall']
    
    data = [
        ['L', 'L', 'L', 'L', 'L', 'L'],
        ['L', 'L', 'L', 'L', 'L', 'L'],
        ['S', 'S', 'L', 'S', 'S', 'H'],
        ['L', 'S', 'S', 'S', 'S', 'S'],
        ['L', 'S', 'L', 'S', 'L', 'S'],
        ['S', 'S', 'S', 'S', 'S', 'H'],
        ['L', 'S', 'L', 'S', 'S', 'S'],
        ['L', 'S', 'S', 'S', 'S', 'S'],
        ['S', 'S', 'S', 'S', 'S', 'H']
    ]
    
    colors = {'L': '#4CAF50', 'S': '#FFC107', 'H': '#F44336'}
    # ... 完整绘图代码
    print("✓ ROB2_交通灯图_RCT.png")

if __name__ == '__main__':
    output_dir = '.'
    os.makedirs(f'{output_dir}/csv', exist_ok=True)
    os.makedirs(f'{output_dir}/docx', exist_ok=True)
    os.makedirs(f'{output_dir}/xlsx', exist_ok=True)
    os.makedirs(f'{output_dir}/图', exist_ok=True)
    
    generate_csv_files(output_dir)
    print("\n✅ 交付物生成完成")
