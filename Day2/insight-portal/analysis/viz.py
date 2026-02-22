"""차트 생성 모듈"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from typing import List

# 한글 폰트 설정 (Windows 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def generate_charts(df: pd.DataFrame, out_dir: str = 'reports/charts') -> List[str]:
    """차트 생성 및 저장
    
    Args:
        df: 주문 DataFrame
        out_dir: 저장 디렉토리
        
    Returns:
        저장된 파일 경로 리스트
    """
    # 출력 디렉토리 생성
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    saved_files = []
    
    # 1. 채널별 매출 (Bar Chart)
    fig, ax = plt.subplots(figsize=(10, 6))
    channel_revenue = df.groupby('channel')['revenue'].sum().sort_values(ascending=False)
    channel_revenue.plot(kind='bar', ax=ax, color='steelblue')
    ax.set_title('채널별 매출', fontsize=16, fontweight='bold')
    ax.set_xlabel('채널', fontsize=12)
    ax.set_ylabel('매출 (원)', fontsize=12)
    ax.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=0)
    
    file1 = out_path / 'revenue_by_channel.png'
    plt.savefig(file1, dpi=100, bbox_inches='tight')
    plt.close()
    saved_files.append(str(file1))
    
    # 2. 날짜별 매출 추이 (Line Chart)
    fig, ax = plt.subplots(figsize=(12, 6))
    daily_revenue = df.groupby(df['order_date'].dt.date)['revenue'].sum()
    daily_revenue.plot(ax=ax, color='coral', linewidth=2)
    ax.set_title('일별 매출 추이', fontsize=16, fontweight='bold')
    ax.set_xlabel('날짜', fontsize=12)
    ax.set_ylabel('매출 (원)', fontsize=12)
    ax.grid(alpha=0.3)
    plt.xticks(rotation=45)
    
    file2 = out_path / 'revenue_over_time.png'
    plt.savefig(file2, dpi=100, bbox_inches='tight')
    plt.close()
    saved_files.append(str(file2))
    
    print(f"✅ {len(saved_files)}개 차트 생성 완료: {out_dir}")
    return saved_files
