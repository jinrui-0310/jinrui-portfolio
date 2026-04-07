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


def build_procurement_overview_trend():
    months = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06"]
    sourcing_attainment = [82, 85, 87, 89, 91, 93]
    on_time_sourcing = [78, 80, 83, 84, 86, 88]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=sourcing_attainment, mode="lines+markers", name="Sourcing Attainment Rate", line={"color": "#1f4f7a", "width": 3}))
    fig.add_trace(go.Scatter(x=months, y=on_time_sourcing, mode="lines+markers", name="On-Time Sourcing Rate", line={"color": "#7c8ea3", "width": 3}))
    fig.update_layout(
        title="Monthly Sourcing Progress Overview",
        template="plotly_white",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
        yaxis_title="Rate (%)",
        xaxis_title="Year-Month",
        legend={"orientation": "h", "y": 1.12},
    )
    return fig


def build_procurement_program_attainment():
    programs = ["P01", "P02", "P03", "P04", "P05"]
    attainment = [94, 91, 88, 85, 82]
    fig = go.Figure(go.Bar(x=programs, y=attainment, marker_color="#1f4f7a"))
    fig.update_layout(
        title="Sourcing Attainment by Program",
        template="plotly_white",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
        yaxis_title="Attainment Rate (%)",
        xaxis_title="Program ID",
    )
    return fig


def build_supplier_claims():
    suppliers = ["Supplier A", "Supplier B", "Supplier C", "Supplier D", "Supplier E"]
    claims = [125, 110, 92, 76, 63]
    fig = go.Figure(go.Bar(x=suppliers, y=claims, marker_color="#4f6b88"))
    fig.update_layout(
        title="Claim Amount by Supplier",
        template="plotly_white",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
        yaxis_title="Claim Amount (K RMB)",
        xaxis_title="Supplier",
    )
    return fig


def build_supplier_category_claims():
    categories = ["Battery", "Interior", "Electronics", "Body", "Chassis"]
    claims = [138, 112, 96, 78, 61]
    fig = go.Figure(go.Bar(x=categories, y=claims, marker_color="#7c8ea3"))
    fig.update_layout(
        title="Claim Amount by Part Category",
        template="plotly_white",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
        yaxis_title="Claim Amount (K RMB)",
        xaxis_title="Part Category",
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
        "resume_url": "/static/files/Jinrui_Li_Resume_EN.pdf",
        "resume_zh_url": "/static/files/Jinrui_Li_Resume_ZH.pdf",
    },
    "hero": {
        "eyebrow": "Target roles: Data Analytics, Business Analytics, and Supply Chain Analytics",
        "title": "Turning complex business data into actionable decisions.",
        "intro": "Master's student in Econometrics at Texas A&M University with an international academic background and bilingual communication skills. Graduate study has focused on data analysis, forecasting, regression, and database tools, with the ability to handle data preparation, modeling, trend analysis, and business insight delivery. Combined with nearly three years of industry analytics experience, I can get up to speed quickly and support data-driven decisions in real business settings.",
        "helper": "The English Resume button points to the PDF stored in static/files, so you can replace it later if needed.",
        "stats": [
            {"value": "¥800K+", "label": "Cost savings supported"},
            {"value": "100K+", "label": "Rows queried and analyzed"},
            {"value": "+/-3%", "label": "Forecast deviation range"},
            {"value": "Power BI", "label": "Dashboard reporting experience"},
        ],
    },
    "about": {
        "title": "A business-focused analyst with hands-on experience in insight generation and decision support.",
        "body": "I am a Master's student in Econometrics at Texas A&M University with bilingual communication skills in Chinese and English. My graduate training has covered data analysis, forecasting, regression, and database tools, and I am comfortable with data preparation, modeling, trend analysis, and business insight communication. Combined with nearly three years of industry experience, I can quickly understand business contexts and support data-driven decision-making.",
        "info": [
            {"label": "Location", "value": "College Station, TX"},
            {"label": "Email", "value": "jinrui@tamu.edu"},
            {"label": "Phone", "value": "+86 18571523696"},
            {"label": "Focus", "value": "Econometrics + Applied Analytics"},
        ],
    },
    "experience": {
        "title": "Hands-on analytics experience in procurement and supply chain settings with measurable business impact.",
        "items": [
            {
                "company": "Voyah Automobile Technology Co., Ltd.",
                "company_url": "https://www.voyah.com.cn",
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
            "title": "Procurement Sourcing and Supplier Performance Dashboard",
            "time": "Jan 2026",
            "summary": "Built a Power BI dashboard around sourcing progress, cost achievement, and supplier performance to support procurement management and issue diagnosis.",
            "tags": ["Power BI", "Procurement Analytics", "Supplier Performance"],
            "url": "/en/projects/procurement-dashboard",
        },
        {
            "title": "Promotion Demand Analysis",
            "time": "Apr 2025 - May 2025",
            "summary": "Analyzed promotional sales data in PostgreSQL and built a three-page Tableau dashboard to compare regional demand, model performance, and product lifecycle trends.",
            "tags": ["PostgreSQL", "SQL", "Tableau", "Sales Analytics"],
            "url": "/en/projects/promotion-demand-analysis",
        },
        {
            "title": "Revenue Forecasting for Planning and Decision Support",
            "time": "Feb 2025 - Apr 2025",
            "summary": "Built time-series models in R to forecast 30 months of Texas sales tax revenue and benchmarked results against official state estimates.",
            "tags": ["R", "Time Series", "Forecasting"],
            "url": "/en/projects/tax-forecasting",
        },
    ],
    "skills": {
        "Programming & Querying": ["SQL", "Python", "R", "SAS"],
        "Visualization & BI": ["Power BI", "Tableau", "Dashboard Design", "KPI Design", "Interactive Visualization", "Visual Storytelling"],
        "Data Analysis": ["Data Cleaning", "Exploratory Data Analysis", "Data Transformation", "Business Data Analysis", "Demand and Trend Analysis", "Time Series Forecasting"],
        "Data Modeling & Processing": ["Relational Modeling", "Star Schema", "JOINs & Window Functions", "Metric Definition", "Insight Communication", "Cross-functional Data Collaboration"],
        "Tools & Environment": ["pandas", "NumPy", "matplotlib", "statsmodels", "scikit-learn", "PostgreSQL", "Docker", "Git", "Linux (bash)", "JupyterLab"],
    },
    "certificates": [
        {"title_zh": "Azure 入门", "title_en": "Introduction to Azure", "url": "/static/files/certificates/Introduction to Azure.pdf", "image_url": "/static/images/certificates/Introduction to Azure.pdf.png"},
        {"title_zh": "中级 SQL", "title_en": "Intermediate SQL", "url": "/static/files/certificates/certificate1.pdf", "image_url": "/static/images/certificates/certificate1.pdf.png"},
        {"title_zh": "SQL 数据连接", "title_en": "Joining Data in SQL", "url": "/static/files/certificates/certificate2.pdf", "image_url": "/static/images/certificates/certificate2.pdf.png"},
        {"title_zh": "Seaborn 数据可视化入门", "title_en": "Introduction to Data Visualization with Seaborn", "url": "/static/files/certificates/certificate3.pdf", "image_url": "/static/images/certificates/certificate3.pdf.png"},
        {"title_zh": "Git 入门", "title_en": "Introduction to Git", "url": "/static/files/certificates/certificate4.pdf", "image_url": "/static/images/certificates/certificate4.pdf.png"},
        {"title_zh": "pandas 数据处理", "title_en": "Data Manipulation with pandas", "url": "/static/files/certificates/certificate5.pdf", "image_url": "/static/images/certificates/certificate5.pdf.png"},
    ],
    "education": [
        {
            "school": "Texas A&M University",
            "school_tag": "Top 150 QS",
            "degree": "Master of Science in Econometrics",
            "dates": "Jan 2025 - Dec 2026 (Expected)",
            "location": "College Station, TX, USA",
            "gpa": "GPA: 3.4/4.0",
            "coursework": "Relevant coursework: Data Mining, Regression Analysis, Databases & Big Data, Financial Data Analytics, Economic Forecasting",
        },
        {
            "school": "Wuhan University of Technology",
            "school_tag": "Project 211",
            "degree": "Bachelor of Management in Logistics Management",
            "dates": "Sep 2017 - Jun 2021",
            "location": "Wuhan, China",
            "gpa": "GPA: 3.2/4.0",
            "honors": "Honors: University scholarship, merit student recognition, and awards in logistics innovation and design competitions",
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
        "wechat_note": "因时差问题，电话可能无法接通，还请您添加微信，我会尽快回复，十分感谢。",
        "email": "jinrui@tamu.edu",
        "linkedin": "https://www.linkedin.com/in/jinrui-li-3a9924394",
        "github": "https://github.com/jinrui-0310",
        "resume_url": "/static/files/Jinrui_Li_Resume_ZH.pdf",
        "resume_en_url": "/static/files/Jinrui_Li_Resume_EN.pdf",
    },
    "hero": {
        "eyebrow": "求职方向：数据分析、商业分析、供应链分析",
        "title": "把复杂业务数据转化为可执行的业务决策。",
        "intro": "美国 Texas A&M University 经济学硕士在读，具备国际化学习背景和中英文双语沟通能力。研究生阶段系统接受数据分析、经济预测、回归分析与数据库工具训练，能够完成数据处理、建模分析、趋势预测和业务洞察输出。结合近3年企业数据分析相关经验，能够较快理解业务场景并支持数据驱动决策。",
        "helper": "当前中文页面的简历按钮已经连接到项目里的中文版 PDF，后续你也可以替换成线上链接。",
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
                "company_url": "https://www.voyah.com.cn",
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
            "title": "采购定点与供应商绩效分析 Dashboard",
            "time": "2026年1月",
            "summary": "基于采购业务逻辑构建 Power BI 仪表板，围绕采购定点推进、成本达成与供应商绩效监控，支持采购管理与问题定位。",
            "tags": ["Power BI", "采购分析", "供应商绩效"],
            "url": "/zh/projects/procurement-dashboard",
        },
        {
            "title": "销售税收入预测：支持德州财政规划与决策分析",
            "time": "2025年8月 - 2025年9月",
            "summary": "基于历史德州销售税数据构建时间序列预测框架，对未来 30 个月收入走势进行测算，并与 Texas Comptroller 官方财政估计进行 benchmark 比较。",
            "tags": ["R", "时间序列", "ETS", "VAR"],
            "url": "/zh/projects/texas-sales-tax-forecasting",
        },
        {
            "title": "汽车促销期销售洞察：区域需求、渠道表现与产品生命周期",
            "time": "2025年4月 - 2025年5月",
            "summary": "基于 PostgreSQL 与 SQL 清洗促销销售数据，并用 Tableau 搭建三页 dashboard，分析区域需求、车型表现与生命周期趋势。",
            "tags": ["PostgreSQL", "SQL", "Tableau"],
            "url": "/zh/projects/promotion-demand-analysis",
        },
    ],
    "skills": {
        "编程与查询": ["SQL", "Python", "R", "SAS"],
        "可视化与 BI": ["Power BI", "Tableau", "Dashboard 设计", "KPI 指标设计", "交互式可视化", "可视化故事表达"],
        "数据分析": ["数据清洗", "探索性数据分析", "数据转换", "业务数据分析", "需求与趋势分析", "时间序列预测"],
        "数据建模与处理": ["关系建模", "Star Schema", "JOIN 与窗口函数", "指标口径设计", "数据洞察输出", "跨部门数据协作"],
        "工具与环境": ["pandas", "NumPy", "matplotlib", "statsmodels", "scikit-learn", "PostgreSQL", "Docker", "Git", "Linux (bash)", "JupyterLab"],
    },
    "certificates": [
        {"title_zh": "Azure 入门", "title_en": "Introduction to Azure", "url": "/static/files/certificates/Introduction to Azure.pdf", "image_url": "/static/images/certificates/Introduction to Azure.pdf.png"},
        {"title_zh": "中级 SQL", "title_en": "Intermediate SQL", "url": "/static/files/certificates/certificate1.pdf", "image_url": "/static/images/certificates/certificate1.pdf.png"},
        {"title_zh": "SQL 数据连接", "title_en": "Joining Data in SQL", "url": "/static/files/certificates/certificate2.pdf", "image_url": "/static/images/certificates/certificate2.pdf.png"},
        {"title_zh": "Seaborn 数据可视化入门", "title_en": "Introduction to Data Visualization with Seaborn", "url": "/static/files/certificates/certificate3.pdf", "image_url": "/static/images/certificates/certificate3.pdf.png"},
        {"title_zh": "Git 入门", "title_en": "Introduction to Git", "url": "/static/files/certificates/certificate4.pdf", "image_url": "/static/images/certificates/certificate4.pdf.png"},
        {"title_zh": "pandas 数据处理", "title_en": "Data Manipulation with pandas", "url": "/static/files/certificates/certificate5.pdf", "image_url": "/static/images/certificates/certificate5.pdf.png"},
    ],
    "education": [
        {
            "school": "德州农工大学",
            "school_tag": "QS前150",
            "degree": "计量经济学硕士",
            "dates": "2025/01 - 2026/12（预计）",
            "location": "美国，大学城",
            "gpa": "GPA：3.4/4.0",
            "coursework": "相关课程：数据挖掘、回归分析、数据库与大数据、金融数据分析、经济预测",
        },
        {
            "school": "武汉理工大学",
            "school_tag": "211工程",
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


PROMOTION_DEMAND_PROJECT_EN = {
    "title": "Promotion Demand Analysis",
    "time": "Apr 2025 - May 2025",
    "tags": ["PostgreSQL", "SQL", "Tableau", "Sales Analytics"],
    "overview": "This project focused on promotional sales performance and translated relational business data into a dashboard-ready analytical view for inventory and channel planning. Using PostgreSQL, SQL, and Tableau, I combined sales, customer, product, and dealership data to compare regional demand, model performance, and lifecycle behavior during the promotion period.",
    "process_summary": "The workflow started with transactional and reference tables stored in PostgreSQL, including sales, customers, products, and dealerships. I used SQL to join, filter, and standardize the raw records, created analysis-ready tables for different business questions, did a light round of validation on row counts and aggregated totals, and then built the final Tableau dashboards for review.",
    "tech_stack": ["PostgreSQL", "SQL", "pgAdmin", "Python", "pandas", "Tableau"],
    "data_work": [
        "Reviewed the table structure first and identified the join keys needed to connect sales, customer geography, product attributes, and dealership coverage.",
        "Pulled the relevant promotional records and kept the fields needed for sales amount, transaction timing, channel, region, model, and price positioning.",
        "Standardized category values and created derived fields such as price_category and transaction_year so the outputs could be used directly in Tableau.",
        "Built separate analysis tables for overview, regional/model analysis, and lifecycle tracking instead of trying to answer every question from one flattened extract.",
        "Validated the transformed tables by checking row counts and comparing Tableau-facing aggregates with SQL output totals.",
    ],
    "dashboard_sections": [
        {
            "title": "Dashboard 1: Overall Sales Overview",
            "question": "What does the promotion look like at a high level, and how do sales volume, channel mix, and price tiers behave across the period?",
            "image_url": "/static/images/projects/promotion-demand-analysis/dashboard-1-overview.png",
            "alt": "Promotion Demand Analysis Tableau dashboard overview",
            "findings": [
                "The overview page makes it easy to compare total sales, transaction count, and average sales value without switching across separate reports.",
                "Yearly and channel-level comparisons show that promotion performance is not driven by one dimension alone, so summary KPIs need to be read alongside mix changes.",
                "Price-tier distribution gives a quick read on where demand is concentrating, which is useful when deciding how aggressively to support different product bands.",
            ],
        },
        {
            "title": "Dashboard 2: Regional and Model Performance",
            "question": "Which states and models performed better during the promotion, and where should the business focus inventory and sales attention?",
            "image_url": "/static/images/projects/promotion-demand-analysis/dashboard-2-region-model.png",
            "alt": "Promotion Demand Analysis Tableau dashboard for region and model performance",
            "findings": [
                "State-level demand is uneven, so the regional view helps surface where inventory placement is likely to have the strongest payoff.",
                "Comparing top and bottom markets prevents the team from treating promotion demand as a single national pattern.",
                "Model-level filtering highlights which products are actually carrying demand in stronger regions, which is more actionable than looking only at total sales.",
            ],
        },
        {
            "title": "Dashboard 3: Product Lifecycle Trends",
            "question": "How do discontinued models continue to sell through dealership channels, and what does that imply for lifecycle planning?",
            "image_url": "/static/images/projects/promotion-demand-analysis/dashboard-3-lifecycle.png",
            "alt": "Promotion Demand Analysis Tableau dashboard for product lifecycle trends",
            "findings": [
                "The lifecycle view shows that discontinued products can still contribute meaningful demand after their main selling window has passed.",
                "Cumulative sales trends help separate models that still have dealership pull from those that are tapering off more quickly.",
                "This page adds a practical planning lens for inventory cleanup, channel prioritization, and end-of-life product decisions.",
            ],
        },
    ],
    "summary": "Together, the three dashboards turn raw promotional sales data into a planning tool: the overview supports quick status checks, the regional/model view helps target inventory and channel effort, and the lifecycle page adds a longer-term view for product allocation decisions.",
}


PROCUREMENT_DASHBOARD_PROJECT_EN = {
    "title": "Procurement Sourcing and Supplier Performance Dashboard",
    "time": "Jan 2026",
    "tags": ["Power BI", "Procurement Analytics", "Supplier Performance"],
    "overview": "This project focuses on procurement management in the EV industry and presents a Power BI dashboard built to support sourcing execution, cost management, and supplier risk monitoring. Based on procurement business logic, I designed a star-schema model with supplier, part, program, and date dimensions, together with sourcing and supplier performance fact tables, to support management reporting and analysis.",
    "process_summary": "The final output includes two core dashboard pages: one centered on sourcing progress and cost achievement, and the other focused on supplier performance, claim impact, and issue diagnosis. Together they support procurement management, supplier management, and project follow-up.",
    "business_questions": [
        "How is sourcing progressing across active programs, and is overall sourcing attainment on track?",
        "Among completed sourcing cases, what share was finished on time, and are there signs of meaningful delay?",
        "Did negotiated costs meet target cost expectations, and which programs or categories are still under pressure?",
        "Which sourcing results contribute most to annualized cost reduction, and how can procurement value be quantified?",
        "Which suppliers are associated with higher claim amounts and quality complaints, and which ones should be tracked more closely?",
        "Which part categories are more likely to create financial loss and performance risk, and where should management attention be prioritized?",
    ],
    "data_source_intro": "The project uses a simulated dataset built around realistic procurement business logic to recreate a typical procurement performance analysis scenario. The data structure follows common fields and KPIs used in sourcing management and supplier performance management.",
    "dimension_tables": [
        {"name": "supplier_dim.xlsx", "description": "Supplier master data, including supplier name, tier, category, province/city, risk level, and payment terms."},
        {"name": "part_dim.xlsx", "description": "Part master data, including part name, category, criticality, single-source flag, and target cost."},
        {"name": "program_dim.xlsx", "description": "Program and vehicle information, including program name, vehicle type, and project phase."},
        {"name": "date_dim.xlsx", "description": "Date dimension used for monthly trend analysis."},
    ],
    "fact_tables": [
        {"name": "sourcing_fact_800.xlsx", "description": "Sourcing fact table containing sourcing status, on-time completion flag, target cost, quotation, negotiated cost, annual demand, and annualized cost reduction."},
        {"name": "supplier_performance_fact_800.xlsx", "description": "Supplier performance fact table containing on-time delivery rate, quality complaints, claim amount, cross-functional score, and performance rating."},
    ],
    "dashboard_intro": "Dashboard Overview",
    "dashboard_sections": [
        {
            "title": "1) Procurement Overview",
            "question": "This page is designed for procurement management and highlights sourcing progress and cost control so the team can quickly assess overall sourcing health.",
            "bullets": [
                "Sourcing attainment rate",
                "On-time sourcing attainment rate",
                "Cost achievement rate",
                "Annualized cost reduction",
                "Monthly sourcing progress trend",
                "Cross-program sourcing progress comparison",
            ],
            "image_url": "/static/images/projects/procurement-dashboard/procurement-overview.png",
            "alt": "Procurement overview dashboard",
            "footer": "This page is mainly meant to answer questions such as how sourcing is progressing, whether procurement targets are being met, and whether cost management is effective.",
        },
        {
            "title": "2) Supplier Performance Overview",
            "question": "This page is designed for supplier management and focuses on identifying higher-risk suppliers, concentrated problem suppliers, and problematic part categories.",
            "bullets": [
                "Average on-time delivery rate",
                "Total number of quality complaints",
                "Total claim amount",
                "Cross-functional composite score",
                "Suppliers with the highest claim amount",
                "Claim amount distribution by part category",
                "Supplier performance detail table",
            ],
            "image_url": "/static/images/projects/procurement-dashboard/supplier-performance-overview.png",
            "alt": "Supplier performance overview dashboard",
            "footer": "This page helps answer which suppliers create the largest issues, which categories carry higher risk, and which suppliers need closer management attention.",
        },
    ],
    "project_highlights": [
        "Designed dimension and fact tables manually based on procurement business logic and built a star schema suitable for Power BI.",
        "Used DAX to define key business metrics across both procurement and supplier performance topics.",
        "Integrated sourcing progress, cost management, and supplier performance into one analytical framework.",
        "Structured the dashboard as a two-page workflow that moves from overall monitoring to issue diagnosis.",
        "The project is well suited as a portfolio case for procurement analytics, supply chain analytics, and Power BI visualization work.",
    ],
    "tech_stack": [
        "Power BI: data modeling, DAX metrics, dashboard development",
        "Python / pandas: simulated data generation and preparation",
        "Excel: storage for dimension and fact tables",
        "Data modeling: star schema, dimension/fact table design, primary-key and foreign-key relationships",
    ],
    "file_notes": [
        {"name": "data/", "description": "Source data and model input tables for the project."},
        {"name": "powerbi/EV_procurement_PowerBI_case.pbix", "description": "Power BI dashboard file."},
        {"name": "visuals/", "description": "Project screenshots used on the page."},
        {"name": "notes/", "description": "Project notes and supporting documentation."},
    ],
    "summary": "This project shows my end-to-end workflow for procurement analytics, from data structure design and business metric definition to final Power BI dashboard delivery. Compared with a standalone charting exercise, the project is more centered on business questions, model design, and management decision support, and reflects my ability to translate procurement logic into analyzable and visualized outputs.",
}


PROMOTION_DEMAND_PROJECT_ZH = {
    "title": "汽车促销期销售洞察：区域需求、渠道表现与产品生命周期",
    "time": "2025年4月 - 2025年5月",
    "tags": ["PostgreSQL", "SQL", "Tableau"],
    "overview": "这个项目围绕促销期间的销售表现展开分析，重点想回答三个问题：第一，不同渠道的销售和交易变化是什么样；第二，不同区域和车型的表现差异在哪里；第三，停产车型在经销商渠道中的生命周期表现如何。",
    "process_summary": "项目底层数据来自 PostgreSQL 数据库。我先从原始业务表中提取销售、客户、产品和经销商相关数据，再用 SQL 做筛选、聚合和字段构造，最后把整理好的分析表导入 Tableau，搭建成 3 个用于业务决策支持的仪表盘页面。",
    "tech_stack": ["PostgreSQL", "SQL", "pgAdmin", "Python", "pandas", "Tableau"],
    "business_questions": [
        "促销期间整体销售表现如何变化？",
        "经销商渠道和线上渠道的表现是否存在明显差异？",
        "销售额主要集中在哪个价格层级？",
        "促销期间销售是否集中在少数头部州，不同车型在重点州中的表现是否存在差异？",
        "停产车型在经销商渠道中的累计销售轨迹有什么不同？",
    ],
    "data_sources": [
        {"name": "sales", "description": "交易级销售记录"},
        {"name": "customers", "description": "客户所在城市和州"},
        {"name": "products", "description": "产品、车型和年份信息"},
        {"name": "dealerships", "description": "经销商覆盖信息"},
    ],
    "data_sources_note": "在此基础上，我整理出了 3 张分析表，分别对应不同的分析主题。",
    "data_work": [
        "关联销售、客户、产品和经销商表",
        "按分析目标筛选特定时间范围",
        "过滤不满足阈值的交易记录",
        "构造 `price_category`、`transaction_year` 等分析字段",
        "计算停产车型的累计销售额",
        "生成适合可视化使用的分析表",
    ],
    "analysis_tables": [
        {
            "name": "city_sales_analysis",
            "description": "用于分析不同年份、渠道、价格层级和产品的销售表现。",
            "fields": ["product_id", "channel", "sales_amount", "price_category", "transaction_year", "sales_transaction_date"],
        },
        {
            "name": "state_model_sales",
            "description": "用于分析促销期间不同州和不同车型的销售表现。",
            "fields": ["state", "model", "total_sales"],
        },
        {
            "name": "cumulative_sales_dealership",
            "description": "用于分析停产车型在经销商渠道中的累计销售趋势。",
            "fields": ["model", "model_year", "product_type", "sales_transaction_date", "total_daily_sales", "cumulative_sales", "model_and_year"],
        },
    ],
    "dashboard_intro": "Tableau 仪表盘展示",
    "dashboard_sections": [
        {
            "title": "仪表盘 1：整体销售概览",
            "question": "这一页主要从总量、数量和销售结构三个角度看促销期间的整体表现。我在这一页放了总销售额、总交易数和平均销售额 3 个 KPI，以及渠道销售额趋势、渠道交易笔数趋势和价格层级销售额对比图。",
            "image_url": "/static/images/projects/promotion-demand-analysis/dashboard-1-overview.png",
            "alt": "Promotion Demand Analysis 仪表板整体销售概览",
            "findings": [
                "2018 年销售额和交易笔数同时达到高点，说明这一阶段的增长并不是单纯由高价订单拉动，而是整体成交活跃度的提升；相应地，2019 年的回落也更像是需求端降温，而不只是价格结构变化。",
                "经销商渠道和线上渠道在走势上基本同步，说明销售波动更可能来自整体市场环境或促销效果变化，而不是单一渠道执行问题。换句话说，2019 年的下滑并不适合只从渠道层面归因。",
                "销售额主要集中在 Premium 价格层级，说明当前收入结构对高价值产品依赖较强。对业务来说，这意味着一旦高价层级成交放缓，总销售额会受到更直接的影响，因此库存保障和渠道资源应优先围绕高价值产品配置。",
                "这一页更像一个经营“体检结果”：先看到总体规模变化，再确认变化同时发生在“金额”和“笔数”两端，最后识别出真正支撑收入的是高价值产品，而不是低价走量。",
            ],
        },
        {
            "title": "仪表盘 2：区域与车型表现分析",
            "question": "这一页主要关注促销期间销售的区域分布情况，以及重点车型在头部州中的表现。我展示了各州销售额总览，并分别筛出了 Lemon 和 Model Chi 销售额最高的前 5 个州，用来观察头部市场是否集中，以及两个车型在重点州中的销售表现是否存在差异。",
            "image_url": "/static/images/projects/promotion-demand-analysis/dashboard-2-region-model.png",
            "alt": "Promotion Demand Analysis 仪表板区域与车型表现",
            "findings": [
                "从各州销售额总览来看，促销期销售明显由少数头部州驱动，说明区域需求分布并不均匀。对业务来说，区域配置的重点不应放在“全国平均铺开”，而应优先锁定贡献更高的重点市场。",
                "Lemon 和 Model Chi 的头部州高度重合，说明这两个车型并不是依赖完全不同的区域市场；换句话说，重点州的识别本身是相对稳定的，真正的差异不在“去哪些州”，而在“同样的重点州里该推什么车型、推多深”。",
                "在相同头部州中，Model Chi 的销售规模显著高于 Lemon，这表明两个车型的差异更多体现在市场渗透深度和销售强度上，而不是区域覆盖范围本身。对资源分配而言，这意味着不能只做到“州级优先级”，还要进一步做到“州内车型优先级”。",
                "这一页最重要的业务启发不是“哪个州高、哪个州低”，而是：重点市场可以先被识别出来，但进入重点市场之后，车型配置不能平均分配，而需要按州内的车型销售深度做差异化投放。",
            ],
        },
        {
            "title": "仪表盘 3：产品生命周期趋势分析",
            "question": "这一页主要分析停产车型在经销商渠道中的累计销售轨迹。我把累计销售趋势图和最终累计销售额对比图放在一起，一张看过程，一张看结果。",
            "image_url": "/static/images/projects/promotion-demand-analysis/dashboard-3-lifecycle.png",
            "alt": "Promotion Demand Analysis 仪表板产品与生命周期趋势",
            "findings": [
                "不同停产车型的累计销售轨迹差异明显，说明即使都已经退出生产，它们在历史销售周期中的贡献也并不相同。这种差异有助于识别哪些车型曾经真正形成规模效应，哪些车型则更像短周期、低沉淀产品。",
                "Model Chi 2014 和 Model Sigma 2015 的累计增长更快、最终累计销售额更高，说明它们不仅卖得更多，而且在销售周期内具备更持续的成交能力。相比之下，这类车型更值得被视为高贡献历史产品，而不是偶然的阶段性热销。",
                "Blade 2014 很早就停止增长，最终累计销售规模也明显偏低，说明其生命周期较短，销售动能衰减更早。对业务复盘来说，这类车型更值得追问的是：问题出在产品吸引力、渠道支持不足，还是销售周期本身就偏短。",
                "这一页的价值不只是比较“谁卖得多”，而是帮助区分：哪些车型在生命周期里形成了持续贡献，哪些车型虽然存在销售记录，但没有建立起长期规模。这类判断更接近真实产品策略复盘，而不只是静态销售排名。",
            ],
        },
    ],
    "summary": "这个项目让我把数据库取数、数据清洗、分析表整理和 Tableau 可视化串成了一整套完整流程。相比只做单张图表，这次更接近真实业务分析场景：先定义问题，再提取数据、整理口径，最后把结果做成可读性更强的仪表盘。",
    "next_steps": [
        "更长时间范围下的趋势观察",
        "更细的区域层级分析",
        "更完整的筛选器和交互设计",
    ],
    "file_notes": [
        {"name": "data/", "description": "清洗后的分析数据表"},
        {"name": "sql/", "description": "用于提取和整理分析表的 SQL"},
        {"name": "visuals/", "description": "仪表盘截图"},
        {"name": "notes/", "description": "项目过程记录"},
        {"name": "tableau/", "description": "Tableau 工作簿文件"},
    ],
}


PROCUREMENT_DASHBOARD_PROJECT_ZH = {
    "title": "采购定点与供应商绩效分析 Dashboard",
    "time": "2026年1月",
    "tags": ["Power BI", "采购分析", "供应商绩效"],
    "overview": "本项目围绕新能源车采购管理场景，构建了一个基于 Power BI 的采购定点与供应商绩效分析仪表板，用于支持采购推进、成本管理和供应商风险监控。项目以采购业务逻辑为基础，搭建了供应商、零件、项目和日期等维表，以及定点事实表和供应商绩效事实表，形成可用于经营分析的星型数据模型。",
    "process_summary": "最终产出包含两个核心仪表板页面：一页聚焦采购定点进展与成本达成情况，另一页聚焦供应商绩效、索赔影响及问题定位，适用于采购管理、供应商管理和项目推进场景。",
    "business_questions": [
        "当前各项目的采购定点推进情况如何，整体定点达成率是否达标。",
        "已完成定点的项目中，按时完成的比例如何，是否存在明显拖期。",
        "谈判后成本是否达到目标成本，哪些项目或品类存在成本压力。",
        "年化降本金额主要来自哪些定点结果，采购工作的业务价值如何量化。",
        "哪些供应商带来了更高的索赔金额和质量投诉，是否需要优先跟踪。",
        "哪些零件品类更容易产生财务损失和绩效风险，管理重点应放在哪里。",
    ],
    "data_source_intro": "本项目数据为基于真实采购业务逻辑构建的模拟数据集，用于还原企业采购经营分析场景。数据结构参考了采购项目管理和供应商绩效管理中的常见字段与指标设计。",
    "dimension_tables": [
        {"name": "supplier_dim.xlsx", "description": "供应商基础信息，包括供应商名称、等级、品类、省市、风险等级、付款账期等"},
        {"name": "part_dim.xlsx", "description": "零件基础信息，包括零件名称、品类、关键程度、单一来源标记、目标成本等"},
        {"name": "program_dim.xlsx", "description": "车型/项目基础信息，包括项目名称、车型类型、项目阶段等"},
        {"name": "date_dim.xlsx", "description": "日期维度，用于月度趋势分析"},
    ],
    "fact_tables": [
        {"name": "sourcing_fact_800.xlsx", "description": "定点事实表，记录定点状态、是否按时完成、目标成本、报价、谈判后成本、年需求量、年化降本金额等"},
        {"name": "supplier_performance_fact_800.xlsx", "description": "供应商绩效事实表，记录交付及时率、质量投诉次数、索赔金额、跨职能评分和绩效等级等"},
    ],
    "dashboard_intro": "仪表板介绍",
    "dashboard_sections": [
        {
            "title": "1）采购项目总览",
            "question": "该页面面向采购管理场景，重点展示采购定点推进与成本控制情况，帮助快速了解整体 sourcing 健康度。",
            "bullets": [
                "定点达成率",
                "按时定点达成率",
                "成本达成率",
                "年化降本金额",
                "月度定点推进趋势",
                "不同项目间的定点推进对比",
            ],
            "image_url": "/static/images/projects/procurement-dashboard/procurement-overview.png",
            "alt": "采购项目总览 Dashboard",
            "footer": "这一页面主要用于回答“项目推进得怎么样”“采购目标完成得如何”“成本管理是否有效”等问题。",
        },
        {
            "title": "2）供应商绩效总览",
            "question": "该页面面向供应商管理场景，重点识别高风险供应商、问题集中供应商及问题品类。",
            "bullets": [
                "平均交付及时率",
                "质量投诉总次数",
                "索赔金额总和",
                "跨职能综合评分",
                "索赔金额最高的供应商",
                "各零件品类对应的索赔金额分布",
                "供应商绩效明细表",
            ],
            "image_url": "/static/images/projects/procurement-dashboard/supplier-performance-overview.png",
            "alt": "供应商绩效总览 Dashboard",
            "footer": "这一页面主要用于回答“问题最大的供应商是谁”“哪些品类风险更高”“哪些供应商需要优先管理”等问题。",
        },
    ],
    "project_highlights": [
        "基于采购业务逻辑手动设计维表与事实表，搭建适用于 Power BI 的星型模型",
        "使用 DAX 构建采购侧与供应商侧关键经营指标",
        "将采购推进、成本管理与供应商绩效整合到同一个分析框架中",
        "通过双页面 dashboard 实现从整体监控到问题定位的分析路径",
        "项目结构清晰，适合作为采购分析、供应链分析和 Power BI 可视化作品集项目展示",
    ],
    "tech_stack": [
        "Power BI：数据建模、DAX 指标、仪表板搭建",
        "Python / pandas：模拟数据生成与整理",
        "Excel：维表与事实表存储",
        "数据建模：Star Schema、维表/事实表设计、主键/外键关系",
    ],
    "file_notes": [
        {"name": "data/", "description": "项目原始数据与建模输入表"},
        {"name": "powerbi/EV_procurement_PowerBI_case.pbix", "description": "Power BI 仪表板文件"},
        {"name": "visuals/", "description": "项目页面截图"},
        {"name": "notes/", "description": "项目说明文档"},
    ],
    "summary": "本项目展示了我在采购分析场景下从数据结构设计、业务指标定义到 Power BI 仪表板落地的完整过程。相比单纯图表展示，这个项目更强调业务问题驱动、模型设计和管理决策支持，体现了我将采购业务逻辑转化为可分析、可视化结果的能力。",
}


TEXAS_SALES_TAX_FORECAST_PROJECT_ZH = {
    "title": "销售税收入预测：支持德州财政规划与决策分析",
    "time": "2025年8月 - 2025年9月",
    "tags": ["R", "时间序列", "ETS", "VAR"],
    "overview": "本项目围绕德州销售税收入预测展开，目标是基于历史财政数据构建时间序列预测模型，对未来 30 个月的销售税收入走势进行测算和趋势判断，为中期财政规划和相关决策分析提供量化依据。",
    "process_summary": "项目基于 R 完成数据读取、时间序列处理、可视化分析、模型建立和结果比较，最终形成以 ETS、ARIMA 和 VAR 思路为核心的预测分析框架，并将预测结果与 Texas Comptroller 官方 FY2025–FY2027 估计进行对比验证。",
    "business_questions": [
        "德州销售税收入的长期趋势和波动特征是什么。",
        "历史销售税序列是否存在明显季节性、异常波动或方差不稳定问题。",
        "在中期财政预测场景下，哪类时间序列模型能够提供更稳定、可解释的预测结果。",
        "预测结果与官方财政估计相比是否具有参考价值。",
        "哪些宏观经济指标可能对销售税收入变化具有解释作用。",
    ],
    "data_sources": [
        {"name": "历史销售税时间序列数据", "description": "课程项目中的德州销售税历史数据，用于构建月度时间序列并完成主要预测分析。"},
        {"name": "Texas Comptroller 官方财政预测数据", "description": "FY2025–FY2027 官方财政估计，用作 benchmark，对比模型预测结果的参考价值。"},
        {"name": "宏观经济指标", "description": "用于 VAR 分析的解释变量，如 vehicle tax、retail trade、unemployment rate 等。"},
    ],
    "methods": [
        "使用 R 读取并整理德州销售税历史数据，构建月度时间序列。",
        "对原始序列进行初步可视化，观察长期趋势、季节性和波动变化。",
        "进行对数变换、节假日调整、异常点处理和哑变量构造，以提高序列稳定性与可解释性。",
        "构建 ETS 与 ARIMA 等单变量时间序列模型，对未来 30 个月销售税收入进行预测。",
        "引入宏观经济指标，建立多变量 VAR 模型，用于分析收入变化的关键驱动因素。",
        "将模型预测结果按 fiscal year 汇总，并与 Texas Comptroller 官方 FY2025–FY2027 估计进行比较。",
    ],
    "results": [
        "项目建立了针对未来 30 个月销售税收入的预测框架。",
        "ETS 模型在中期预测中表现更稳定，并在 FY2026 和 FY2027 与官方估计的比较中显示出更低误差。",
        "模型结果与官方财政估计偏差控制在较小范围内，说明预测结果具有一定政策参考价值。",
        "引入宏观经济变量后，多变量模型能够帮助分析销售税收入变化背后的关键影响因素，并增强结果解释能力。",
    ],
    "output_intro": "可视化 / 模型输出",
    "output_note": "页面中使用的图表素材来自仓库现有的 Team18 项目导出结果，保留了历史趋势、序列处理和预测输出这几类核心内容。",
    "output_sections": [
        {
            "title": "历史销售税趋势图",
            "description": "用于观察历史销售税收入的长期趋势、季节性特征和整体波动变化，是后续序列处理和模型选择的起点。",
            "image_url": "/static/images/projects/team18-termproject/trend-plot.png",
            "alt": "德州销售税历史趋势图",
        },
        {
            "title": "原始序列与变换后序列对比",
            "description": "对比原始序列与变换后序列的表现，用于辅助判断方差稳定性，并说明对数变换和预处理步骤的必要性。",
            "image_url": "/static/images/projects/team18-termproject/original-vs-log-series.png",
            "alt": "原始序列与变换后序列对比图",
        },
        {
            "title": "未来 30 个月预测结果图（ETS）",
            "description": "展示单变量时间序列模型对未来 30 个月销售税收入的预测结果，并用于后续 fiscal year 层面的估计比较。",
            "image_url": "/static/images/projects/team18-termproject/ets-30-month-forecast.png",
            "alt": "ETS 未来 30 个月预测结果图",
        },
        {
            "title": "未来 30 个月预测结果图（VAR）",
            "description": "展示引入宏观经济指标后的多变量预测结果，用于对比不同建模思路在解释能力和预测表现上的差异。",
            "image_url": "/static/images/projects/team18-termproject/var-30-month-forecast.png",
            "alt": "VAR 未来 30 个月预测结果图",
        },
    ],
    "project_highlights": [
        "基于 R 构建完整的时间序列预测流程，从原始序列处理到模型评估形成闭环",
        "同时使用单变量与多变量建模思路，兼顾预测表现与经济解释",
        "将模型输出与官方财政估计进行 benchmark，对结果的现实参考价值进行验证",
        "不仅关注预测数值本身，也关注财政规划场景下的可解释性和稳定性",
    ],
    "tech_stack": [
        "R",
        "forecast",
        "ggplot2 / ggfortify",
        "tsibble / zoo",
        "时间序列建模（ETS、ARIMA、VAR）",
        "数据清洗与特征处理",
    ],
    "file_notes": [
        {"name": "project_materials/Team18-Termproject.html", "description": "原始项目报告与导出结果页面，包含课程项目中的主要分析过程和图表输出。"},
        {"name": "static/images/projects/team18-termproject/", "description": "从原始 HTML 中提取并用于详情页展示的趋势图、序列处理图和预测结果图。"},
    ],
    "summary": "本项目展示了我在财政收入预测场景下，从时间序列清洗、模型建立到结果比较验证的完整分析过程。相比单纯预测数值，本项目更强调预测结果在财政规划和决策分析场景下的可解释性、稳定性和参考价值，体现了我将时间序列建模方法应用到实际政策分析问题中的能力。",
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


@app.route("/en/projects/procurement-dashboard")
def project_procurement_dashboard_en():
    return render_template(
        "project_procurement_dashboard_en.html",
        page_title="Procurement Sourcing and Supplier Performance Dashboard | Jeri Li",
        data=ENGLISH,
        project=PROCUREMENT_DASHBOARD_PROJECT_EN,
    )


@app.route("/en/projects/promotion-demand-analysis")
def project_promotion_demand_en():
    return render_template("project_promotion_demand_en.html", page_title="Promotion Demand Analysis | Jeri Li", data=ENGLISH, project=PROMOTION_DEMAND_PROJECT_EN)


@app.route("/zh")
def home_zh():
    return render_template("index_zh.html", page_title="李今锐 | 数据分析作品集", data=CHINESE)


@app.route("/zh/projects")
def projects_zh():
    return render_template("projects_zh.html", page_title="项目经历 | 李今锐", data=CHINESE)


@app.route("/zh/projects/procurement-dashboard")
def project_procurement_dashboard_zh():
    return render_template("project_procurement_dashboard_zh.html", page_title="采购定点与供应商绩效分析 Dashboard | 李今锐", data=CHINESE, project=PROCUREMENT_DASHBOARD_PROJECT_ZH)


@app.route("/zh/projects/texas-sales-tax-forecasting")
def project_texas_sales_tax_forecasting_zh():
    return render_template(
        "project_texas_sales_tax_forecasting_zh.html",
        page_title="销售税收入预测：支持德州财政规划与决策分析 | 李今锐",
        data=CHINESE,
        project=TEXAS_SALES_TAX_FORECAST_PROJECT_ZH,
    )


@app.route("/zh/projects/promotion-demand-analysis")
def project_promotion_demand_zh():
    return render_template("project_promotion_demand_zh.html", page_title="汽车促销期销售洞察 | 李今锐", data=CHINESE, project=PROMOTION_DEMAND_PROJECT_ZH)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
