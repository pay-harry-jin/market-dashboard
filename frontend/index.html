<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>글로벌 시장 리스크 대시보드</title>
  <!-- TradingView Lightweight Charts (금융 차트 특화, Chart.js보다 10x 빠름) -->
  <script src="https://unpkg.com/lightweight-charts@4.1.3/dist/lightweight-charts.standalone.production.js"></script>
  <style>
    /* ══════════════════════════════════════
       DESIGN TOKENS
    ══════════════════════════════════════ */
    :root {
      --c-bg:       #0a0e17;
      --c-surface:  #111827;
      --c-surface2: #1a2235;
      --c-border:   #1e2d45;
      --c-text:     #e2e8f0;
      --c-muted:    #64748b;
      --c-up:       #22c55e;
      --c-down:     #ef4444;
      --c-blue:     #3b82f6;
      --c-yellow:   #f59e0b;
      --c-purple:   #a855f7;
      --c-orange:   #f97316;
      --c-teal:     #14b8a6;
      --c-accent:   #2563eb;
      --radius:     10px;
      --shadow:     0 1px 3px rgba(0,0,0,.4);
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: var(--c-bg);
      color: var(--c-text);
      font-family: 'Inter', 'Segoe UI', -apple-system, sans-serif;
      font-size: 14px;
      line-height: 1.5;
      min-height: 100vh;
    }

    /* ══ HEADER ════════════════════════════ */
    .header {
      background: var(--c-surface);
      border-bottom: 1px solid var(--c-border);
      padding: 0 28px;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 200;
      backdrop-filter: blur(8px);
    }
    .header-left { display: flex; align-items: center; gap: 12px; }
    .header-logo {
      width: 32px; height: 32px;
      background: linear-gradient(135deg, var(--c-accent), var(--c-purple));
      border-radius: 8px;
      display: flex; align-items: center; justify-content: center;
      font-size: 16px;
    }
    .header-title { font-size: 16px; font-weight: 700; letter-spacing: -.3px; }
    .header-title span { color: var(--c-blue); }
    .header-right { display: flex; align-items: center; gap: 12px; }
    .badge-live {
      display: flex; align-items: center; gap: 5px;
      font-size: 11px; color: var(--c-up);
      background: rgba(34,197,94,.1);
      border: 1px solid rgba(34,197,94,.25);
      border-radius: 20px; padding: 3px 10px;
    }
    .badge-live::before {
      content: '';
      width: 6px; height: 6px; border-radius: 50%;
      background: var(--c-up);
      animation: pulse 2s infinite;
    }
    @keyframes pulse {
      0%,100% { opacity:1; } 50% { opacity:.3; }
    }
    #ts { font-size: 11px; color: var(--c-muted); }
    .btn {
      background: var(--c-accent);
      color: #fff; border: none; border-radius: 6px;
      padding: 6px 14px; font-size: 12px; font-weight: 600;
      cursor: pointer; display: flex; align-items: center; gap: 6px;
      transition: background .15s;
    }
    .btn:hover { background: #1d4ed8; }
    .btn:disabled { opacity: .4; cursor: default; }
    .spin { display: inline-block; animation: spin 1s linear infinite; }
    @keyframes spin { to { transform: rotate(360deg); } }

    /* ══ MAIN LAYOUT ═══════════════════════ */
    .main {
      max-width: 1600px;
      margin: 0 auto;
      padding: 24px 28px 60px;
    }

    /* ══ SECTION HEADING ═══════════════════ */
    .sec-head {
      display: flex; align-items: center; gap: 8px;
      margin: 28px 0 14px;
    }
    .sec-head h2 {
      font-size: 11px; font-weight: 700;
      text-transform: uppercase; letter-spacing: 1.2px;
      color: var(--c-muted);
    }
    .sec-head::after {
      content: '';
      flex: 1; height: 1px;
      background: var(--c-border);
    }

    /* ══ KPI GRID ══════════════════════════ */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
      gap: 12px;
    }

    .kpi-card {
      background: var(--c-surface);
      border: 1px solid var(--c-border);
      border-radius: var(--radius);
      padding: 18px 16px 14px;
      display: flex; flex-direction: column; gap: 4px;
      transition: border-color .2s, box-shadow .2s;
      position: relative; overflow: hidden;
    }
    .kpi-card::before {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 3px;
      background: var(--kpi-color, var(--c-muted));
      border-radius: 3px 0 0 3px;
    }
    .kpi-card:hover {
      border-color: var(--kpi-color, var(--c-border));
      box-shadow: 0 0 0 1px var(--kpi-color, transparent), var(--shadow);
    }

    .kpi-name {
      font-size: 10px; font-weight: 600;
      text-transform: uppercase; letter-spacing: .8px;
      color: var(--c-muted);
    }
    .kpi-val {
      font-size: 28px; font-weight: 800;
      font-variant-numeric: tabular-nums;
      letter-spacing: -1.5px; line-height: 1;
      color: var(--c-text);
      min-height: 32px;
    }
    .kpi-chg {
      font-size: 12px; font-weight: 600;
      display: flex; align-items: center; gap: 3px;
    }
    .kpi-chg.up   { color: var(--c-up); }
    .kpi-chg.dn   { color: var(--c-down); }
    .kpi-chg.flat { color: var(--c-muted); }
    .kpi-date { font-size: 10px; color: var(--c-muted); margin-top: 2px; }

    /* skeleton */
    .skel {
      background: linear-gradient(90deg,
        var(--c-surface2) 25%,
        var(--c-border) 50%,
        var(--c-surface2) 75%);
      background-size: 200% 100%;
      animation: shim 1.5s infinite;
      border-radius: 4px;
    }
    .skel-val  { height: 30px; width: 70%; margin: 4px 0; }
    .skel-chg  { height: 14px; width: 45%; }
    @keyframes shim { to { background-position: -200% 0; } }

    /* ══ CHART GRID ════════════════════════ */
    .chart-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 16px;
    }

    .chart-card {
      background: var(--c-surface);
      border: 1px solid var(--c-border);
      border-radius: var(--radius);
      overflow: hidden;
    }
    .chart-card-header {
      display: flex; align-items: center;
      justify-content: space-between;
      padding: 14px 16px 10px;
    }
    .chart-card-info { display: flex; flex-direction: column; gap: 2px; }
    .chart-card-title { font-size: 13px; font-weight: 700; }
    .chart-card-sub   { font-size: 11px; color: var(--c-muted); }
    .chart-src-badge {
      font-size: 10px; font-weight: 600;
      padding: 2px 8px; border-radius: 20px;
    }
    .src-yahoo { background: rgba(59,130,246,.12); color: var(--c-blue); }
    .src-fred  { background: rgba(168,85,247,.12); color: var(--c-purple); }

    /* period tabs */
    .period-tabs {
      display: flex; gap: 2px;
      padding: 0 16px 10px;
    }
    .period-tab {
      font-size: 11px; font-weight: 600;
      padding: 3px 8px; border-radius: 4px;
      cursor: pointer; color: var(--c-muted);
      background: transparent; border: none;
      transition: background .15s, color .15s;
    }
    .period-tab:hover   { background: var(--c-surface2); color: var(--c-text); }
    .period-tab.active  { background: var(--c-accent); color: #fff; }

    .chart-wrap { height: 180px; }

    /* ══ ERROR STATE ═══════════════════════ */
    .err-state {
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      height: 100%; gap: 6px;
      color: var(--c-muted); font-size: 12px; padding: 16px;
      text-align: center;
    }
    .err-state .err-icon { font-size: 22px; }

    /* ══ FRED SETUP BANNER ═════════════════ */
    .setup-banner {
      background: linear-gradient(135deg, #1a1200, #1f1500);
      border: 1px solid rgba(245,158,11,.3);
      border-radius: var(--radius);
      margin: 20px 0 0;
      padding: 16px 20px;
      display: flex; align-items: center; gap: 14px;
      flex-wrap: wrap;
    }
    .setup-banner.hidden { display: none; }
    .setup-icon { font-size: 22px; flex-shrink: 0; }
    .setup-text { flex: 1; min-width: 200px; }
    .setup-text strong { color: var(--c-yellow); display: block; margin-bottom: 2px; }
    .setup-text span { font-size: 12px; color: #94730a; }
    .setup-text a { color: var(--c-yellow); }
    .setup-input {
      flex: 2; min-width: 220px;
      background: rgba(0,0,0,.3);
      border: 1px solid rgba(245,158,11,.4);
      border-radius: 6px; color: var(--c-text);
      padding: 8px 12px; font-size: 13px; outline: none;
    }
    .setup-input:focus { border-color: var(--c-yellow); }
    .setup-save {
      background: var(--c-yellow); color: #0a0e17;
      border: none; border-radius: 6px;
      padding: 8px 18px; font-size: 13px; font-weight: 700;
      cursor: pointer; white-space: nowrap;
      transition: opacity .15s;
    }
    .setup-save:hover { opacity: .85; }

    /* ══ FOOTER ════════════════════════════ */
    footer {
      text-align: center;
      padding: 20px 28px;
      border-top: 1px solid var(--c-border);
      color: var(--c-muted); font-size: 11px;
    }
    footer a { color: var(--c-blue); text-decoration: none; }
    footer a:hover { text-decoration: underline; }

    /* ══ RESPONSIVE ════════════════════════ */
    @media (max-width: 680px) {
      .header { padding: 0 16px; }
      .header-title { font-size: 14px; }
      .main { padding: 16px 16px 60px; }
      .chart-grid { grid-template-columns: 1fr; }
      .kpi-grid { grid-template-columns: repeat(2, 1fr); }
    }
  </style>
</head>
<body>

<!-- ══ HEADER ══════════════════════════════════════════ -->
<header class="header">
  <div class="header-left">
    <div class="header-logo">📊</div>
    <div class="header-title">글로벌 시장 <span>리스크 대시보드</span></div>
  </div>
  <div class="header-right">
    <span class="badge-live">LIVE</span>
    <span id="ts">로딩 중...</span>
    <button class="btn" id="refresh-btn" onclick="loadAll()">
      <span id="ri">↻</span> 새로고침
    </button>
  </div>
</header>

<!-- ══ MAIN ════════════════════════════════════════════ -->
<main class="main">

  <!-- FRED 설정 배너 -->
  <div class="setup-banner" id="setup-banner">
    <span class="setup-icon">⚠️</span>
    <div class="setup-text">
      <strong>FRED API 키 필요</strong>
      <span>국채금리·HY스프레드·Margin Debt·CPI·PCE·PPI 데이터를 보려면 무료 키가 필요합니다.
        <a href="https://fred.stlouisfed.org/docs/api/api_key.html" target="_blank">여기서 발급 →</a>
      </span>
    </div>
    <input class="setup-input" id="fred-input" type="text"
           placeholder="발급받은 FRED API Key 입력..." />
    <button class="setup-save" onclick="saveFredKey()">저장 &amp; 적용</button>
  </div>

  <!-- ── 리스크 지표 ── -->
  <div class="sec-head"><h2>리스크 지표</h2></div>
  <div class="kpi-grid" id="g-risk"></div>

  <!-- ── 주식 · 자산 시장 ── -->
  <div class="sec-head"><h2>주식 &amp; 자산 시장</h2></div>
  <div class="kpi-grid" id="g-market"></div>

  <!-- ── 거시 경제 ── -->
  <div class="sec-head"><h2>거시 경제 지표 (월별 발표)</h2></div>
  <div class="kpi-grid" id="g-macro"></div>

  <!-- ── 추이 차트 ── -->
  <div class="sec-head"><h2>추이 차트</h2></div>
  <div class="chart-grid" id="g-charts"></div>

</main>

<footer>
  데이터 소스:
  <a href="https://finance.yahoo.com" target="_blank">Yahoo Finance</a> (yfinance) &nbsp;&amp;&nbsp;
  <a href="https://fred.stlouisfed.org" target="_blank">FRED – St. Louis Fed</a>
  &nbsp;|&nbsp; 장중 1분, FRED 1시간, 거시지표 24시간 캐시
</footer>

<script>
/* ══════════════════════════════════════════════════════
   CONFIG & STATE
══════════════════════════════════════════════════════ */
const API = '';   // 같은 서버에서 서빙되므로 상대 경로

let lwCharts = {};    // id → LightweightCharts instance
let lwSeries = {};    // id → series instance

/* ══════════════════════════════════════════════════════
   FRED KEY MANAGEMENT
══════════════════════════════════════════════════════ */
function saveFredKey() {
  const v = document.getElementById('fred-input').value.trim();
  if (!v) return;
  // 서버 .env를 직접 수정할 수 없으므로 백엔드에 PATCH 요청 대신
  // 새로고침 시 URL 파라미터로 전달하거나 사용자가 .env에 직접 입력하도록 안내
  alert('서버의 .env 파일에 FRED_API_KEY=' + v + ' 를 입력한 뒤 서버를 재시작해 주세요.');
}

function initBanner() {
  // 서버가 FRED 키를 가지고 있는지는 /api/health로 확인
  fetch(API + '/api/health')
    .then(r => r.json())
    .then(() => {
      // 일단 배너 숨김 — FRED API 오류 시 개별 카드에서 표시
      document.getElementById('setup-banner').classList.add('hidden');
    })
    .catch(() => {});
}

/* ══════════════════════════════════════════════════════
   KPI CARD HELPERS
══════════════════════════════════════════════════════ */
const KPI_DEFS = {
  risk: [
    { id: 'vix',        label: 'VIX',             color: '#ef4444', src: 'yahoo', suffix: '',    dec: 2 },
    { id: 'hy_spread',  label: 'HY Spread OAS',   color: '#f97316', src: 'fred',  suffix: ' bps',dec: 0 },
    { id: 'treasury10y',label: '10년물 국채금리', color: '#3b82f6', src: 'fred',  suffix: '%',   dec: 2 },
  ],
  market: [
    { id: 'dxy',        label: '달러 인덱스',      color: '#60a5fa', src: 'yahoo', suffix: '',    dec: 3 },
    { id: 'nasdaq',     label: 'Nasdaq',           color: '#a855f7', src: 'yahoo', suffix: '',    dec: 0 },
    { id: 'russell',    label: 'Russell 2000',     color: '#22c55e', src: 'yahoo', suffix: '',    dec: 2 },
    { id: 'gold',       label: '금 (USD/oz)',      color: '#f59e0b', src: 'yahoo', suffix: '',    dec: 2 },
    { id: 'margin_debt',label: 'Margin Debt',      color: '#f43f5e', src: 'fred',  suffix: ' B$', dec: 1 },
  ],
  macro: [
    { id: 'cpi', label: 'CPI YoY', color: '#fbbf24', src: 'fred', suffix: '%', dec: 2, isYoY: true },
    { id: 'pce', label: 'PCE YoY', color: '#38bdf8', src: 'fred', suffix: '%', dec: 2, isYoY: true },
    { id: 'ppi', label: 'PPI YoY', color: '#fb923c', src: 'fred', suffix: '%', dec: 2, isYoY: true },
  ],
};

function fmt(v, dec) {
  if (v == null || isNaN(v)) return '—';
  return Number(v).toLocaleString('en-US', {
    minimumFractionDigits: dec, maximumFractionDigits: dec
  });
}

function chgHtml(chg) {
  if (chg == null) return `<span class="kpi-chg flat">—</span>`;
  const cls  = chg > 0 ? 'up' : chg < 0 ? 'dn' : 'flat';
  const arrow = chg > 0 ? '▲' : chg < 0 ? '▼' : '';
  return `<span class="kpi-chg ${cls}">${arrow} ${Math.abs(chg).toFixed(2)}%</span>`;
}

function skelHtml() {
  return `<div class="skel skel-val"></div><div class="skel skel-chg"></div>`;
}

function buildCard(def) {
  const d = document.createElement('div');
  d.className = 'kpi-card';
  d.id = 'kpi-' + def.id;
  d.style.setProperty('--kpi-color', def.color);
  d.innerHTML = `
    <div class="kpi-name">${def.label}</div>
    <div class="kpi-val" id="kv-${def.id}">${skelHtml()}</div>
    <div id="kc-${def.id}"></div>
    <div class="kpi-date" id="kd-${def.id}"></div>
  `;
  return d;
}

function fillCard(def, data) {
  const valEl  = document.getElementById('kv-' + def.id);
  const chgEl  = document.getElementById('kc-' + def.id);
  const dateEl = document.getElementById('kd-' + def.id);
  if (!valEl) return;

  if (data.error) {
    valEl.innerHTML = `<span style="font-size:13px;color:var(--c-down)">${data.error}</span>`;
    return;
  }

  // YoY 지표
  if (def.isYoY) {
    const v = data.yoy_pct;
    valEl.textContent = v != null ? fmt(v, def.dec) + def.suffix : '—';
    chgEl.innerHTML   = data.mom_pct != null
      ? `<span class="kpi-chg ${data.mom_pct>=0?'up':'dn'}" title="MoM">MoM ${data.mom_pct>=0?'▲':'▼'} ${Math.abs(data.mom_pct).toFixed(2)}%</span>`
      : '';
    if (dateEl && data.last_date) dateEl.textContent = data.last_date;
    return;
  }

  // 일반 KPI
  const curr = data.current ?? data.current_index;
  valEl.textContent = fmt(curr, def.dec) + def.suffix;
  chgEl.innerHTML   = chgHtml(data.change_pct);
  if (dateEl && data.last_date) dateEl.textContent = data.last_date;
}

function initKpiGrids() {
  ['risk','market','macro'].forEach(group => {
    const el = document.getElementById('g-' + group);
    KPI_DEFS[group].forEach(def => el.appendChild(buildCard(def)));
  });
}

/* ══════════════════════════════════════════════════════
   DATA LOADING
══════════════════════════════════════════════════════ */
async function loadYahooKpis() {
  const res = await fetch(API + '/api/yahoo/kpi');
  if (!res.ok) throw new Error('Yahoo KPI fetch failed');
  const data = await res.json();
  // data: { vix: {...}, nasdaq: {...}, ... }
  [...KPI_DEFS.risk, ...KPI_DEFS.market].forEach(def => {
    if (def.src === 'yahoo' && data[def.id]) {
      fillCard(def, data[def.id]);
    }
  });
}

async function loadFredKpis() {
  const [kpiRes, macroRes] = await Promise.all([
    fetch(API + '/api/fred/kpi'),
    fetch(API + '/api/fred/macro'),
  ]);

  if (kpiRes.ok) {
    const kpi = await kpiRes.json();
    [...KPI_DEFS.risk, ...KPI_DEFS.market].forEach(def => {
      if (def.src === 'fred' && kpi[def.id]) {
        fillCard(def, kpi[def.id]);
      }
    });
  }

  if (macroRes.ok) {
    const macro = await macroRes.json();
    KPI_DEFS.macro.forEach(def => {
      if (macro[def.id]) fillCard(def, macro[def.id]);
    });
  }
}

/* ══════════════════════════════════════════════════════
   CHARTS — TradingView Lightweight Charts
══════════════════════════════════════════════════════ */
const CHART_DEFS = [
  // Yahoo
  { id: 'ch-vix',     title: 'VIX (공포지수)',      sub: 'CBOE Volatility Index',         src: 'yahoo', key: 'vix',     color: '#ef4444' },
  { id: 'ch-nasdaq',  title: 'Nasdaq Composite',    sub: '^IXIC',                         src: 'yahoo', key: 'nasdaq',  color: '#a855f7' },
  { id: 'ch-russell', title: 'Russell 2000',        sub: '소형주 지수 ^RUT',              src: 'yahoo', key: 'russell', color: '#22c55e' },
  { id: 'ch-gold',    title: '금 선물 (USD/oz)',    sub: 'COMEX Gold GC=F',               src: 'yahoo', key: 'gold',    color: '#f59e0b' },
  { id: 'ch-dxy',     title: '달러 인덱스 (DXY)',   sub: 'US Dollar Index',               src: 'yahoo', key: 'dxy',     color: '#3b82f6' },
  // FRED
  { id: 'ch-t10y',   title: '10년물 국채금리',     sub: 'US Treasury 10Y Yield (%)',      src: 'fred',  seriesId: 'DGS10',         color: '#60a5fa' },
  { id: 'ch-hy',     title: 'HY Spread (OAS)',     sub: 'ICE BofA HY OAS (bps)',          src: 'fred',  seriesId: 'BAMLH0A0HYM2',  color: '#f97316' },
  { id: 'ch-margin', title: 'Margin Debt',         sub: 'FINRA Margin Debt (십억$)',      src: 'fred',  seriesId: 'RIWFRBSL',      color: '#f43f5e' },
  { id: 'ch-cpi',    title: 'CPI 지수',            sub: 'Consumer Price Index (월별)',    src: 'fred',  seriesId: 'CPIAUCSL',      color: '#fbbf24' },
  { id: 'ch-pce',    title: 'PCE 지수',            sub: 'PCE Price Index (월별)',         src: 'fred',  seriesId: 'PCEPI',         color: '#38bdf8' },
  { id: 'ch-ppi',    title: 'PPI 지수',            sub: 'Producer Price Index (월별)',    src: 'fred',  seriesId: 'PPIACO',        color: '#fb923c' },
];

const PERIODS_YAHOO = ['6mo','1y','2y','5y'];
const PERIODS_FRED  = ['12','24','60'];

function initChartCards() {
  const grid = document.getElementById('g-charts');
  grid.innerHTML = '';

  CHART_DEFS.forEach(def => {
    const card = document.createElement('div');
    card.className = 'chart-card';
    card.id = 'card-' + def.id;

    const badgeCls = def.src === 'yahoo' ? 'src-yahoo' : 'src-fred';
    const badgeTxt = def.src === 'yahoo' ? 'Yahoo Finance' : 'FRED';
    const periods  = def.src === 'yahoo' ? PERIODS_YAHOO : PERIODS_FRED;
    const tabsHtml = periods.map((p,i) =>
      `<button class="period-tab${i===1?' active':''}" data-period="${p}" onclick="switchPeriod('${def.id}','${p}',this)">${def.src==='yahoo'?p:p+'mo'}</button>`
    ).join('');

    card.innerHTML = `
      <div class="chart-card-header">
        <div class="chart-card-info">
          <span class="chart-card-title">${def.title}</span>
          <span class="chart-card-sub">${def.sub}</span>
        </div>
        <span class="chart-src-badge ${badgeCls}">${badgeTxt}</span>
      </div>
      <div class="period-tabs">${tabsHtml}</div>
      <div class="chart-wrap" id="${def.id}"></div>
    `;
    grid.appendChild(card);
  });
}

function createLWChart(containerId, color) {
  const container = document.getElementById(containerId);
  if (!container) return null;

  // 이전 인스턴스 제거
  if (lwCharts[containerId]) {
    lwCharts[containerId].remove();
    delete lwCharts[containerId];
    delete lwSeries[containerId];
  }

  const chart = LightweightCharts.createChart(container, {
    width:  container.clientWidth,
    height: 180,
    layout: {
      background: { color: 'transparent' },
      textColor: '#64748b',
    },
    grid: {
      vertLines: { color: '#1e2d45' },
      horzLines: { color: '#1e2d45' },
    },
    crosshair: {
      mode: LightweightCharts.CrosshairMode.Normal,
      vertLine: { color: '#3b82f6', labelBackgroundColor: '#1e40af' },
      horzLine: { color: '#3b82f6', labelBackgroundColor: '#1e40af' },
    },
    rightPriceScale: {
      borderColor: '#1e2d45',
      textColor: '#64748b',
    },
    timeScale: {
      borderColor: '#1e2d45',
      timeVisible: true,
      secondsVisible: false,
    },
    handleScroll: true,
    handleScale: true,
  });

  const series = chart.addAreaSeries({
    lineColor: color,
    topColor:    color + '44',
    bottomColor: color + '08',
    lineWidth: 2,
    crosshairMarkerVisible: true,
    crosshairMarkerRadius: 4,
    crosshairMarkerBorderColor: color,
    crosshairMarkerBackgroundColor: '#0a0e17',
    lastValueVisible: true,
    priceLineVisible: true,
    priceLineColor: color + '80',
  });

  lwCharts[containerId] = chart;
  lwSeries[containerId] = series;

  // 리사이즈 대응
  const ro = new ResizeObserver(() => {
    if (lwCharts[containerId]) {
      lwCharts[containerId].applyOptions({ width: container.clientWidth });
    }
  });
  ro.observe(container);

  return { chart, series };
}

function setChartData(containerId, rawData) {
  const series = lwSeries[containerId];
  if (!series) return;

  const points = rawData
    .filter(p => p.value != null)
    .map(p => ({ time: p.date, value: p.value }))
    .sort((a, b) => a.time < b.time ? -1 : 1);

  series.setData(points);
  lwCharts[containerId]?.timeScale().fitContent();
}

function showChartError(containerId, msg) {
  const el = document.getElementById(containerId);
  if (!el) return;
  if (lwCharts[containerId]) {
    lwCharts[containerId].remove();
    delete lwCharts[containerId];
    delete lwSeries[containerId];
  }
  el.innerHTML = `
    <div class="err-state">
      <span class="err-icon">⚠</span>
      <span>${msg}</span>
    </div>`;
}

async function loadChart(def, period) {
  createLWChart(def.id, def.color);

  try {
    let history;
    if (def.src === 'yahoo') {
      const res = await fetch(`${API}/api/yahoo/history/${def.key}?period=${period}`);
      if (!res.ok) throw new Error(await res.text());
      const data = await res.json();
      history = data.history;
    } else {
      const months = parseInt(period) || 24;
      const res = await fetch(`${API}/api/fred/history/${def.seriesId}?months=${months}`);
      if (!res.ok) throw new Error(await res.text());
      const data = await res.json();
      history = data.history;
      // RIWFRBSL (Margin Debt) 단위 변환: 달러 → 십억달러
      if (def.seriesId === 'RIWFRBSL') {
        history = history.map(p => ({ ...p, value: p.value / 1e9 }));
      }
    }
    setChartData(def.id, history);
  } catch (e) {
    showChartError(def.id, e.message || '데이터 로딩 실패');
  }
}

function switchPeriod(chartId, period, tabEl) {
  // 탭 활성화
  const tabs = tabEl.closest('.period-tabs').querySelectorAll('.period-tab');
  tabs.forEach(t => t.classList.remove('active'));
  tabEl.classList.add('active');

  const def = CHART_DEFS.find(d => d.id === chartId);
  if (def) loadChart(def, period);
}

async function loadAllCharts() {
  // 기본 period: yahoo=1y, fred=24mo
  await Promise.allSettled(
    CHART_DEFS.map(def => {
      const defaultPeriod = def.src === 'yahoo' ? '1y' : '24';
      return loadChart(def, defaultPeriod);
    })
  );
}

/* ══════════════════════════════════════════════════════
   MAIN LOAD
══════════════════════════════════════════════════════ */
function setLoading(on) {
  const btn = document.getElementById('refresh-btn');
  const ri  = document.getElementById('ri');
  btn.disabled = on;
  ri.className = on ? 'spin' : '';
}

async function loadAll() {
  setLoading(true);
  try {
    await Promise.allSettled([
      loadYahooKpis(),
      loadFredKpis(),
    ]);
    await loadAllCharts();
    document.getElementById('ts').textContent =
      '업데이트: ' + new Date().toLocaleString('ko-KR', {
        month:'2-digit', day:'2-digit',
        hour:'2-digit', minute:'2-digit'
      });
  } finally {
    setLoading(false);
  }
}

/* ══════════════════════════════════════════════════════
   BOOT
══════════════════════════════════════════════════════ */
initBanner();
initKpiGrids();
initChartCards();
loadAll();

// 5분마다 자동 새로고침
setInterval(loadAll, 5 * 60 * 1000);
</script>
</body>
</html>
