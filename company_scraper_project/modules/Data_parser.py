def parse_news(raw_news):
    if not raw_news:
        print("No news data available.")
        return []
    return [headline.strip() for headline in raw_news if headline.strip()]

def parse_leadership(raw_leadership):
    if not raw_leadership:
        print("No leadership data available.")
        return []
    return [{"name": person["name"].strip(), "title": person["title"].strip(), "email": person["email"].strip()} for person in raw_leadership]

def parse_financials(raw_financials):
    if not raw_financials:
        print("No financial data available.")
        return {}
    return {key: value.strip() for key, value in raw_financials.items()}
