import json
import os

import plotly
import plotly.graph_objects as go
from flask import Flask, render_template

app = Flask(__name__)


def serialize_chart(figure):
    return json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)


def build_tax_forecast_line():
    months = ["2025-01", "2025-04", "2025-07", "2025-10", "2026-01", "2026-04", "2026-07", "2026-10", "2027-01", "2027-04"]
    actual = [3.92, 4.04, 4.18, 4.11, 4.26, 4.35, 4.46, 4.54, 4.63, 4.71]
    forecast = [3.95, 4.02, 4.16, 4.14, 4.24, 4.33, 4.44, 4.51, 4.60, 4.68]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=actual, mode="lines+markers", name="Observed", line={"color": "#143c52", "width": 3}))
    fig.add_trace(go.Scatter(x=months, y=forecast, mode="lines+markers", name="ETS Forecast", line={"color": "#c57b57", "width": 3, "dash": "dash"}))
    fig.update_layout(
        title="Texas Sales Tax Revenue Forecast",
        template="plotly_white",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
        yaxis_title="Revenue (USD Billions)",
        xaxis_title="Month",
        legend={"orientation": "h", "y": 1.12},
    )
    return fig


def build_tax_benchmark():
    periods = ["FY2025", "FY2026", "FY2027"]
    official = [50.8, 52.6, 54.3]
    forecast = [50.5, 53.2, 54.8]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=periods, y=official, name="Official Estimate", marker_color="#9db5c0"))
    fig.add_trace(go.Bar(x=periods, y=forecast, name="Model Forecast", marker_color="#c57b57"))
    fig.update_layout(
        title="Model vs Official Benchmark",
        barmode="group",
        template="plotly_white",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
        yaxis_title="Annual Revenue (USD Billions)",
    )
    return fig


def build_tax_macro():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    vehicle_tax = [101, 103, 108, 111, 109, 114]
    retail_trade = [96, 98, 101, 103, 105, 107]
    unemployment = [4.5, 4.4, 4.2, 4.1, 4.0, 3.9]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=vehicle_tax, name="Vehicle Tax Index", mode="lines+markers"))
    fig.add_trace(go.Scatter(x=months, y=retail_trade, name="Retail Trade Index", mode="lines+markers"))
    fig.add_trace(go.Scatter(x=months, y=unemployment, name="Unemployment Rate", mode="lines+markers", yaxis="y2", line={"dash": "dot"}))
    fig.update_layout(
        title="Macroeconomic Drivers in VAR(2)",
        template="plotly_white",
        margin={"l": 40, "r": 40, "t": 60, "b": 40},
        yaxis={"title": "Index Level"},
        yaxis2={"title": "Rate (%)", "overlaying": "y", "side": "right"},
        legend={"orientation": "h", "y": 1.12},
    )
    return fig


def build_sales_state():
    states = ["Texas", "California", "Florida", "New York", "Illinois", "Georgia"]
    sales = [4.8, 4.1, 3.6, 3.2, 2.9, 2.4]
    fig = go.Figure(go.Bar(x=states, y=sales, marker_color="#143c52"))
    fig.update_layout(
        title="Sales by State During Promotion",
        template="plotly_white",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
        yaxis_title="Revenue (USD Millions)",
    )
    return fig


def build_sales_promo():
    groups = ["Full Price", "Light Discount", "Deep Discount"]
    conversion = [2.1, 3.4, 4.0]
    avg_order = [820, 790, 730]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=groups, y=conversion, name="Conversion Rate (%)", marker_color="#c57b57"))
    fig.add_trace(go.Scatter(x=groups, y=avg_order, name="Avg Order Value (USD)", mode="lines+markers", yaxis="y2", line={"color": "#143c52", "width": 3}))
    fig.update_layout(
        title="Promotion Performance by Price Category",
        template="plotly_white",
        margin={"l": 40, "r": 40, "t": 60, "b": 40},
        yaxis={"title": "Conversion Rate (%)"},
        yaxis2={"title": "Avg Order Value", "overlaying": "y", "side": "right"},
        legend={"orientation": "h", "y": 1.12},
    )
    return fig


def build_sales_channel():
    years = ["2023", "2024", "2025"]
    online = [1.8, 2.2, 2.9]
    retail = [2.6, 2.9, 3.1]
    partners = [1.1, 1.4, 1.7]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=online, name="Online", marker_color="#143c52"))
    fig.add_trace(go.Bar(x=years, y=retail, name="Retail", marker_color="#6b8a96"))
    fig.add_trace(go.Bar(x=years, y=partners, name="Channel Partners", marker_color="#c57b57"))
    fig.update_layout(
        title="Channel Mix by Year",
        barmode="stack",
        template="plotly_white",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
        yaxis_title="Revenue (USD Millions)",
    )
    return fig


ENGLISH = {
    "personal": {
        "name": "Jinrui Li",
        "preferred_name": "Jeri Li",
        "headline": "Data Analytics | Business Intelligence | Forecasting | Supply Chain Analytics",
        "location": "College Station, TX",
        "phone": "+86 18571523696",
        "email": "jinrui@tamu.edu",
        "linkedin": "https://www.linkedin.com/in/jinrui-li-3a9924394",
        "github": "https://github.com/jinrui-0310",
        "resume_url": "/static/files/Jinrui_Li_Resume.pdf",
    },
    "hero": {
        "eyebrow": "Open to analytics, BI, forecasting, and supply chain roles",
        "title": "Turning complex business data into clear decisions.",
        "intro": "Master's student in Econometrics at Texas A&M University with experience in procurement analytics, dashboard reporting, supply chain data modeling, and forecasting.",
        "helper": "The Resume button currently points to the PDF stored in static/files so you can replace it later if needed.",
        "stats": [
            {"value": "¥800K+", "label": "Cost savings supported"},
            {"value": "100K+", "label": "Rows queried and analyzed"},
            {"value": "+/-3%", "label": "Forecast deviation range"},
            {"value": "Power BI", "label": "Dashboard reporting experience"},
        ],
    },
    "about": {
        "title": "Business-minded analytics with a supply chain lens.",
        "body": "I am a Master's student in Econometrics at Texas A&M University with prior experience in procurement analytics, supply chain data modeling, dashboard reporting, and forecasting. My work combines business understanding with analytical tools such as Python, SQL, R, SAS, Power BI, and Excel. I am especially interested in data analytics, business intelligence, forecasting, and operations or supply chain analytics roles.",
        "info": [
            {"label": "Location", "value": "College Station, TX"},
            {"label": "Email", "value": "jinrui@tamu.edu"},
            {"label": "Phone", "value": "+86 18571523696"},
            {"label": "Focus", "value": "Econometrics + Applied Analytics"},
        ],
    },
    "experience": {
        "title": "Procurement and supply chain analytics experience with real business impact.",
        "items": [
            {
                "company": "Voyah Automobile Technology Co., Ltd.",
                "title": "Procurement Data Analyst",
                "dates": "Jul 2021 - Mar 2024",
                "location": "Wuhan, China",
                "bullets": [
                    "Built and maintained Power BI and Excel dashboards to monitor procurement execution progress, cost variance, and supplier delivery performance, supporting monthly reviews and data-driven decisions.",
                    "Used SQL and Power Query to create a centralized procurement data model across projects, parts, suppliers, quotations, and cost data, improving reporting accuracy and cross-functional analysis support.",
                    "Conducted variance and sensitivity analysis on procurement costs, helping identify optimization opportunities and contributing to over RMB 800K in savings.",
                    "Partnered with procurement, R&D, logistics, and finance teams to support scheduling, delivery coordination, issue diagnosis, and business analysis.",
                    "Delivered ad hoc analysis and structured reporting for audit and business review needs, reducing document rework by approximately 40%.",
                ],
            }
        ],
    },
    "projects": [
        {
            "title": "Revenue Forecasting for Planning and Decision Support",
            "time": "Feb 2025 - Apr 2025",
            "summary": "Built time-series models in R to forecast 30 months of Texas sales tax revenue and benchmarked results against official state estimates.",
            "tags": ["R", "Time Series", "Forecasting"],
            "url": "/en/projects/tax-forecasting",
        },
        {
            "title": "Promotional Demand Analysis for Inventory and Channel Planning",
            "time": "Apr 2025 - May 2025",
            "summary": "Analyzed 100K+ records with SQL and Python to identify regional demand patterns, channel performance, and product-tier differences during a promotion period.",
            "tags": ["SQL", "Python", "Visualization"],
            "url": "/en/projects/sales-analytics",
        },
    ],
    "skills": {
        "Languages": ["SQL", "Python", "R", "SAS"],
        "Analytics": ["Data Cleaning", "EDA", "Data Transformation", "Data Visualization", "Time Series Forecasting", "Business Data Analysis"],
        "Tools / Libraries": ["Power BI", "pandas", "NumPy", "matplotlib", "statsmodels", "scikit-learn", "JupyterLab"],
        "Database / Systems": ["PostgreSQL", "Docker", "Git", "Linux (bash)"],
        "Capabilities": ["Relational Modeling", "JOINs & Window Functions", "KPI Reporting", "Cross-functional Data Collaboration", "Insight Communication"],
    },
    "education": [
        {
            "school": "Texas A&M University",
            "degree": "Master of Science in Econometrics",
            "dates": "Jan 2025 - Dec 2026 (Expected)",
            "location": "College Station, TX, USA",
            "details": "GPA: 3.4/4.0 | Relevant coursework: Economic Forecasting, Data Mining, Regression Analysis, Databases & Big Data, Financial Data Analytics",
        },
        {
            "school": "Wuhan University of Technology",
            "degree": "Bachelor of Management in Logistics Management",
            "dates": "Sep 2017 - Jun 2021",
            "location": "Wuhan, China",
            "details": "GPA: 3.2/4.0 | Honors: University scholarship, merit student recognition, and awards in logistics innovation and design competitions",
        },
    ],
}


CHINESE = {
    "personal": {
        "name": "李今锐",
        "preferred_name": "李今锐",
        "headline": "数据分析 | 商业分析 | 供应链分析",
        "location": "美国德州，College Station",
        "phone": "+86 18571523696",
        "wechat": "18571523696",
        "wechat_note": "备注：因时差，若电话无法接通，还请您添加微信，我会尽快回复，感谢。",
        "email": "jinrui@tamu.edu",
        "linkedin": "https://www.linkedin.com/in/jinrui-li-3a9924394",
        "github": "https://github.com/jinrui-0310",
        "resume_url": "/static/files/Jinrui_Li_Resume.pdf",
    },
    "hero": {
        "eyebrow": "求职方向：数据分析、商业分析、供应链分析",
        "title": "把复杂业务数据转化为可执行的业务决策。",
        "intro": "美国 Texas A&M University 经济学硕士在读，具备国际化学习背景和中英文双语沟通能力。研究生阶段系统接受数据分析、经济预测、回归分析与数据库工具训练，能够完成数据处理、建模分析、趋势预测和业务洞察输出。结合近3年企业数据分析相关经验，能够较快理解业务场景并支持数据驱动决策。",
        "helper": "当前 Resume 按钮已经连接到项目里的 PDF 简历文件，后续你也可以替换成线上链接。",
        "stats": [
            {"value": "¥800K+", "label": "支持实现成本节约"},
            {"value": "100K+", "label": "查询与分析记录数"},
            {"value": "+/-3%", "label": "预测偏差范围"},
            {"value": "Power BI", "label": "Dashboard 报告经验"},
        ],
    },
    "about": {
        "title": "兼具业务理解与分析能力，关注数据驱动的业务洞察与决策支持。",
        "body": "美国 Texas A&M University 计量经济学硕士在读，具备中英文双语沟通能力。研究生阶段系统接受数据分析、经济预测、回归分析与数据库工具训练，能够完成数据处理、建模分析、趋势预测和业务洞察输出。结合近3年工业界数据分析相关经验，能够较快理解业务场景并支持数据驱动决策。",
        "info": [
            {"label": "所在地", "value": "美国德州，College Station"},
            {"label": "邮箱", "value": "jinrui@tamu.edu"},
            {"label": "电话", "value": "+86 18571523696"},
            {"label": "方向", "value": "计量经济学 + 应用数据分析"},
        ],
    },
    "experience": {
        "title": "在采购与供应链场景中积累了真实业务落地的数据分析经验。",
        "items": [
            {
                "company": "岚图汽车科技股份有限公司",
                "title": "采购数据分析师",
                "dates": "2021年7月 - 2024年3月",
                "location": "中国武汉",
                "bullets": [
                    "负责搭建并维护 Power BI 与 Excel 业务分析仪表盘，对采购计划执行进度、成本偏差及供应商交付表现等核心指标进行持续监控和分析，支撑月度经营复盘、业务洞察输出及数据驱动决策。",
                    "使用 SQL 和 Power Query 搭建集中化采购数据模型，打通项目、零件、供应商、报价及成本等多维业务数据，提升数据整合效率、报表准确性和跨部门分析支持能力。",
                    "针对采购成本开展方差分析和敏感性分析，识别主要成本影响因素及优化机会，为降本方案制定和业务决策提供数据依据，项目周期内累计推动实现超过 80 万元人民币的成本节约。",
                    "协同采购、研发、物流和财务等团队开展业务数据分析，支持采购排期、交付安排及异常问题定位，为跨部门协作和业务决策提供数据支持。",
                    "承担临时性数据分析与报告输出工作，形成结构化分析结论，支持审计和业务复盘，将文档返工率降低约 40%。",
                ],
            }
        ],
    },
    "projects": [
        {
            "title": "收入预测：支持规划与决策分析",
            "time": "2025年2月 - 2025年4月",
            "summary": "基于 R 构建时间序列模型，对德州销售税收入未来 30 个月走势进行测算，并与官方州级估计进行对比验证。",
            "tags": ["R", "时间序列", "预测分析"],
            "url": "/zh/projects/tax-forecasting",
        },
        {
            "title": "促销需求分析：支持库存与渠道规划",
            "time": "2025年4月 - 2025年5月",
            "summary": "基于 SQL 与 Python 对 10 万+ 销售记录进行分析，识别区域需求、渠道表现与产品层级差异，支撑库存配置与渠道规划。",
            "tags": ["SQL", "Python", "数据可视化"],
            "url": "/zh/projects/sales-analytics",
        },
    ],
    "skills": {
        "编程语言": ["SQL", "Python", "R", "SAS"],
        "数据分析": ["数据清洗", "探索性数据分析", "数据转换", "数据可视化", "时间序列预测", "业务数据分析"],
        "工具 / 库": ["Power BI", "pandas", "NumPy", "matplotlib", "statsmodels", "scikit-learn", "JupyterLab"],
        "数据库 / 系统": ["PostgreSQL", "Docker", "Git", "Linux（bash）"],
        "相关能力": ["关系建模", "JOIN 与窗口函数", "KPI 报表分析", "跨部门数据协作", "数据洞察输出"],
    },
    "education": [
        {
            "school": "德州农工大学（QS前150）",
            "degree": "计量经济学硕士",
            "dates": "2025/01 - 2026/12（预计）",
            "location": "美国，大学城",
            "gpa": "GPA：3.4/4.0",
            "coursework": "相关课程：数据挖掘、回归分析、数据库与大数据、金融数据分析、经济预测",
        },
        {
            "school": "武汉理工大学（211工程）",
            "degree": "物流管理学士",
            "dates": "2017/09 - 2021/06",
            "location": "中国，武汉",
            "gpa": "GPA：3.2/4.0",
            "honors": "奖项荣誉：校级三等奖学金（前13%）、院级三好学生（前30%）、“顺丰杯”物流创新大赛三等奖、“马钢杯”全国大学生物流设计大赛三等奖",
        },
    ],
}


TAX_PROJECT_EN = {
    "title": "Revenue Forecasting for Planning and Decision Support",
    "time": "Feb 2025 - Apr 2025",
    "tags": ["R", "ETS", "ARIMA", "VAR"],
    "overview": "Built time-series forecasting models in R to estimate Texas sales tax revenue over the next 30 months and support medium-term planning decisions.",
    "business_problem": "Planning work requires forecasts that are both reliable and explainable. This project aimed to provide a quantitative view of expected revenue trends and assess whether the model outputs aligned closely with official state guidance.",
    "tech_stack": ["R", "Time Series Modeling", "ETS", "ARIMA", "VAR"],
    "methods": [
        "Built time-series models to project 30 months of Texas sales tax revenue.",
        "Benchmarked forecasts against FY2025-FY2027 official state estimates.",
        "Introduced macroeconomic indicators such as retail trade, vehicle tax, and unemployment to improve explanatory power.",
        "Compared multiple model forms and selected the strongest-performing approach.",
    ],
    "results": [
        "Forecast deviation remained within +/-3% versus official estimates.",
        "Improved planning relevance by linking revenue patterns to macro drivers.",
        "Produced a reusable forecasting workflow for future refreshes.",
    ],
    "detail_intro": "The charts below are realistic placeholders and can later be replaced with your actual forecasting outputs.",
    "charts": [
        {"id": "tax-en-1", "title": "Forecast Line Chart", "description": "Observed revenue versus the selected ETS forecast.", "graph_json": serialize_chart(build_tax_forecast_line())},
        {"id": "tax-en-2", "title": "Official Benchmark Comparison", "description": "Model output compared with official planning estimates.", "graph_json": serialize_chart(build_tax_benchmark())},
        {"id": "tax-en-3", "title": "Macro Drivers", "description": "Illustrative view of the macro indicators used in the model.", "graph_json": serialize_chart(build_tax_macro())},
    ],
}


SALES_PROJECT_EN = {
    "title": "Promotional Demand Analysis for Inventory and Channel Planning",
    "time": "Apr 2025 - May 2025",
    "tags": ["SQL", "Python", "Visualization"],
    "overview": "Combined SQL extraction and Python analysis to evaluate promotional demand patterns across regions, channels, and product tiers.",
    "business_problem": "Teams needed to understand which markets and product layers performed best during the promotion period so they could make better inventory and channel planning decisions.",
    "tech_stack": ["SQL", "Python", "pandas", "PostgreSQL", "JupyterLab"],
    "methods": [
        "Extracted, joined, and cleaned 100K+ records across customer, product, and transaction tables.",
        "Segmented results by year, channel, and price tier to compare demand patterns.",
        "Built visual summaries for regional demand, promotion performance, and year-over-year change.",
        "Structured outputs so findings could directly support planning discussions.",
    ],
    "results": [
        "Highlighted key markets and stronger-performing product layers.",
        "Created clear visuals for inventory allocation and channel planning conversations.",
        "Demonstrated an end-to-end SQL and Python analytics workflow.",
    ],
    "detail_intro": "These charts are placeholders designed to be easy to replace with your own business visuals later.",
    "charts": [
        {"id": "sales-en-1", "title": "Sales by State", "description": "Illustrative state-level demand ranking during promotion.", "graph_json": serialize_chart(build_sales_state())},
        {"id": "sales-en-2", "title": "Promotion Performance Comparison", "description": "Conversion and order value by price tier.", "graph_json": serialize_chart(build_sales_promo())},
        {"id": "sales-en-3", "title": "Channel Mix by Year", "description": "Stacked view of channel contribution over time.", "graph_json": serialize_chart(build_sales_channel())},
    ],
}


TAX_PROJECT_ZH = {
    "title": "收入预测：支持规划与决策分析",
    "time": "2025年2月 - 2025年4月",
    "tags": ["R", "ETS", "ARIMA", "VAR"],
    "overview": "基于 R 构建时间序列预测模型，对德州销售税收入未来 30 个月的走势进行测算和趋势判断，为中期规划制定及相关决策分析提供量化依据。",
    "business_problem": "规划分析需要兼顾预测准确性、稳定性与解释能力。该项目的目标是通过可量化的方法判断未来收入趋势，并验证模型结果在实际规划场景中的参考价值。",
    "tech_stack": ["R", "时间序列建模", "ETS", "ARIMA", "VAR"],
    "methods": [
        "构建时间序列预测模型，对未来 30 个月德州销售税收入进行测算。",
        "将模型结果与 FY2025-FY2027 官方州级估计进行对比验证。",
        "引入零售贸易、车辆税、失业率等宏观经济指标，分析关键影响因素。",
        "比较不同模型形式并选择表现更优的方案。",
    ],
    "results": [
        "预测偏差控制在 ±3% 以内，验证了模型稳定性。",
        "增强了预测结果的解释能力和规划参考价值。",
        "形成了可继续刷新和扩展的预测分析流程。",
    ],
    "detail_intro": "下方图表为占位展示，后续可以直接替换为你自己的真实模型结果。",
    "charts": [
        {"id": "tax-zh-1", "title": "预测趋势图", "description": "展示历史观测值与预测结果的对比。", "graph_json": serialize_chart(build_tax_forecast_line())},
        {"id": "tax-zh-2", "title": "官方预测对比图", "description": "将模型结果与官方州级估计进行比较。", "graph_json": serialize_chart(build_tax_benchmark())},
        {"id": "tax-zh-3", "title": "宏观驱动因素图", "description": "展示模型中使用的宏观变量示意。", "graph_json": serialize_chart(build_tax_macro())},
    ],
}


SALES_PROJECT_ZH = {
    "title": "促销需求分析：支持库存与渠道规划",
    "time": "2025年4月 - 2025年5月",
    "tags": ["SQL", "Python", "数据可视化"],
    "overview": "基于 SQL 与 Python 对促销期间各区域、渠道和产品层级的需求表现进行分析，为库存配置与渠道规划提供支持。",
    "business_problem": "业务团队需要快速识别哪些区域需求更强、哪些产品层级表现更好，以及不同渠道的销售差异，从而优化库存投放与渠道资源分配。",
    "tech_stack": ["SQL", "Python", "pandas", "PostgreSQL", "JupyterLab"],
    "methods": [
        "基于 SQL 对客户、商品和交易等多张业务表中的 10 万+ 销售记录进行提取、关联和清洗。",
        "使用 pandas 按年份、渠道和价格层级对销售数据进行整理拆分，完成 3 年、2 个渠道、4 个价格层级的对比分析。",
        "结合业务需求输出区域需求趋势、促销累计表现和同比变化等可视化图表。",
        "通过结构化分析识别重点市场及高表现产品分层，支撑库存和渠道决策讨论。",
    ],
    "results": [
        "完成了从 SQL 数据提取到 Python 可视化输出的端到端业务分析流程。",
        "识别出促销期间重点市场及高表现产品层级。",
        "为库存配置与渠道规划提供了清晰的数据支持。",
    ],
    "detail_intro": "这些图表是贴近业务分析场景的占位版本，后续你可以直接替换成自己的查询结果或真实图表。",
    "charts": [
        {"id": "sales-zh-1", "title": "州别销售表现", "description": "展示促销期间各州收入排名的示意图。", "graph_json": serialize_chart(build_sales_state())},
        {"id": "sales-zh-2", "title": "促销表现对比", "description": "展示不同价格分层下的转化率与客单价差异。", "graph_json": serialize_chart(build_sales_promo())},
        {"id": "sales-zh-3", "title": "渠道与年份拆解", "description": "展示不同年份下渠道收入结构的变化。", "graph_json": serialize_chart(build_sales_channel())},
    ],
}


@app.route("/")
@app.route("/en")
def home_en():
    return render_template("index_en.html", page_title="Jinrui Li | Data Analytics & BI Portfolio", data=ENGLISH)


@app.route("/projects")
def projects_en():
    return render_template("projects_en.html", page_title="Projects | Jeri Li", data=ENGLISH)


@app.route("/en/projects/tax-forecasting")
def project_tax_en():
    return render_template("project_tax_forecasting_en.html", page_title="Revenue Forecasting | Jeri Li", data=ENGLISH, project=TAX_PROJECT_EN)


@app.route("/en/projects/sales-analytics")
def project_sales_en():
    return render_template("project_sales_analytics_en.html", page_title="Promotional Demand Analysis | Jeri Li", data=ENGLISH, project=SALES_PROJECT_EN)


@app.route("/zh")
def home_zh():
    return render_template("index_zh.html", page_title="李今锐 | 数据分析作品集", data=CHINESE)


@app.route("/zh/projects")
def projects_zh():
    return render_template("projects_zh.html", page_title="项目经历 | 李今锐", data=CHINESE)


@app.route("/zh/projects/tax-forecasting")
def project_tax_zh():
    return render_template("project_tax_forecasting_zh.html", page_title="收入预测项目 | 李今锐", data=CHINESE, project=TAX_PROJECT_ZH)


@app.route("/zh/projects/sales-analytics")
def project_sales_zh():
    return render_template("project_sales_analytics_zh.html", page_title="促销需求分析项目 | 李今锐", data=CHINESE, project=SALES_PROJECT_ZH)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
