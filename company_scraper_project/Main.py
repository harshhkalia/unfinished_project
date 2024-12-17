from modules.Scraper import fetch_trending_news, fetch_leadership_info, fetch_financial_data
from modules.Data_parser import parse_news, parse_leadership, parse_financials
from modules.File_generator import save_to_excel
from utils.Helpers import setup_driver

def main():
    company_name = input("Enter the company name: ")

    driver = setup_driver()

    try:
        print(f"Scraping data for {company_name}...")

        raw_news = fetch_trending_news(driver, company_name)
        print(f"Trending News: {raw_news}") 

        raw_leadership = fetch_leadership_info(driver, company_name)
        print(f"Leadership Info: {raw_leadership}") 

        raw_financials = fetch_financial_data(driver, company_name)
        print(f"Financial Data: {raw_financials}")

        news = parse_news(raw_news)
        leadership = parse_leadership(raw_leadership)
        financials = parse_financials(raw_financials)

        if not news or not leadership or not financials:
            print("Some data is missing, not saving to Excel.")
            return

        data = {
            "news": news,
            "leadership": leadership,
            "financials": financials
        }

        print(f"Parsed Data: {data}")

        save_to_excel(data, company_name)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
