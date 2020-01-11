# Mortgage Payment Calculator

> 按揭贷款计算器

## 使用说明

- 查看帮助请执行: `python mortgage-payment-calculator/calculate.py --help`
- 安装依赖： `pip install -r requirements.txt`

## 示例

```shell
# 一年期 12 万贷款，年利率 4.8%，等额本金方式，每月偿还明细
python mortgage-payment-calculator/calculate.py --loan_amount 120000 --interest_rate 0.048 --years 1 --payment_type 'equal-principal-payment'
```
