"""KPI 계산 테스트"""
import pytest
import pandas as pd
from analysis.kpi import compute_kpis

@pytest.fixture
def sample_df():
    """테스트용 DataFrame"""
    data = {
        'order_id': ['ORD-001', 'ORD-002', 'ORD-003', 'ORD-004'],
        'order_date': pd.to_datetime(['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04']),
        'region': ['서울', '서울', '부산', '부산'],
        'channel': ['온라인', '모바일', '온라인', '오프라인'],
        'revenue': [100000, 200000, 150000, 80000],
        'cost': [60000, 120000, 90000, 50000],
        'is_returned': [False, False, True, False]
    }
    return pd.DataFrame(data)

def test_total_revenue(sample_df):
    """총 매출 계산 테스트"""
    kpis = compute_kpis(sample_df)
    assert kpis['total_revenue'] == 530000

def test_gross_profit(sample_df):
    """총 이익 계산 테스트"""
    kpis = compute_kpis(sample_df)
    expected_profit = (100000 - 60000) + (200000 - 120000) + (150000 - 90000) + (80000 - 50000)
    assert kpis['gross_profit'] == expected_profit

def test_gross_margin(sample_df):
    """마진율 계산 테스트"""
    kpis = compute_kpis(sample_df)
    expected_margin = (210000 / 530000) * 100
    assert abs(kpis['gross_margin'] - round(expected_margin, 2)) < 0.01

def test_revenue_by_channel(sample_df):
    """채널별 매출 테스트"""
    kpis = compute_kpis(sample_df)
    assert kpis['revenue_by_channel']['온라인'] == 250000
    assert kpis['revenue_by_channel']['모바일'] == 200000
    assert kpis['revenue_by_channel']['오프라인'] == 80000

def test_return_rate_by_region(sample_df):
    """지역별 반품률 테스트"""
    kpis = compute_kpis(sample_df)
    assert kpis['return_rate_by_region']['서울'] == 0.0  # 0/2
    assert kpis['return_rate_by_region']['부산'] == 50.0  # 1/2

def test_empty_dataframe():
    """빈 DataFrame 처리 테스트"""
    empty_df = pd.DataFrame(columns=['order_id', 'order_date', 'region', 'channel', 'revenue', 'cost', 'is_returned'])
    kpis = compute_kpis(empty_df)
    assert kpis['total_revenue'] == 0.0
    assert kpis['gross_profit'] == 0.0
