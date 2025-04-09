# LAB-08: ERD Diagram

## Purpose

This report presents an Entity Relationship Diagram (ERD) using MermaidJS to define how raw weekly gainer stock data is transformed into structured intermediate and final tables. The goal is to make data processing and querying efficient for analysis — especially for identifying repeated stock symbols and analyzing price trends or volume fluctuations.

---

## Use Cases

1. **Recurring Stock Symbols**  
   Identify which stock symbols appear most frequently across all weekly gainer files. This can help determine which stocks are consistently performing or trending.

2. **Price Range Distribution**  
   Compute the price range and average closing price per symbol to understand volatility and trends over time.

3. **Volume Trends**  
   Analyze how trading volume changes across weeks for selected stocks, which can hint at market sentiment or reactions to news.

---

## ERD Diagram

```mermaid
erDiagram
    RAW_GAINERS ||--o{ WEEKLY_SYMBOLS : contains
    WEEKLY_SYMBOLS ||--o{ SYMBOL_STATS : describes
    SYMBOL ||--o{ SYMBOL_STATS : summarized_in
    SYMBOL ||--o{ CANDLE_DATA : has_prices
    SYMBOL ||--o{ FINAL_TABLE : aggregated_to
    SYMBOL_STATS ||--o{ FINAL_TABLE : contributes

    RAW_GAINERS {
        string file_name
        date week_start
    }

    WEEKLY_SYMBOLS {
        string symbol
        date date_added
    }

    SYMBOL_STATS {
        string symbol
        int frequency
        string dates_appeared
    }

    CANDLE_DATA {
        string symbol
        date date
        float open
        float close
        float high
        float low
        int volume
    }

    FINAL_TABLE {
        string symbol
        int frequency
        float avg_price
        float price_range
        float avg_volume
    }
