# EV Procurement & Supplier Performance Dashboard

A Power BI dashboard project built around a simulated EV procurement business case. The project focuses on sourcing execution, cost achievement, annualized savings, and supplier performance monitoring.

## Project Overview

This project simulates a procurement management scenario in the new energy vehicle industry and translates it into a business-oriented Power BI dashboard.

I designed a star-schema data model with supplier, part, program, and date dimensions, then built two fact tables to track sourcing outcomes and supplier performance. Based on this model, I created a two-page dashboard to support procurement progress tracking, cost control, and supplier risk identification.

The dashboard is structured to answer practical business questions such as:
- Are sourcing activities progressing on schedule?
- Are negotiated costs meeting target costs?
- Which suppliers contribute the most financial impact through claims?
- Which part categories are associated with higher supplier-related losses?

## Business Problem

Procurement teams need a structured way to monitor sourcing progress, evaluate cost execution, and identify supplier risks before they materially affect project timelines or operating performance.

Without a centralized dashboard, sourcing status, cost achievement, and supplier issues are often scattered across multiple files and functions, making it difficult to:
- track sourcing completion across programs
- measure whether negotiated costs meet target costs
- quantify annualized savings
- identify suppliers with the highest claims and complaint exposure
- prioritize part categories that require closer management attention

This project addresses those issues by turning procurement and supplier data into a compact management dashboard.

## Data Source

The dataset used in this project is a **business-logic-driven simulated dataset** designed to resemble a realistic procurement and supplier management environment.

### Dimension tables
- `supplier_dim.xlsx`
- `part_dim.xlsx`
- `program_dim.xlsx`
- `date_dim.xlsx`

### Fact tables
- `sourcing_fact_800.xlsx`
- `supplier_performance_fact_800.xlsx`

The data model was built to reflect a typical procurement reporting structure:
- supplier information
- part and commodity structure
- vehicle program and launch phase
- sourcing status and cost outcomes
- supplier delivery and quality performance

## Dashboard Pages

## 1. Procurement Overview
This page focuses on sourcing progress and cost execution.

Key KPIs:
- Sourcing Attainment Rate
- On-Time Sourcing Rate
- Cost Achievement Rate
- Annual Saving Amount

Main visuals:
- Monthly Sourcing Attainment Trend
- Sourcing Attainment Rate by Program

This page is intended to help answer:
- How far has sourcing progressed?
- Are sourcing activities being completed on time?
- Are target costs being achieved?
- What is the business value of sourcing execution in terms of annualized savings?

## 2. Supplier Performance
This page focuses on supplier performance and issue prioritization.

Key KPIs:
- Avg On-Time Delivery Rate
- Total Quality Complaints
- Total Claim Amount
- Avg Cross-Functional Score

Main visuals:
- Top 10 Suppliers by Claim Amount
- Claim Amount by Part Category
- Supplier Performance Detail table

This page is intended to help answer:
- Which suppliers create the largest financial impact?
- Which part categories are associated with higher claim exposure?
- Which suppliers require closer follow-up based on delivery, complaints, and cross-functional evaluation?

## Data Model

This project uses a **star schema**.

### Dimensions
- `supplier_dim`
- `part_dim`
- `program_dim`
- `date_dim`

### Facts
- `sourcing_fact_800`
- `supplier_performance_fact_800`

The model was built to support scalable KPI calculation and clean drill-down analysis across programs, parts, suppliers, and time.

## Key Measures

Examples of dashboard measures include:
- Sourcing Attainment Rate
- On-Time Sourcing Rate
- Cost Achievement Rate
- Annual Saving Amount
- Avg On-Time Delivery Rate
- Total Quality Complaints
- Total Claim Amount
- Avg Cross-Functional Score

## Tools Used

- **Power BI** for data modeling, DAX, and dashboard development
- **Python / pandas** for generating and structuring simulated business data
- **Excel** for storing dimension and fact tables

## File Structure

```text
CASE/
├── data/
│   ├── date_dim.xlsx
│   ├── part_dim.xlsx
│   ├── program_dim.xlsx
│   ├── sourcing_fact_800.xlsx
│   ├── supplier_dim.xlsx
│   └── supplier_performance_fact_800.xlsx
├── notes/
├── powerbi/
│   └── EV_procurement_PowerBI_case.pbix
├── visuals/
│   ├── 采购项目总览.png
│   └── 供应商绩效总览.png
└── README.md
