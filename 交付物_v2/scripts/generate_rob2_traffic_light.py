#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROB2交通灯图生成脚本
生成符合Cochrane标准的偏倚风险评价交通灯图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_traffic_light():
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
    plt.rcParams['axes.unicode_minus'] = False

    # 研究列表（英文格式）
    studies = [
        'Wang RY 2025', 'Li XY 2025', 'Jiang HH 2024', 'Lu LY 2021',
        'Wang Q 2021', 'Chen YY 2020', 'Liang QY 2019', 'Wen CY 2018', 'Ren XX 2016'
    ]

    # ROB2评价维度
    domains = [
        'D1: Randomization\nprocess',
        'D2: Deviations from\nintended interventions', 
        'D3: Missing\noutcome data',
        'D4: Measurement\nof the outcome',
        'D5: Selection of\nthe reported result',
        'Overall'
    ]

    # 评价结果矩阵 (L=Low, S=Some concerns, H=High)
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
    symbols = {'L': '+', 'S': '!', 'H': '−'}

    fig, ax = plt.subplots(figsize=(14, 11))
    ax.set_aspect('equal')
    radius = 0.35

    for i, study in enumerate(studies):
        for j, domain in enumerate(domains):
            rating = data[i][j]
            circle = plt.Circle((j * 1.5 + 0.75, len(studies) - i - 0.5), 
                               radius, color=colors[rating], ec='white', linewidth=2)
            ax.add_patch(circle)
            ax.text(j * 1.5 + 0.75, len(studies) - i - 0.5, symbols[rating],
                   ha='center', va='center', fontsize=16, fontweight='bold',
                   color='white' if rating != 'S' else 'black')

    ax.set_xlim(-0.5, len(domains) * 1.5 + 0.5)
    ax.set_ylim(-1.8, len(studies) + 0.5)
    ax.set_xticks([j * 1.5 + 0.75 for j in range(len(domains))])
    ax.set_xticklabels(domains, fontsize=10)
    ax.set_yticks([len(studies) - i - 0.5 for i in range(len(studies))])
    ax.set_yticklabels(studies, fontsize=11)

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(length=0)

    # 图例
    legend_y = -1.2
    for idx, (color, label, symbol) in enumerate([
        ('#4CAF50', 'Low risk', '+'),
        ('#FFC107', 'Some concerns', '!'),
        ('#F44336', 'High risk', '−')
    ]):
        x_pos = 2.5 + idx * 2.5
        circle = plt.Circle((x_pos, legend_y), 0.25, color=color, ec='white', linewidth=2)
        ax.add_patch(circle)
        ax.text(x_pos, legend_y, symbol, ha='center', va='center', 
               fontsize=14, fontweight='bold',
               color='white' if color != '#FFC107' else 'black')
        ax.text(x_pos + 0.5, legend_y, label, ha='left', va='center', fontsize=11)

    ax.set_title('Risk of Bias Assessment (ROB 2.0) - Traffic Light Plot\n(Clinical RCT Studies Only)',
                fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig('../图/ROB2_交通灯图_RCT.png', dpi=300, bbox_inches='tight')
    plt.savefig('../图/ROB2_交通灯图_RCT.svg', dpi=300, bbox_inches='tight')
    print("✓ ROB2交通灯图已生成")

if __name__ == '__main__':
    generate_traffic_light()
