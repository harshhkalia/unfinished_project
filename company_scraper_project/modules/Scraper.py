from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_trending_news(driver, company_name):
    news_list = []
    try:
        print("Scraping trending news...")
        driver.get("https://news.google.com/")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(f"{company_name} news")
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load (increased wait time)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".xrnccd"))
        )

        headlines = driver.find_elements(By.CSS_SELECTOR, ".xrnccd .DY5T1d")
        for headline in headlines[:10]:  # Limit to first 10 headlines
            news_list.append(headline.text)
    
    except Exception as e:
        print(f"Error fetching news: {e}")
    
    return news_list

def fetch_leadership_info(driver, company_name):
    leadership = []
    try:
        print("Scraping leadership info from Crunchbase...")

        # Crunchbase search URL (adjust based on company name)
        search_url = f"https://www.crunchbase.com/organization/{company_name.lower().replace(' ', '-')}"
        
        driver.get(search_url)

        # Wait for the page to load completely (increased wait time)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".person-card"))
        )

        # Scrape leadership data from Crunchbase's person cards
        leaders = driver.find_elements(By.CSS_SELECTOR, ".person-card")

        for leader in leaders:
            name = leader.find_element(By.CSS_SELECTOR, ".entity-name").text
            title = leader.find_element(By.CSS_SELECTOR, ".entity-title").text

            # Try to extract email if it exists
            try:
                email = leader.find_element(By.CSS_SELECTOR, "a[href^='mailto:']").get_attribute("href").replace("mailto:", "")
            except:
                email = "Not available"

            leadership.append({"name": name, "title": title, "email": email})

        print(f"Leadership Info: {leadership}")
    
    except Exception as e:
        print(f"Error fetching leadership info: {e}")
    
    return leadership 

def fetch_financial_data(driver, company_name):
    financial_data = {}
    try:
        print("Fetching financial data...")

        company_ticker = company_name.lower().replace(' ', '-')
        url = f"https://finance.yahoo.com/quote/{company_ticker}"

        driver.get(url)

        # Wait for the revenue element to appear (increased wait time)
        try:
            revenue_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//td[@data-test="REVENUE-value"]'))
            )
            revenue = revenue_element.text if revenue_element else 'Not available'
        except Exception as e:
            revenue = 'Not available'
            print(f"Error fetching revenue: {e}")

        # Wait for the future plans/news section to appear
        try:
            news_section = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//section[@class="Mb(15px)"]'))
            )
            future_plans = news_section.find_element(By.TAG_NAME, 'h3').text if news_section else 'No recent plans available'
        except Exception as e:
            future_plans = 'Not available'
            print(f"Error fetching future plans: {e}")

        financial_data = {
            "Revenue": revenue,
            "Future Plans": future_plans
        }

        print(f"Financial Data: {financial_data}")

    except Exception as e:
        print(f"Error fetching financial data: {e}")
    
    return financial_data
