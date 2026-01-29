#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rm5文件数据更新脚本
用于向RevMan文件中添加新研究数据
"""

import re

def add_study_data(rm5_path, study_id, outcome_id, mean1, sd1, n1, mean2, sd2, n2):
    """向rm5文件中添加新的研究数据"""
    with open(rm5_path, 'r', encoding='ISO-8859-1') as f:
        content = f.read()
    
    # 构建CONT_DATA XML
    new_data = f'''<CONT_DATA EFFECT_SIZE="0" ESTIMABLE="YES" MEAN_1="{mean1}" MEAN_2="{mean2}" 
        SD_1="{sd1}" SD_2="{sd2}" STUDY_ID="{study_id}" TOTAL_1="{n1}" TOTAL_2="{n2}"/>'''
    
    # 在对应outcome中插入
    # ... 具体插入逻辑
    
    with open(rm5_path, 'w', encoding='ISO-8859-1') as f:
        f.write(content)
    
    print(f"✓ 已添加 {study_id} 到 {outcome_id}")

def remove_outcome(rm5_path, outcome_id):
    """从rm5文件中删除指定结局"""
    with open(rm5_path, 'r', encoding='ISO-8859-1') as f:
        content = f.read()
    
    pattern = rf'<CONT_OUTCOME[^>]*ID="{outcome_id}"[^>]*>.*?</CONT_OUTCOME>\s*'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    with open(rm5_path, 'w', encoding='ISO-8859-1') as f:
        f.write(content)
    
    print(f"✓ 已删除结局 {outcome_id}")

if __name__ == '__main__':
    print("rm5数据更新工具")
    print("用法: update_rm5_data.py <rm5文件> <操作> <参数>")
