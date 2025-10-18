from research_agent import ResearchAgent
from analysis_agent import AnalysisAgent

class Orchestrator:
    def __init__(self):
        self.research = ResearchAgent()
        self.analysis = AnalysisAgent()

    def generate_report(self, company_name, ticker):
        stock_data = self.research.get_stock_data(ticker)
        news = self.research.get_news(company_name)
        sentiment = self.analysis.analyze_sentiment(news)
        report = f"Report for {company_name}\n\n{sentiment}\n\nRecent News:\n"
        for n in news:
            report += f"- {n}\n"
        return report
