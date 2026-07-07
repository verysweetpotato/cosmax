import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="포뮬로그 FormuLog | 처방 변경 이력 관리",
    layout="wide",
)

# HTML을 별도 파일로 분리하지 않고 app.py 안에 직접 포함해 관리합니다.
HTML_CONTENT = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>포뮬로그 FormuLog | 처방 변경 이력 관리</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>
  :root{
    /* 메인 네이비 스케일 (--navy-700이 지정된 메인 컬러 #1B3A5C) */
    --navy-900:#0f2438;
    --navy-800:#152f4a;
    --navy-700:#1B3A5C;
    --navy-600:#2c5478;
    --navy-500:#3f6690;
    --navy-100:#e6ecf2;
    --navy-50:#eef2f6;
    --white:#ffffff;
    --card-bg:#F5F6F8;
    --border:#dde2e8;
    --text-main:#1c2733;
    --text-sub:#647085;
    /* 소프트 골드 (버튼 강조색) */
    --gold:#C9A66B;
    --gold-dark:#b8934f;
    --gold-text:#152f4a;
    --danger:#c0392b;
    --danger-bg:#fdeceb;
    --success:#1e7d4f;
    --success-bg:#e8f7ef;
    --new:#1a5fb4;
    --new-bg:#e7f1fd;
    --removed:#8a8f98;
    --removed-bg:#f0f1f3;
    --shadow: 0 4px 16px rgba(15,36,56,0.06);
    --shadow-lg: 0 12px 32px rgba(15,36,56,0.14);
    --radius: 14px;
  }
  *{box-sizing:border-box;}
  body{
    margin:0;
    font-family:"Noto Sans KR","Malgun Gothic","Segoe UI",sans-serif;
    font-size:15px;
    background:var(--navy-50);
    color:var(--text-main);
    line-height:1.6;
  }

  /* Header */
  header{
    background:linear-gradient(135deg, var(--navy-900), var(--navy-700));
    color:var(--white);
    padding:20px 28px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:16px;
    box-shadow:var(--shadow);
    position:sticky;
    top:0;
    z-index:50;
  }
  .brand{
    display:flex;
    align-items:center;
    gap:12px;
    min-width:0;
    flex:1 1 auto;
  }
  .brand-logo{
    width:38px;height:38px;
    flex-shrink:0;
    border-radius:10px;
    background:var(--white);
    color:var(--navy-800);
    display:flex;align-items:center;justify-content:center;
    font-weight:800;
    font-size:16px;
  }
  .brand-text{
    min-width:0;
  }
  .brand-text h1{
    font-size:24px;
    font-weight:800;
    margin:0;
    letter-spacing:0.2px;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
  }
  header .user-badge{
    font-size:13.5px;
    background:rgba(255,255,255,0.1);
    padding:8px 14px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.2);
    white-space:nowrap;
    flex-shrink:0;
  }

  main{
    max-width:1440px;
    margin:0 auto;
    padding:48px 32px 60px;
  }

  .page-title{
    margin:8px 0 22px;
  }
  .page-title h2{
    font-size:26px;
    font-weight:800;
    margin:0 0 6px;
    color:var(--navy-900);
  }
  .page-title p{
    margin:0;
    color:var(--text-sub);
    font-size:14.5px;
  }

  .layout{
    display:grid;
    grid-template-columns:repeat(3, 1fr);
    gap:36px;
    align-items:start;
  }
  .layout > section:first-child{ grid-column:span 2; }
  .layout > section:last-child{ grid-column:span 1; }

  .card{
    background:var(--card-bg);
    border:1px solid var(--border);
    border-radius:var(--radius);
    box-shadow:var(--shadow);
    padding:22px;
  }
  .card h3{
    margin:0 0 4px;
    font-size:18px;
    font-weight:800;
    color:var(--navy-900);
  }
  .card .sub{
    margin:0 0 16px;
    font-size:13.5px;
    color:var(--text-sub);
  }

  /* Formula list */
  .toolbar{
    display:flex;
    gap:10px;
    margin-bottom:16px;
    flex-wrap:wrap;
  }
  .search-input{
    flex:1;
    min-width:160px;
    padding:10px 14px;
    border-radius:10px;
    border:1px solid var(--border);
    font-size:15px;
    background:var(--navy-50);
  }
  .search-input:focus{
    outline:none;
    border-color:var(--navy-500);
    background:var(--white);
  }

  .table-scroll{
    width:100%;
    overflow-x:auto;
    -webkit-overflow-scrolling:touch;
  }

  table{
    width:100%;
    border-collapse:collapse;
    font-size:14.5px;
  }
  thead th{
    text-align:left;
    padding:10px 8px;
    color:var(--text-sub);
    font-weight:700;
    font-size:12.5px;
    letter-spacing:0.3px;
    border-bottom:2px solid var(--navy-100);
    white-space:nowrap;
  }
  tbody td{
    padding:12px 8px;
    border-bottom:1px solid var(--border);
    vertical-align:middle;
  }
  tbody tr:hover{
    background:var(--navy-50);
  }
  .formula-row{
    cursor:pointer;
  }
  .select-cell{
    width:28px;
  }
  .select-cell input{
    width:16px;height:16px;
    accent-color:var(--navy-700);
    cursor:pointer;
  }
  .product-cell{
    font-weight:700;
    font-size:13.5px;
    color:var(--navy-600);
  }
  .manager-mobile{
    display:none;
  }
  .formula-name{
    font-weight:700;
    color:var(--navy-900);
  }
  .formula-id{
    font-size:12px;
    color:var(--text-sub);
    display:block;
    margin-top:2px;
  }
  .version-badge{
    display:inline-block;
    background:var(--navy-100);
    color:var(--navy-700);
    font-weight:700;
    font-size:12.5px;
    padding:4px 10px;
    border-radius:20px;
  }
  .date-cell{
    color:var(--text-sub);
    font-size:13.5px;
  }
  .manager-cell{
    color:var(--text-main);
    font-size:13.5px;
  }

  .compare-bar{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:12px;
    margin-top:18px;
    padding-top:16px;
    border-top:1px dashed var(--border);
    flex-wrap:wrap;
  }
  .compare-status{
    font-size:13.5px;
    color:var(--text-sub);
  }
  .compare-status b{
    color:var(--navy-800);
  }

  /* 샘플 처방 카드 */
  .sample-section{
    margin-top:36px;
  }
  .sample-grid{
    display:grid;
    grid-template-columns:repeat(auto-fill, minmax(220px, 1fr));
    gap:16px;
    margin-top:4px;
  }
  .sample-card{
    background:var(--white);
    border:1px solid var(--border);
    border-radius:12px;
    padding:16px;
    cursor:pointer;
    transition:transform 0.15s ease, box-shadow 0.15s ease;
  }
  .sample-card:hover{
    transform:translateY(-3px);
    box-shadow:var(--shadow-lg);
  }
  .sample-card-title{
    margin:0 0 6px;
    font-size:15px;
    font-weight:800;
    color:var(--navy-900);
  }
  .sample-card-desc{
    margin:0 0 12px;
    font-size:13px;
    color:var(--text-sub);
  }
  .sample-card-tags{
    display:flex;
    gap:6px;
    flex-wrap:wrap;
  }
  .chip{
    display:inline-block;
    font-size:11.5px;
    font-weight:700;
    padding:3px 10px;
    border-radius:20px;
  }
  .chip-category{
    background:var(--navy-100);
    color:var(--navy-700);
  }
  .chip-version{
    background:var(--gold);
    color:var(--gold-text);
  }
  .custom-tags{
    display:flex;
    flex-wrap:wrap;
    gap:6px;
    margin-top:8px;
  }
  .chip-custom{
    display:inline-flex;
    align-items:center;
    gap:4px;
    font-size:11.5px;
    font-weight:700;
    padding:3px 6px 3px 10px;
    border-radius:20px;
    background:transparent;
    border:1px solid var(--navy-500);
    color:var(--navy-600);
  }
  .tag-remove{
    background:transparent;
    color:var(--navy-500);
    font-size:13px;
    line-height:1;
    padding:2px;
    border-radius:50%;
  }
  .tag-remove:hover{
    background:var(--navy-100);
    color:var(--danger);
  }
  .tag-add-row{
    display:flex;
    gap:6px;
    margin-top:8px;
  }
  .tag-input{
    flex:1;
    min-width:0;
    padding:6px 10px;
    border-radius:20px;
    border:1px solid var(--border);
    font-size:12.5px;
    background:var(--navy-50);
  }
  .tag-input:focus{
    outline:none;
    border-color:var(--navy-500);
    background:var(--white);
  }
  .tag-add-btn{
    background:var(--navy-100);
    color:var(--navy-700);
    padding:6px 12px;
    border-radius:20px;
    font-size:12px;
    font-weight:700;
  }
  .tag-add-btn:hover{
    background:#dde7f5;
  }
  .sample-card-toggle{
    display:flex;
    align-items:center;
    gap:4px;
    margin-top:12px;
    font-size:12px;
    font-weight:700;
    color:var(--navy-600);
  }
  .sample-card-toggle .toggle-icon{
    display:inline-block;
    transition:transform 0.15s ease;
  }
  .sample-card.expanded .sample-card-toggle .toggle-icon{
    transform:rotate(180deg);
  }
  .sample-card-ingredients{
    display:none;
    margin-top:12px;
    padding-top:12px;
    border-top:1px dashed var(--border);
  }
  .sample-card.expanded .sample-card-ingredients{
    display:block;
  }
  .ingredients-title{
    margin:0 0 8px;
    font-size:12px;
    font-weight:700;
    color:var(--navy-700);
  }
  .ingredient-list{
    list-style:none;
    margin:0;
    padding:0;
    display:flex;
    flex-direction:column;
    gap:6px;
  }
  .ingredient-list li{
    display:flex;
    justify-content:space-between;
    gap:8px;
    font-size:12.5px;
    color:var(--text-main);
  }
  .ingredient-list li span:last-child{
    font-weight:700;
    color:var(--navy-700);
  }

  /* 배합량 계산기 */
  .calc-result{
    margin-top:16px;
    padding:16px;
    border-radius:10px;
    background:var(--navy-50);
    border:1px solid var(--border);
  }
  .calc-placeholder{
    margin:0;
    font-size:13px;
    color:var(--text-sub);
    text-align:center;
  }
  .calc-loading{
    margin:0;
    font-size:13.5px;
    font-weight:600;
    color:var(--navy-600);
    text-align:center;
  }
  .calc-result-title{
    margin:0 0 10px;
    font-size:13px;
    font-weight:700;
    color:var(--navy-700);
  }
  .calc-total{
    display:flex;
    justify-content:space-between;
    margin-top:10px;
    padding-top:10px;
    border-top:1px solid var(--border);
    font-size:13.5px;
    font-weight:800;
    color:var(--navy-900);
  }

  button{
    font-family:inherit;
    cursor:pointer;
    border:none;
  }
  .btn-primary{
    background:var(--gold);
    color:var(--gold-text);
    padding:11px 22px;
    border-radius:10px;
    font-size:14.5px;
    font-weight:700;
    transition:background 0.15s, transform 0.1s;
  }
  .btn-primary:hover{ background:var(--gold-dark); }
  .btn-primary:active{ transform:scale(0.98); }
  .btn-primary:disabled{
    background:#d8dbe0;
    color:#8a8f98;
    cursor:not-allowed;
  }
  .btn-secondary{
    background:var(--navy-100);
    color:var(--navy-800);
    padding:11px 20px;
    border-radius:10px;
    font-size:14.5px;
    font-weight:600;
  }
  .btn-secondary:hover{ background:#dde7f5; }
  .btn-ghost{
    background:transparent;
    color:var(--navy-600);
    padding:8px 10px;
    font-size:13px;
    font-weight:600;
    border-radius:8px;
  }
  .btn-ghost:hover{ background:var(--navy-50); }
  .action-cell{
    white-space:nowrap;
  }
  .icon-btn{
    padding:6px 10px;
    border-radius:8px;
    font-size:12.5px;
    font-weight:700;
    margin-right:6px;
  }
  .icon-btn.edit{ background:var(--navy-100); color:var(--navy-700); }
  .icon-btn.edit:hover{ background:#dde7f5; }
  .icon-btn.delete{ background:var(--danger-bg); color:var(--danger); }
  .icon-btn.delete:hover{ background:#fbdbd8; }

  /* New formula form */
  .field{
    margin-bottom:14px;
  }
  .field label{
    display:block;
    font-size:13px;
    font-weight:700;
    color:var(--navy-800);
    margin-bottom:6px;
  }
  .field input,
  .field select{
    width:100%;
    padding:10px 12px;
    border-radius:9px;
    border:1px solid var(--border);
    font-size:15px;
    background:var(--navy-50);
    font-family:inherit;
    color:var(--text-main);
  }
  .field input:focus,
  .field select:focus{
    outline:none;
    border-color:var(--navy-500);
    background:var(--white);
  }
  .ingredient-row{
    display:grid;
    grid-template-columns:1.4fr 0.8fr auto;
    gap:8px;
    margin-bottom:8px;
  }
  .ingredient-row input{
    padding:9px 10px;
    border-radius:8px;
    border:1px solid var(--border);
    font-size:14.5px;
    background:var(--navy-50);
    width:100%;
  }
  .ingredient-row input:focus{
    outline:none;
    border-color:var(--navy-500);
    background:var(--white);
  }
  .remove-row{
    background:var(--danger-bg);
    color:var(--danger);
    border-radius:8px;
    width:34px;
    font-size:15px;
    font-weight:700;
  }
  .add-row-btn{
    width:100%;
    background:var(--navy-50);
    border:1px dashed var(--navy-500);
    color:var(--navy-700);
    padding:9px;
    border-radius:9px;
    font-size:13px;
    font-weight:700;
    margin-bottom:16px;
  }
  .add-row-btn:hover{ background:var(--navy-100); }

  .ratio-hint{
    font-size:12px;
    color:var(--text-sub);
    margin:-6px 0 14px;
  }
  .ratio-hint.warn{ color:var(--danger); font-weight:600; }

  /* Comparison Modal */
  .modal-overlay{
    position:fixed;
    inset:0;
    background:rgba(11,27,51,0.55);
    display:none;
    align-items:flex-start;
    justify-content:center;
    padding:40px 16px;
    overflow-y:auto;
    z-index:100;
  }
  .modal-overlay.open{ display:flex; }
  .modal{
    background:var(--card-bg);
    border-radius:16px;
    max-width:760px;
    width:100%;
    box-shadow:var(--shadow-lg);
    overflow:hidden;
  }
  .modal-header{
    background:var(--navy-900);
    color:var(--white);
    padding:20px 24px;
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
  }
  .modal-header h3{
    margin:0 0 4px;
    font-size:19px;
    font-weight:800;
  }
  .modal-header .versus{
    font-size:13px;
    color:#b9c8e0;
  }
  .modal-close{
    background:rgba(255,255,255,0.12);
    color:var(--white);
    width:30px;height:30px;
    border-radius:50%;
    font-size:15px;
    line-height:1;
  }
  .modal-close:hover{ background:rgba(255,255,255,0.24); }
  .modal-body{
    padding:20px 24px 24px;
  }
  .legend{
    display:flex;
    gap:16px;
    flex-wrap:wrap;
    margin-bottom:16px;
    font-size:12.5px;
    color:var(--text-sub);
  }
  .legend span{
    display:inline-flex;
    align-items:center;
    gap:6px;
  }
  .dot{
    width:10px;height:10px;
    border-radius:50%;
    display:inline-block;
  }
  .dot.changed{ background:var(--danger); }
  .dot.new{ background:var(--new); }
  .dot.removed{ background:var(--removed); }

  .compare-table{
    width:100%;
    border-collapse:collapse;
    font-size:14.5px;
  }
  .compare-table th{
    text-align:left;
    padding:9px 10px;
    background:var(--navy-50);
    color:var(--text-sub);
    font-size:12.5px;
    letter-spacing:0.3px;
  }
  .compare-table td{
    padding:11px 10px;
    border-bottom:1px solid var(--border);
  }
  .row-changed{ background:var(--danger-bg); }
  .row-new{ background:var(--new-bg); }
  .row-removed{ background:var(--removed-bg); }
  .tag{
    font-size:11.5px;
    font-weight:700;
    padding:3px 9px;
    border-radius:20px;
    display:inline-block;
  }
  .tag.changed{ background:var(--danger); color:var(--white); }
  .tag.new{ background:var(--new); color:var(--white); }
  .tag.removed{ background:var(--removed); color:var(--white); }
  .tag.same{ background:var(--navy-100); color:var(--navy-700); }
  .diff-value{
    font-weight:700;
  }
  .diff-value.up{ color:var(--danger); }
  .diff-value.down{ color:var(--new); }
  .strike{ text-decoration:line-through; color:var(--text-sub); }

  .empty-msg{
    text-align:center;
    color:var(--text-sub);
    font-size:13.5px;
    padding:24px 0;
  }
  .empty-msg img{
    display:block;
    width:120px;
    margin:0 auto 12px;
  }

  .toast{
    position:fixed;
    bottom:26px;
    left:50%;
    transform:translateX(-50%) translateY(20px);
    background:var(--navy-900);
    color:var(--white);
    padding:12px 20px;
    border-radius:10px;
    font-size:14px;
    box-shadow:var(--shadow-lg);
    opacity:0;
    pointer-events:none;
    transition:all 0.25s ease;
    z-index:200;
  }
  .toast.show{
    opacity:1;
    transform:translateX(-50%) translateY(0);
  }

  /* ---- 반응형: PC(3열, 기본) > 태블릿(2열) > 모바일(1열) ---- */
  @media (max-width: 1024px){
    /* 태블릿: 2열 */
    .layout{ grid-template-columns:repeat(2, 1fr); }
    .layout > section:first-child, .layout > section:last-child{ grid-column:span 1; }
  }
  @media (max-width: 768px){
    /* 모바일: 1열, 카드가 화면 밖으로 깨지지 않도록 스택 */
    .layout{ grid-template-columns:1fr; }
    /* 처방목록/신규등록 카드를 샘플 카드 수준 너비로 좁혀서 중앙 정렬 */
    .layout > section{
      max-width:340px;
      width:100%;
      margin-left:auto;
      margin-right:auto;
    }

    body{ font-size:16px; }
    header{ padding:14px 16px; gap:10px; }
    .brand{ gap:8px; }
    .brand-logo{ width:32px; height:32px; font-size:14px; }
    header .user-badge{ padding:7px 10px; font-size:12px; }
    .brand-text h1{ font-size:19px; }
    .page-title h2{ font-size:21px; }
    .card h3{ font-size:16.5px; }
    main{ padding:28px 12px 40px; }
    .layout{ gap:18px; }
    .card{ padding:14px; }
    .card h3{ margin:0 0 3px; }
    .card .sub{ margin:0 0 10px; }
    .toolbar{ margin-bottom:10px; gap:8px; }
    .field{ margin-bottom:10px; }
    table{ font-size:14px; }
    tbody td{ padding:8px 6px; }
    /* 모바일에서는 제품명(담당자는 그 아래 표시)·작업만 노출, 처방명·담당자·버전·수정일자 컬럼은 숨김 (선택 체크박스는 버전 비교를 위해 유지) */
    thead th:nth-child(3), tbody td:nth-child(3),
    thead th:nth-child(4), tbody td:nth-child(4),
    thead th:nth-child(5), tbody td:nth-child(5),
    thead th:nth-child(6), tbody td:nth-child(6){ display:none; }
    .manager-mobile{
      display:block;
      font-size:12px;
      font-weight:500;
      color:var(--text-sub);
      margin-top:2px;
    }
    .table-scroll table{ min-width:220px; } /* 제품명+작업만 남아 폭이 좁아짐 */
    .ingredient-row{ grid-template-columns:1fr 1fr auto; margin-bottom:6px; }
    .compare-bar{ flex-direction:column; align-items:stretch; margin-top:12px; padding-top:10px; }
    .compare-bar button{ width:100%; }
    .modal-body{ padding:16px; }
    .compare-table{ font-size:13.5px; }
    .table-scroll .compare-table{ min-width:480px; }
    /* iOS Safari가 16px 미만 입력창에 자동 확대(zoom)를 거는 것을 방지 */
    input, select, textarea{ font-size:16px; }

    /* 손가락으로 탭하기 쉬운 최소 44px 탭 영역 */
    .btn-primary, .btn-secondary{ min-height:44px; }
    .action-cell{ display:flex; flex-direction:column; gap:8px; }
    .icon-btn{
      display:flex;
      align-items:center;
      justify-content:center;
      width:100%;
      min-height:44px;
      margin-right:0;
      font-size:13.5px;
    }
    .modal-close{ width:44px; height:44px; font-size:18px; }
    .remove-row{ width:44px; min-height:44px; }
    .add-row-btn{ min-height:44px; margin-bottom:10px; }
    .ratio-hint{ margin:-4px 0 10px; }
    .select-cell{ width:auto; }
    .select-cell input{ width:20px; height:20px; padding:10px; }
  }
</style>
</head>
<body>

<header>
  <div class="brand">
    <div class="brand-logo">FL</div>
    <div class="brand-text">
      <h1>포뮬로그 FormuLog</h1>
    </div>
  </div>
  <div class="user-badge">Login</div>
</header>

<main>
  <div class="page-title">
    <h2>처방 변경 이력 관리</h2>
    <p>처방별 버전 이력을 확인하고, 두 버전 간 원료·비율 변경 사항을 한눈에 비교하세요.</p>
  </div>

  <div class="layout">
    <!-- 처방 목록 -->
    <section class="card">
      <h3>처방 목록 &amp; 버전 이력</h3>
      <p class="sub">비교할 두 개의 버전 행에 체크한 뒤 [버전 비교] 버튼을 누르세요.</p>

      <div class="toolbar">
        <input type="text" id="searchInput" class="search-input" placeholder="제품명, 처방명으로 검색 후 Enter">
      </div>

      <div class="table-scroll">
        <table>
          <thead>
            <tr>
              <th class="select-cell"></th>
              <th>제품명</th>
              <th>처방명</th>
              <th>담당자</th>
              <th>버전</th>
              <th>수정일자</th>
              <th>작업</th>
            </tr>
          </thead>
          <tbody id="formulaTableBody">
            <!-- JS로 렌더링 -->
          </tbody>
        </table>
      </div>

      <div class="compare-bar">
        <div class="compare-status" id="compareStatus">비교할 버전을 2개 선택하세요 (<b>0/2</b> 선택됨)</div>
        <button class="btn-primary" id="compareBtn" disabled>버전 비교</button>
      </div>
    </section>

    <!-- 신규 처방 등록 -->
    <section class="card">
      <h3>신규 처방 등록</h3>
      <p class="sub">원료명과 비율, 담당자를 입력해 새 버전을 기록합니다.</p>

      <div class="field">
        <label for="newProductName">제품명</label>
        <input type="text" id="newProductName" placeholder="예: 모이스처 크림 200ml">
      </div>
      <div class="field">
        <label for="newFormulaName">처방명</label>
        <input type="text" id="newFormulaName" placeholder="예: 수분크림 리뉴얼 v2">
      </div>
      <div class="field">
        <label for="newManager">담당자</label>
        <input type="text" id="newManager" placeholder="예: R-1042">
      </div>

      <label style="display:block;font-size:12.5px;font-weight:600;color:var(--navy-800);margin-bottom:6px;">원료 구성</label>
      <div id="ingredientList">
        <div class="ingredient-row">
          <input type="text" class="ing-name" placeholder="원료명">
          <input type="number" class="ing-ratio" placeholder="비율(%)" step="0.1">
          <button class="remove-row" type="button" onclick="removeIngredientRow(this)">×</button>
        </div>
      </div>
      <button type="button" class="add-row-btn" id="addRowBtn">+ 원료 추가</button>
      <p class="ratio-hint" id="ratioHint">전체 비율 합계: 0%</p>

      <button class="btn-primary" style="width:100%;" id="registerBtn">신규 처방 등록</button>
    </section>
  </div>

  <section class="card sample-section">
    <h3>샘플 처방 카드</h3>
    <p class="sub">등록된 처방을 카드 형태로 한눈에 확인하세요.</p>
    <div class="toolbar">
      <select id="categoryFilter" class="search-input">
        <option value="">전체보기</option>
      </select>
    </div>
    <div class="sample-grid" id="sampleGrid">
      <!-- JS로 렌더링 -->
    </div>
  </section>

  <section class="card sample-section">
    <h3>배합량 계산기</h3>
    <p class="sub">처방과 배치 용량을 입력하면, 최신 버전 비율 기준으로 각 원료의 실제 투입량(g)을 계산합니다.</p>

    <div class="field">
      <label for="calcFormulaSelect">처방 선택</label>
      <select id="calcFormulaSelect"></select>
    </div>
    <div class="field">
      <label for="calcBatchAmount">배치 용량 (g)</label>
      <input type="number" id="calcBatchAmount" placeholder="예: 500" min="0" step="0.1">
    </div>
    <button class="btn-primary" id="calcConfirmBtn">확인</button>

    <div class="calc-result" id="calcResult">
      <p class="calc-placeholder">처방과 배치 용량을 입력하고 확인을 누르면 결과가 표시됩니다.</p>
    </div>
  </section>
</main>

<!-- 버전 비교 모달 -->
<div class="modal-overlay" id="modalOverlay">
  <div class="modal">
    <div class="modal-header">
      <div>
        <h3 id="modalTitle">버전 비교</h3>
        <div class="versus" id="modalVersus"></div>
      </div>
      <button class="modal-close" id="modalCloseBtn">×</button>
    </div>
    <div class="modal-body">
      <div class="legend">
        <span><span class="dot changed"></span>변경 (±1% 이상)</span>
        <span><span class="dot new"></span>신규 항목</span>
        <span><span class="dot removed"></span>삭제 항목</span>
      </div>
      <div class="table-scroll">
        <table class="compare-table" id="compareTable">
          <thead>
            <tr>
              <th>원료명</th>
              <th>이전 버전</th>
              <th>선택 버전</th>
              <th>변화량</th>
              <th>구분</th>
            </tr>
          </thead>
          <tbody id="compareTableBody"></tbody>
        </table>
      </div>
    </div>
  </div>
</div>

<!-- 원료 구성 보기 팝업 -->
<div class="modal-overlay" id="ingredientModalOverlay">
  <div class="modal" style="max-width:420px;">
    <div class="modal-header">
      <div>
        <h3 id="ingredientModalTitle">원료 구성</h3>
        <div class="versus" id="ingredientModalVersus"></div>
      </div>
      <button class="modal-close" id="ingredientModalCloseBtn">×</button>
    </div>
    <div class="modal-body">
      <ul class="ingredient-list" id="ingredientModalList"></ul>
    </div>
  </div>
</div>

<!-- 처방/버전 수정 모달 -->
<div class="modal-overlay" id="editModalOverlay">
  <div class="modal">
    <div class="modal-header">
      <div>
        <h3 id="editModalTitle">처방 수정</h3>
        <div class="versus" id="editModalVersus"></div>
      </div>
      <button class="modal-close" id="editModalCloseBtn">×</button>
    </div>
    <div class="modal-body">
      <div class="field">
        <label for="editProductName">제품명</label>
        <input type="text" id="editProductName" placeholder="예: 모이스처 크림 200ml">
      </div>
      <div class="field">
        <label for="editFormulaName">처방명</label>
        <input type="text" id="editFormulaName" placeholder="예: 수분크림 리뉴얼 v2">
      </div>
      <div class="field">
        <label for="editManager">담당자</label>
        <input type="text" id="editManager" placeholder="예: R-1042">
      </div>

      <label style="display:block;font-size:12.5px;font-weight:600;color:var(--navy-800);margin-bottom:6px;">원료 구성</label>
      <div id="editIngredientList"></div>
      <button type="button" class="add-row-btn" id="editAddRowBtn">+ 원료 추가</button>
      <p class="ratio-hint" id="editRatioHint">전체 비율 합계: 0%</p>

      <button class="btn-primary" style="width:100%;" id="editSaveBtn">저장</button>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
  // ---------- 데모 데이터 ----------
  // 각 처방은 여러 버전을 가지며, 각 버전은 원료 구성(원료명 -> 비율)을 갖는다.
  let formulas = [
    {
      id: "F-001",
      product: "모이스처 크림 200ml",
      category: "스킨케어",
      name: "수분크림 베이스",
      manager: "R-1042",
      tags: ["저자극"],
      versions: [
        { version: "v1.0", date: "2026-04-02", ingredients: { "정제수": 60, "글리세린": 8, "히알루론산": 1.5, "세테아릴알코올": 4 } },
        { version: "v1.1", date: "2026-05-10", ingredients: { "정제수": 58, "글리세린": 8, "히알루론산": 2.5, "세테아릴알코올": 4, "판테놀": 1.0 } },
        { version: "v1.2", date: "2026-06-28", ingredients: { "정제수": 58, "글리세린": 9.2, "히알루론산": 2.5, "판테놀": 1.0 } }
      ]
    },
    {
      id: "F-002",
      product: "선블록 SPF50+",
      category: "선케어",
      name: "선크림 SPF50 리뉴얼",
      manager: "R-2078",
      tags: ["여름신상"],
      versions: [
        { version: "v2.0", date: "2026-03-15", ingredients: { "정제수": 40, "티타늄디옥사이드": 12, "징크옥사이드": 8, "사이클로펜타실록산": 15 } },
        { version: "v2.1", date: "2026-06-01", ingredients: { "정제수": 38, "티타늄디옥사이드": 13.5, "징크옥사이드": 8, "사이클로펜타실록산": 15, "나이아신아마이드": 2 } }
      ]
    },
    {
      id: "F-003",
      product: "약산성 클렌징폼",
      category: "클렌저",
      name: "저자극 클렌징 폼",
      manager: "R-3115",
      tags: [],
      versions: [
        { version: "v1.0", date: "2026-02-20", ingredients: { "정제수": 65, "코카미도프로필베타인": 12, "라우릴글루코사이드": 10 } },
        { version: "v1.1", date: "2026-05-22", ingredients: { "정제수": 63, "코카미도프로필베타인": 12, "라우릴글루코사이드": 11.5, "판테놀": 0.5 } },
        { version: "v1.2", date: "2026-07-01", ingredients: { "정제수": 63, "코카미도프로필베타인": 13.2, "판테놀": 0.5 } }
      ]
    },
    {
      id: "F-004",
      product: "브라이트닝 세럼 30ml",
      category: "스킨케어",
      name: "비타민C 브라이트닝 세럼",
      manager: "R-1587",
      tags: ["비건"],
      versions: [
        { version: "v1.0", date: "2026-03-08", ingredients: { "정제수": 55, "아스코빌글루코사이드": 5, "나이아신아마이드": 3, "부틸렌글라이콜": 10 } },
        { version: "v1.1", date: "2026-06-14", ingredients: { "정제수": 53, "아스코빌글루코사이드": 6.5, "나이아신아마이드": 3, "부틸렌글라이콜": 10, "판테놀": 1.0 } }
      ]
    },
    {
      id: "F-005",
      product: "딥모이스처 나이트크림 50ml",
      category: "스킨케어",
      name: "세라마이드 나이트크림",
      manager: "R-2244",
      tags: [],
      versions: [
        { version: "v1.0", date: "2026-01-19", ingredients: { "정제수": 50, "세라마이드엔피": 2, "쉐어버터": 8, "스쿠알란": 6 } },
        { version: "v1.1", date: "2026-04-27", ingredients: { "정제수": 48, "세라마이드엔피": 3.2, "쉐어버터": 8, "스쿠알란": 6, "토코페롤": 0.5 } },
        { version: "v1.2", date: "2026-06-30", ingredients: { "정제수": 48, "세라마이드엔피": 3.2, "쉐어버터": 9.5, "토코페롤": 0.5 } }
      ]
    },
    {
      id: "F-006",
      product: "판테놀 진정 토너 150ml",
      category: "스킨케어",
      name: "판테놀 수딩 토너",
      manager: "R-3390",
      tags: [],
      versions: [
        { version: "v1.0", date: "2026-02-11", ingredients: { "정제수": 80, "판테놀": 2, "글리세린": 5, "알란토인": 0.3 } },
        { version: "v1.1", date: "2026-05-05", ingredients: { "정제수": 78.5, "판테놀": 3.2, "글리세린": 5, "알란토인": 0.3 } }
      ]
    },
    {
      id: "F-007",
      product: "레티놀 안티에이징 앰플 30ml",
      category: "스킨케어",
      name: "레티놀 0.3% 앰플",
      manager: "R-1729",
      tags: ["트렌드"],
      versions: [
        { version: "v1.0", date: "2026-03-25", ingredients: { "정제수": 45, "레티놀": 0.3, "스쿠알란": 10, "다이메티콘": 8 } },
        { version: "v1.1", date: "2026-06-09", ingredients: { "정제수": 43.5, "레티놀": 0.3, "스쿠알란": 11.5, "다이메티콘": 8, "판테놀": 0.7 } }
      ]
    },
    {
      id: "F-008",
      product: "저자극 베이비 로션 200ml",
      category: "바디케어",
      name: "베이비 모이스처 로션",
      manager: "R-2951",
      tags: [],
      versions: [
        { version: "v1.0", date: "2026-01-30", ingredients: { "정제수": 70, "쉐어버터": 5, "호호바오일": 4, "판테놀": 1.5 } },
        { version: "v1.1", date: "2026-04-18", ingredients: { "정제수": 68.5, "쉐어버터": 5, "호호바오일": 5.5, "판테놀": 1.5 } }
      ]
    },
    {
      id: "F-009",
      product: "탄력 리프팅 크림 50ml",
      category: "스킨케어",
      name: "펩타이드 리프팅 크림",
      manager: "R-3488",
      tags: [],
      versions: [
        { version: "v1.0", date: "2026-02-27", ingredients: { "정제수": 52, "아세틸헥사펩타이드": 2, "다이메티콘": 8, "쉐어버터": 6 } },
        { version: "v1.1", date: "2026-05-16", ingredients: { "정제수": 50.5, "아세틸헥사펩타이드": 3, "다이메티콘": 8, "쉐어버터": 6, "토코페롤": 0.5 } },
        { version: "v1.2", date: "2026-07-03", ingredients: { "정제수": 50.5, "아세틸헥사펩타이드": 3, "다이메티콘": 9.2, "토코페롤": 0.5 } }
      ]
    },
    {
      id: "F-010",
      product: "산뜻 선쿠션 SPF50+",
      category: "메이크업",
      name: "선쿠션 파운데이션",
      manager: "R-1655",
      tags: [],
      versions: [
        { version: "v1.0", date: "2026-03-02", ingredients: { "정제수": 35, "티타늄디옥사이드": 14, "사이클로펜타실록산": 18, "탈크": 6 } },
        { version: "v1.1", date: "2026-06-20", ingredients: { "정제수": 34, "티타늄디옥사이드": 15.5, "사이클로펜타실록산": 18, "탈크": 6, "나이아신아마이드": 1.5 } }
      ]
    }
  ];

  const RATIO_THRESHOLD = 1; // ±1% 이상은 변경으로 표시

  // ---------- 상태 ----------
  // 선택은 { formulaId, versionIndex } 형태로 최대 2개까지 저장
  let selectedVersions = [];

  const tbody = document.getElementById("formulaTableBody");
  const compareStatus = document.getElementById("compareStatus");
  const compareBtn = document.getElementById("compareBtn");
  const searchInput = document.getElementById("searchInput");

  const sampleGrid = document.getElementById("sampleGrid");
  const categoryFilter = document.getElementById("categoryFilter");

  function populateCategoryOptions() {
    const categories = [...new Set(formulas.map(f => f.category || "미분류"))];
    categoryFilter.innerHTML = `<option value="">전체보기</option>` +
      categories.map(c => `<option value="${c}">${c}</option>`).join("");
  }
  populateCategoryOptions();

  categoryFilter.addEventListener("change", renderSampleCards);

  function renderSampleCards() {
    const selectedCategory = categoryFilter.value;
    const cardFormulas = selectedCategory
      ? formulas.filter(f => (f.category || "미분류") === selectedCategory)
      : formulas;

    if (cardFormulas.length === 0) {
      sampleGrid.innerHTML = `<p class="empty-msg" style="grid-column:1/-1;">해당 카테고리의 처방이 없습니다.</p>`;
      return;
    }

    sampleGrid.innerHTML = cardFormulas.map(f => {
      const latest = f.versions[f.versions.length - 1];
      const category = f.category || "미분류";
      const ingredientRows = Object.entries(latest.ingredients)
        .sort((a, b) => b[1] - a[1])
        .map(([name, ratio]) => `<li><span>${name}</span><span>${ratio.toFixed(1)}%</span></li>`)
        .join("");

      return `
        <div class="sample-card" data-formula="${f.id}">
          <h4 class="sample-card-title">${f.product}</h4>
          <p class="sample-card-desc">${f.name} · 담당 ${f.manager}</p>
          <div class="sample-card-tags">
            <span class="chip chip-category">${category}</span>
            <span class="chip chip-version">${latest.version}</span>
          </div>
          <div class="custom-tags">
            ${(f.tags || []).map(tag => `<span class="chip-custom">${tag}<button type="button" class="tag-remove" data-tag="${tag}">×</button></span>`).join("")}
          </div>
          <div class="tag-add-row">
            <input type="text" class="tag-input" placeholder="태그 추가">
            <button type="button" class="tag-add-btn">추가</button>
          </div>
          <div class="sample-card-toggle">
            <span class="toggle-label">원료 구성 보기</span>
            <span class="toggle-icon">▾</span>
          </div>
          <div class="sample-card-ingredients">
            <p class="ingredients-title">원료 구성 (${latest.version} 기준)</p>
            <ul class="ingredient-list">${ingredientRows}</ul>
          </div>
        </div>
      `;
    }).join("");
  }

  function addTagToCard(formulaId, rawValue) {
    const tag = rawValue.trim();
    if (!tag) { showToast("태그 내용을 입력하세요."); return; }
    const formula = formulas.find(f => f.id === formulaId);
    if (!formula) return;
    formula.tags = formula.tags || [];
    if (formula.tags.includes(tag)) { showToast("이미 추가된 태그입니다."); return; }
    formula.tags.push(tag);
    renderSampleCards();
  }

  sampleGrid.addEventListener("click", (e) => {
    const card = e.target.closest(".sample-card");
    if (!card) return;

    const removeBtn = e.target.closest(".tag-remove");
    if (removeBtn) {
      const formula = formulas.find(f => f.id === card.dataset.formula);
      if (formula) {
        formula.tags = (formula.tags || []).filter(t => t !== removeBtn.dataset.tag);
        renderSampleCards();
      }
      return;
    }

    const addBtn = e.target.closest(".tag-add-btn");
    if (addBtn) {
      const input = card.querySelector(".tag-input");
      addTagToCard(card.dataset.formula, input.value);
      return;
    }

    if (e.target.closest(".tag-input")) return; // 입력창 클릭 시 카드 토글 방지

    card.classList.toggle("expanded");
    const label = card.querySelector(".toggle-label");
    label.textContent = card.classList.contains("expanded") ? "원료 구성 접기" : "원료 구성 보기";
  });

  sampleGrid.addEventListener("keydown", (e) => {
    if (e.key !== "Enter" || !e.target.classList.contains("tag-input")) return;
    const card = e.target.closest(".sample-card");
    if (card) addTagToCard(card.dataset.formula, e.target.value);
  });

  function renderTable(filterText = "") {
    renderSampleCards();
    tbody.innerHTML = "";
    const keyword = filterText.trim().toLowerCase();
    const filtered = formulas.filter(f =>
      f.product.toLowerCase().includes(keyword) || f.name.toLowerCase().includes(keyword)
    );

    if (filtered.length === 0) {
      tbody.innerHTML = `<tr><td colspan="7" class="empty-msg"><img src="bunny-mascot.png" alt="검색 결과 없음">검색 결과가 없습니다.</td></tr>`;
      return;
    }

    filtered.forEach(f => {
      // 각 처방마다 최신 버전만 목록에 노출하되, 이력 전체를 펼쳐서 보여준다.
      f.versions.forEach((v, idx) => {
        const isLatest = idx === f.versions.length - 1;
        const tr = document.createElement("tr");
        tr.className = "formula-row";
        tr.dataset.formula = f.id;
        tr.dataset.version = idx;
        const checkId = `chk-${f.id}-${idx}`;
        const isChecked = selectedVersions.some(s => s.formulaId === f.id && s.versionIndex === idx);

        tr.innerHTML = `
          <td class="select-cell">
            <input type="checkbox" id="${checkId}" data-formula="${f.id}" data-version="${idx}" ${isChecked ? "checked" : ""}>
          </td>
          <td class="product-cell">${f.product}<span class="manager-mobile">담당 ${f.manager}</span></td>
          <td>
            <span class="formula-name">${f.name}</span>
            <span class="formula-id">${f.id} · ${isLatest ? "최신 버전" : "이전 버전"}</span>
          </td>
          <td class="manager-cell">${f.manager}</td>
          <td><span class="version-badge">${v.version}</span></td>
          <td class="date-cell">${v.date}</td>
          <td class="action-cell">
            <button class="icon-btn edit" type="button" onclick="openEditModal('${f.id}', ${idx})">수정</button>
            <button class="icon-btn delete" type="button" onclick="deleteVersion('${f.id}', ${idx})">삭제</button>
          </td>
        `;
        tbody.appendChild(tr);
      });
    });

    // 체크박스 이벤트 바인딩
    tbody.querySelectorAll('input[type="checkbox"]').forEach(cb => {
      cb.addEventListener("change", onVersionCheck);
    });
  }

  function onVersionCheck(e) {
    const formulaId = e.target.dataset.formula;
    const versionIndex = Number(e.target.dataset.version);

    if (e.target.checked) {
      if (selectedVersions.length >= 2) {
        // 이미 2개 선택된 상태면 가장 오래된 선택을 해제하고 새로 추가
        const removed = selectedVersions.shift();
        const removedCb = document.getElementById(`chk-${removed.formulaId}-${removed.versionIndex}`);
        if (removedCb) removedCb.checked = false;
      }
      selectedVersions.push({ formulaId, versionIndex });
    } else {
      selectedVersions = selectedVersions.filter(
        s => !(s.formulaId === formulaId && s.versionIndex === versionIndex)
      );
    }

    updateCompareStatus();
  }

  function updateCompareStatus() {
    const count = selectedVersions.length;
    compareStatus.innerHTML = `비교할 버전을 2개 선택하세요 (<b>${count}/2</b> 선택됨)`;
    compareBtn.disabled = count !== 2;
  }

  searchInput.addEventListener("keydown", (e) => {
    if (e.key !== "Enter") return;
    renderTable(searchInput.value);
  });

  // ---------- 버전 비교 ----------
  const modalOverlay = document.getElementById("modalOverlay");
  const modalTitle = document.getElementById("modalTitle");
  const modalVersus = document.getElementById("modalVersus");
  const compareTableBody = document.getElementById("compareTableBody");

  compareBtn.addEventListener("click", () => {
    if (selectedVersions.length !== 2) return;

    // 날짜 기준으로 정렬해 "이전 -> 이후" 순서를 보장
    const entries = selectedVersions.map(s => {
      const formula = formulas.find(f => f.id === s.formulaId);
      const version = formula.versions[s.versionIndex];
      return { formula, version };
    }).sort((a, b) => new Date(a.version.date) - new Date(b.version.date));

    const [before, after] = entries;

    modalTitle.textContent = `${before.formula.name} 버전 비교`;
    modalVersus.textContent = `${before.version.version} (${before.version.date})  →  ${after.version.version} (${after.version.date})`;

    renderComparison(before.version.ingredients, after.version.ingredients);
    modalOverlay.classList.add("open");
  });

  function renderComparison(beforeMap, afterMap) {
    compareTableBody.innerHTML = "";
    const allNames = new Set([...Object.keys(beforeMap), ...Object.keys(afterMap)]);

    // 정렬: 변경/신규/삭제를 위로, 동일 항목을 아래로
    const rows = [];
    allNames.forEach(name => {
      const beforeVal = beforeMap.hasOwnProperty(name) ? beforeMap[name] : null;
      const afterVal = afterMap.hasOwnProperty(name) ? afterMap[name] : null;
      let status, order;

      if (beforeVal === null) {
        status = "new"; order = 0;
      } else if (afterVal === null) {
        status = "removed"; order = 1;
      } else if (Math.abs(afterVal - beforeVal) >= RATIO_THRESHOLD) {
        status = "changed"; order = 0;
      } else {
        status = "same"; order = 2;
      }
      rows.push({ name, beforeVal, afterVal, status, order });
    });

    rows.sort((a, b) => a.order - b.order || a.name.localeCompare(b.name));

    rows.forEach(r => {
      const tr = document.createElement("tr");
      let rowClass = "";
      let tagHtml = "";
      let beforeCell = r.beforeVal !== null ? `${r.beforeVal.toFixed(1)}%` : `<span class="strike">-</span>`;
      let afterCell = r.afterVal !== null ? `${r.afterVal.toFixed(1)}%` : `<span class="strike">-</span>`;
      let diffCell = "-";

      if (r.status === "new") {
        rowClass = "row-new";
        tagHtml = `<span class="tag new">신규</span>`;
        beforeCell = `<span class="strike">-</span>`;
        diffCell = `<span class="diff-value up">+${r.afterVal.toFixed(1)}%</span>`;
      } else if (r.status === "removed") {
        rowClass = "row-removed";
        tagHtml = `<span class="tag removed">삭제</span>`;
        afterCell = `<span class="strike">-</span>`;
        diffCell = `<span class="diff-value down">-${r.beforeVal.toFixed(1)}%</span>`;
      } else if (r.status === "changed") {
        rowClass = "row-changed";
        tagHtml = `<span class="tag changed">변경</span>`;
        const diff = r.afterVal - r.beforeVal;
        const sign = diff > 0 ? "+" : "";
        diffCell = `<span class="diff-value ${diff > 0 ? "up" : "down"}">${sign}${diff.toFixed(1)}%p</span>`;
      } else {
        tagHtml = `<span class="tag same">동일</span>`;
        diffCell = `<span style="color:var(--text-sub)">0.0%p</span>`;
      }

      tr.className = rowClass;
      tr.innerHTML = `
        <td>${r.name}</td>
        <td>${beforeCell}</td>
        <td>${afterCell}</td>
        <td>${diffCell}</td>
        <td>${tagHtml}</td>
      `;
      compareTableBody.appendChild(tr);
    });
  }

  document.getElementById("modalCloseBtn").addEventListener("click", closeModal);
  modalOverlay.addEventListener("click", (e) => {
    if (e.target === modalOverlay) closeModal();
  });
  function closeModal() {
    modalOverlay.classList.remove("open");
  }

  // ---------- 원료 구성 팝업 ----------
  const ingredientModalOverlay = document.getElementById("ingredientModalOverlay");
  const ingredientModalTitle = document.getElementById("ingredientModalTitle");
  const ingredientModalVersus = document.getElementById("ingredientModalVersus");
  const ingredientModalList = document.getElementById("ingredientModalList");

  tbody.addEventListener("click", (e) => {
    if (e.target.closest("input, button")) return; // 체크박스·수정·삭제 클릭은 제외
    const row = e.target.closest(".formula-row");
    if (!row) return;
    openIngredientModal(row.dataset.formula, Number(row.dataset.version));
  });

  function openIngredientModal(formulaId, versionIndex) {
    const formula = formulas.find(f => f.id === formulaId);
    if (!formula) return;
    const version = formula.versions[versionIndex];
    if (!version) return;

    ingredientModalTitle.textContent = `${formula.product} 원료 구성`;
    ingredientModalVersus.textContent = `${formula.name} · ${version.version} (${version.date})`;

    ingredientModalList.innerHTML = Object.entries(version.ingredients)
      .sort((a, b) => b[1] - a[1])
      .map(([name, ratio]) => `<li><span>${name}</span><span>${ratio.toFixed(1)}%</span></li>`)
      .join("");

    ingredientModalOverlay.classList.add("open");
  }

  document.getElementById("ingredientModalCloseBtn").addEventListener("click", closeIngredientModal);
  ingredientModalOverlay.addEventListener("click", (e) => {
    if (e.target === ingredientModalOverlay) closeIngredientModal();
  });
  function closeIngredientModal() {
    ingredientModalOverlay.classList.remove("open");
  }

  // ---------- 신규 처방 등록 ----------
  const ingredientList = document.getElementById("ingredientList");
  const addRowBtn = document.getElementById("addRowBtn");
  const ratioHint = document.getElementById("ratioHint");
  const registerBtn = document.getElementById("registerBtn");

  function createIngredientRow() {
    const row = document.createElement("div");
    row.className = "ingredient-row";
    row.innerHTML = `
      <input type="text" class="ing-name" placeholder="원료명">
      <input type="number" class="ing-ratio" placeholder="비율(%)" step="0.1">
      <button class="remove-row" type="button" onclick="removeIngredientRow(this)">×</button>
    `;
    row.querySelector(".ing-ratio").addEventListener("input", updateRatioHint);
    return row;
  }

  addRowBtn.addEventListener("click", () => {
    ingredientList.appendChild(createIngredientRow());
  });

  ingredientList.querySelectorAll(".ing-ratio").forEach(inp => {
    inp.addEventListener("input", updateRatioHint);
  });

  function removeIngredientRow(btn) {
    const row = btn.closest(".ingredient-row");
    const container = row.parentElement;
    if (container.children.length > 1) {
      row.remove();
    } else {
      row.querySelector(".ing-name").value = "";
      row.querySelector(".ing-ratio").value = "";
    }
    if (container.id === "editIngredientList") {
      updateEditRatioHint();
    } else {
      updateRatioHint();
    }
  }
  // 전역에 노출 (인라인 onclick에서 사용)
  window.removeIngredientRow = removeIngredientRow;

  function updateRatioHint() {
    const ratios = Array.from(ingredientList.querySelectorAll(".ing-ratio"))
      .map(i => parseFloat(i.value) || 0);
    const total = ratios.reduce((a, b) => a + b, 0);
    ratioHint.textContent = `전체 비율 합계: ${total.toFixed(1)}%`;
    ratioHint.classList.toggle("warn", Math.abs(total - 100) > 0.05 && total !== 0);
  }

  registerBtn.addEventListener("click", () => {
    const product = document.getElementById("newProductName").value.trim();
    const name = document.getElementById("newFormulaName").value.trim();
    const manager = document.getElementById("newManager").value.trim();
    const nameInputs = ingredientList.querySelectorAll(".ing-name");
    const ratioInputs = ingredientList.querySelectorAll(".ing-ratio");

    if (!product) { showToast("제품명을 입력하세요."); return; }
    if (!name) { showToast("처방명을 입력하세요."); return; }
    if (!manager) { showToast("담당자를 입력하세요."); return; }

    const ingredients = {};
    let hasValidIngredient = false;
    for (let i = 0; i < nameInputs.length; i++) {
      const iname = nameInputs[i].value.trim();
      const iratio = parseFloat(ratioInputs[i].value);
      if (iname && !isNaN(iratio)) {
        ingredients[iname] = iratio;
        hasValidIngredient = true;
      }
    }

    if (!hasValidIngredient) { showToast("원료명과 비율을 최소 1개 이상 입력하세요."); return; }

    const newFormula = {
      id: `F-${String(formulas.length + 1).padStart(3, "0")}`,
      product,
      name,
      manager,
      versions: [
        { version: "v1.0", date: new Date().toISOString().slice(0, 10), ingredients }
      ]
    };

    formulas.push(newFormula);
    renderTable(searchInput.value);
    showToast(`"${name}" 처방이 v1.0으로 등록되었습니다.`);

    // 폼 초기화
    document.getElementById("newProductName").value = "";
    document.getElementById("newFormulaName").value = "";
    document.getElementById("newManager").value = "";
    ingredientList.innerHTML = "";
    ingredientList.appendChild(createIngredientRow());
    updateRatioHint();
  });

  // ---------- 처방/버전 수정 ----------
  const editModalOverlay = document.getElementById("editModalOverlay");
  const editModalVersus = document.getElementById("editModalVersus");
  const editProductName = document.getElementById("editProductName");
  const editFormulaName = document.getElementById("editFormulaName");
  const editManager = document.getElementById("editManager");
  const editIngredientList = document.getElementById("editIngredientList");
  const editAddRowBtn = document.getElementById("editAddRowBtn");
  const editRatioHint = document.getElementById("editRatioHint");
  const editSaveBtn = document.getElementById("editSaveBtn");

  let editingTarget = null; // { formulaId, versionIndex }

  function createEditIngredientRow(name = "", ratio = "") {
    const row = document.createElement("div");
    row.className = "ingredient-row";
    row.innerHTML = `
      <input type="text" class="ing-name" placeholder="원료명" value="${name}">
      <input type="number" class="ing-ratio" placeholder="비율(%)" step="0.1" value="${ratio}">
      <button class="remove-row" type="button" onclick="removeIngredientRow(this)">×</button>
    `;
    row.querySelector(".ing-ratio").addEventListener("input", updateEditRatioHint);
    return row;
  }

  function updateEditRatioHint() {
    const ratios = Array.from(editIngredientList.querySelectorAll(".ing-ratio"))
      .map(i => parseFloat(i.value) || 0);
    const total = ratios.reduce((a, b) => a + b, 0);
    editRatioHint.textContent = `전체 비율 합계: ${total.toFixed(1)}%`;
    editRatioHint.classList.toggle("warn", Math.abs(total - 100) > 0.05 && total !== 0);
  }

  editAddRowBtn.addEventListener("click", () => {
    editIngredientList.appendChild(createEditIngredientRow());
    updateEditRatioHint();
  });

  function openEditModal(formulaId, versionIndex) {
    const formula = formulas.find(f => f.id === formulaId);
    if (!formula) return;
    const version = formula.versions[versionIndex];
    if (!version) return;

    editingTarget = { formulaId, versionIndex };
    editModalVersus.textContent = `${formula.id} · ${version.version} (${version.date})`;
    editProductName.value = formula.product;
    editFormulaName.value = formula.name;
    editManager.value = formula.manager;

    editIngredientList.innerHTML = "";
    Object.entries(version.ingredients).forEach(([name, ratio]) => {
      editIngredientList.appendChild(createEditIngredientRow(name, ratio));
    });
    if (editIngredientList.children.length === 0) {
      editIngredientList.appendChild(createEditIngredientRow());
    }
    updateEditRatioHint();

    editModalOverlay.classList.add("open");
  }
  window.openEditModal = openEditModal;

  function closeEditModal() {
    editModalOverlay.classList.remove("open");
    editingTarget = null;
  }
  document.getElementById("editModalCloseBtn").addEventListener("click", closeEditModal);
  editModalOverlay.addEventListener("click", (e) => {
    if (e.target === editModalOverlay) closeEditModal();
  });

  editSaveBtn.addEventListener("click", () => {
    if (!editingTarget) return;
    const formula = formulas.find(f => f.id === editingTarget.formulaId);
    if (!formula) return;
    const version = formula.versions[editingTarget.versionIndex];
    if (!version) return;

    const product = editProductName.value.trim();
    const name = editFormulaName.value.trim();
    const manager = editManager.value.trim();
    const nameInputs = editIngredientList.querySelectorAll(".ing-name");
    const ratioInputs = editIngredientList.querySelectorAll(".ing-ratio");

    if (!product) { showToast("제품명을 입력하세요."); return; }
    if (!name) { showToast("처방명을 입력하세요."); return; }
    if (!manager) { showToast("담당자를 입력하세요."); return; }

    const ingredients = {};
    let hasValidIngredient = false;
    for (let i = 0; i < nameInputs.length; i++) {
      const iname = nameInputs[i].value.trim();
      const iratio = parseFloat(ratioInputs[i].value);
      if (iname && !isNaN(iratio)) {
        ingredients[iname] = iratio;
        hasValidIngredient = true;
      }
    }

    if (!hasValidIngredient) { showToast("원료명과 비율을 최소 1개 이상 입력하세요."); return; }

    formula.product = product;
    formula.name = name;
    formula.manager = manager;
    version.ingredients = ingredients;
    version.date = new Date().toISOString().slice(0, 10);

    closeEditModal();
    renderTable(searchInput.value);
    showToast(`"${name}" ${version.version} 버전이 수정되었습니다.`);
  });

  // ---------- 버전 삭제 ----------
  function deleteVersion(formulaId, versionIndex) {
    const formulaIdx = formulas.findIndex(f => f.id === formulaId);
    if (formulaIdx === -1) return;
    const formula = formulas[formulaIdx];
    const version = formula.versions[versionIndex];
    if (!version) return;

    const confirmed = window.confirm(
      `"${formula.name}" ${version.version} 버전을 삭제하시겠습니까?\n이 작업은 되돌릴 수 없습니다.`
    );
    if (!confirmed) return;

    formula.versions.splice(versionIndex, 1);
    if (formula.versions.length === 0) {
      formulas.splice(formulaIdx, 1);
    }

    // 삭제로 인해 동일 처방의 나머지 버전 인덱스가 밀릴 수 있으므로 관련 선택은 초기화
    selectedVersions = selectedVersions.filter(s => s.formulaId !== formulaId);

    renderTable(searchInput.value);
    updateCompareStatus();
    showToast(`${version.version} 버전이 삭제되었습니다.`);
  }
  window.deleteVersion = deleteVersion;

  // ---------- 토스트 ----------
  let toastTimer;
  function showToast(msg) {
    const toast = document.getElementById("toast");
    toast.textContent = msg;
    toast.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove("show"), 2600);
  }

  // ---------- 배합량 계산기 ----------
  const calcFormulaSelect = document.getElementById("calcFormulaSelect");
  const calcBatchAmount = document.getElementById("calcBatchAmount");
  const calcConfirmBtn = document.getElementById("calcConfirmBtn");
  const calcResult = document.getElementById("calcResult");

  function populateCalcFormulaOptions() {
    calcFormulaSelect.innerHTML = formulas
      .map(f => `<option value="${f.id}">${f.product} (${f.name})</option>`)
      .join("");
  }
  populateCalcFormulaOptions();

  calcConfirmBtn.addEventListener("click", () => {
    const formulaId = calcFormulaSelect.value;
    const batchAmount = parseFloat(calcBatchAmount.value);

    if (!formulaId) { showToast("처방을 선택하세요."); return; }
    if (!batchAmount || batchAmount <= 0) { showToast("배치 용량을 올바르게 입력하세요."); return; }

    calcResult.innerHTML = `<p class="calc-loading">계산 중...</p>`;

    setTimeout(() => {
      const formula = formulas.find(f => f.id === formulaId);
      const latest = formula.versions[formula.versions.length - 1];
      const rows = Object.entries(latest.ingredients).sort((a, b) => b[1] - a[1]);
      const total = rows.reduce((sum, [, ratio]) => sum + (ratio / 100) * batchAmount, 0);

      const listHtml = rows.map(([name, ratio]) => {
        const weight = (ratio / 100) * batchAmount;
        return `<li><span>${name} (${ratio.toFixed(1)}%)</span><span>${weight.toFixed(2)}g</span></li>`;
      }).join("");

      calcResult.innerHTML = `
        <p class="calc-result-title">${formula.product} · ${latest.version} 기준 (배치 ${batchAmount}g)</p>
        <ul class="ingredient-list">${listHtml}</ul>
        <div class="calc-total"><span>합계</span><span>${total.toFixed(2)}g</span></div>
      `;
    }, 600);
  });

  // ---------- 초기 렌더 ----------
  renderTable();
  updateCompareStatus();
</script>

</body>
</html>
"""

components.html(HTML_CONTENT, height=1800, scrolling=True)
