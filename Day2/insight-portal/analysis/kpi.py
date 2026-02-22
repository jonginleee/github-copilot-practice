"""KPI 계산 로직"""
import pandas as pd
from typing import Dict, Any

def load_orders(csv_path: str) -> pd.DataFrame:
    """주문 데이터 로드 및 전처리
    
    Args:
        csv_path: CSV 파일 경로
        
    Returns:
        전처리된 DataFrame
    """
    df = pd.read_csv(csv_path)
    
    # 날짜 파싱
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # 숫자 컬럼 강제 변환
    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
    df['cost'] = pd.to_numeric(df['cost'], errors='coerce')
    
    # 필수 컬럼 결측 드롭
    df = df.dropna(subset=['order_id', 'order_date', 'revenue', 'cost'])
    
    # 선택 컬럼 결측 기본값
    df['region'] = df['region'].fillna('기타')
    df['channel'] = df['channel'].fillna('기타')
    df['is_returned'] = df['is_returned'].fillna(False)
    
    # 음수 제거
    df = df[(df['revenue'] >= 0) & (df['cost'] >= 0)]
    
    return df

def compute_kpis(df: pd.DataFrame) -> Dict[str, Any]:
    """KPI 계산
    
    Args:
        df: 주문 DataFrame
        
    Returns:
        KPI 딕셔너리
        {
            'total_revenue': float,
            'gross_profit': float,
            'gross_margin': float,
            'revenue_by_channel': dict,
            'return_rate_by_region': dict
        }
    """
    # 총 매출
    total_revenue = float(df['revenue'].sum())
    
    # 총 이익
    gross_profit = float((df['revenue'] - df['cost']).sum())
    
    # 마진율
    gross_margin = (gross_profit / total_revenue * 100) if total_revenue > 0 else 0.0
    
    # 채널별 매출
    revenue_by_channel = df.groupby('channel')['revenue'].sum().to_dict()
    revenue_by_channel = {k: float(v) for k, v in revenue_by_channel.items()}
    
    # 지역별 반품률
    return_stats = df.groupby('region').agg({
        'is_returned': ['sum', 'count']
    })
    return_rate_by_region = {}
    for region in return_stats.index:
        returned = return_stats.loc[region, ('is_returned', 'sum')]
        total = return_stats.loc[region, ('is_returned', 'count')]
        return_rate_by_region[region] = float(returned / total * 100) if total > 0 else 0.0
    
    return {
        'total_revenue': total_revenue,
        'gross_profit': gross_profit,
        'gross_margin': round(gross_margin, 2),
        'revenue_by_channel': revenue_by_channel,
        'return_rate_by_region': return_rate_by_region
    }
