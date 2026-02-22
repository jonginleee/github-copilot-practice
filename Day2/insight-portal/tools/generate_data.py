"""주문 데이터 생성 스크립트"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

def generate_orders_data(n_rows: int = 1000, output_path: str = "data/orders.csv"):
    """주문 데이터 생성
    
    Args:
        n_rows: 생성할 행 수
        output_path: 저장 경로
    """
    np.random.seed(42)
    
    # 날짜 범위: 최근 6개월
    start_date = datetime.now() - timedelta(days=180)
    dates = [start_date + timedelta(days=np.random.randint(0, 180)) for _ in range(n_rows)]
    
    # 데이터 생성
    data = {
        'order_id': [f'ORD-{i:05d}' for i in range(1, n_rows + 1)],
        'order_date': dates,
        'region': np.random.choice(['서울', '경기', '부산', '대구', '기타'], n_rows, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
        'channel': np.random.choice(['온라인', '모바일', '오프라인'], n_rows, p=[0.4, 0.45, 0.15]),
        'revenue': np.random.randint(10000, 500000, n_rows),
        'cost': None,  # 나중에 계산
        'is_returned': np.random.choice([True, False], n_rows, p=[0.05, 0.95])
    }
    
    df = pd.DataFrame(data)
    
    # cost = revenue * (0.4~0.7)
    df['cost'] = (df['revenue'] * np.random.uniform(0.4, 0.7, n_rows)).astype(int)
    
    # 일부 결측값 추가 (5%)
    missing_idx = np.random.choice(df.index, size=int(n_rows * 0.05), replace=False)
    df.loc[missing_idx[:len(missing_idx)//2], 'region'] = np.nan
    df.loc[missing_idx[len(missing_idx)//2:], 'channel'] = np.nan
    
    # 저장
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"✅ {n_rows}개 주문 데이터 생성 완료: {output_path}")
    print(f"   기간: {df['order_date'].min()} ~ {df['order_date'].max()}")
    print(f"   총 매출: {df['revenue'].sum():,}원")

if __name__ == '__main__':
    generate_orders_data()
