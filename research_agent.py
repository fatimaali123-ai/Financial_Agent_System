import yfinance as yf

class ResearchAgent:
    def get_stock_data(self, ticker):
        stock = yf.Ticker(ticker)
        data = stock.history(period="5d")
        return data

    def get_news(self, company_name):
        # Temporary fake news for testing
        return [
            f"{company_name} launches new product!",
            f"{company_name} stock prices rise 5%",
            f"Analysts predict strong future for {company_name}"
        ]
