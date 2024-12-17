import pandas as pd
import os

def save_to_excel(data, company_name):
    try:
        if not os.path.exists('output'):
            os.makedirs('output')
        
        df_news = pd.DataFrame(data["news"], columns=["News"])
        df_leadership = pd.DataFrame(data["leadership"], columns=["Name", "Position", "Email"])
        df_financials = pd.DataFrame(data["financials"], index=[0])

        with pd.ExcelWriter(f"output/{company_name}_data.xlsx") as writer:
            df_news.to_excel(writer, sheet_name="News", index=False)
            df_leadership.to_excel(writer, sheet_name="Leadership", index=False)
            df_financials.to_excel(writer, sheet_name="Financials", index=False)

        print(f"Data saved successfully at output/{company_name}_data.xlsx")
    except Exception as e:
        print(f"Error saving data to Excel: {e}")

