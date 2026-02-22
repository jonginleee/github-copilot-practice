"""KPI/차트 API"""
from fastapi import APIRouter, HTTPException
from pathlib import Path
from analysis.kpi import load_orders, compute_kpis
from analysis.viz import generate_charts

router = APIRouter(prefix="/api", tags=["metrics"])

@router.get("/kpis")
def get_kpis():
    """KPI 데이터 조회"""
    try:
        df = load_orders('data/orders.csv')
        kpis = compute_kpis(df)
        return {"ok": True, "data": kpis}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"ok": False, "error": str(e)})

@router.get("/charts")
def get_charts():
    """차트 목록 조회"""
    try:
        charts_dir = Path('reports/charts')
        if not charts_dir.exists():
            # 차트 생성
            df = load_orders('data/orders.csv')
            generate_charts(df)
        
        chart_files = [f.name for f in charts_dir.glob('*.png')]
        return {"ok": True, "charts": chart_files}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"ok": False, "error": str(e)})
