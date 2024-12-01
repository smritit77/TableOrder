from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome profile for persistent login
profile_directory = "C:\\Users\\Hp\\AppData\\Local\\Google\\Chrome\\User Data"
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={profile_directory}")
options.add_argument('--profile-directory=Default')

# Initialize driver
driver = webdriver.Chrome(options=options)
sleep(5)

try:
    # Open the target URL
    driver.get("https://testh.tunahms.com/sajha_menu")
    sleep(5)

    #order gareko table ko path
    driver.find_element("xpath", '//*[@id="root"]/section/section[1]/section[2]/div[1]/div').click()
    sleep(5)

    #whole table ko path
    whole_table = driver.find_element("xpath", '//div[@class="billAreaRight"]')

    #customer search input field inside the searchHolder
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("xpath", '//input[@placeholder="Search customer\'s name or phone number"]'))
    )

    #List of customer names or numbers to search
    search_terms =["Smriti Thapa"] # Add your search terms here
    for search_term in search_terms:
        # Clear the input field before entering a new search term

        xpath_of_select_customer=f'''//li[@data-id="{search_term}"]'''
        
        search_input.clear()
        sleep(3)
        search_input.send_keys(search_term)
        sleep(5)
        driver.find_element("xpath", xpath_of_select_customer).click()
        print(f"Searching for: {search_term}")
        sleep(3)


    # List of items you want to search for dynamically
    items_to_search = ["Sweet Lassi", "Kulfi","Ice Cream Cone","Ice Cream Fried","Chicken clear soup","Veg clear soup"]  # Add more items here as needed

    for item_name in items_to_search:
        # Dynamically generate the XPath for the item
        xpath_for_item = f'//div[@class="billItemWrapper"]/div/div[text()="{item_name}"]'

        try:
            # Find the item element
            item_element = driver.find_element("xpath", xpath_for_item)
            print(f"Item found: {item_element.text}")
        except Exception as e:
            print(f"Item '{item_name}' not found. Error: {e}")

    # Select the table after searchings
    # Specify the value you want to find in the table
    target_value = "477.87"

   # Maximum number of rows and columns
    max_rows = 1  # Adjust based on the number of rows in the table
    max_columns = 3  # Adjust based on the number of columns in the table

   # Flag to track if the value is found
    value_found = False

    # Loop through each row
    for row_index in range(1, max_rows + 1):  # XPath indexing starts at 1
        for col_index in range(1, max_columns + 1):  # Loop through each column
            try:
               # Dynamically generate XPath for the current cell
               xpath = f"//table//tr[{row_index}]/td[{col_index}]"
            
               # Find the cell using Selenium
               cell = driver.find_element("xpath", xpath)
            
               # Retrieve the cell value
               cell_value = cell.text.strip()
            
                # Check if the cell value matches the target value
               if cell_value == target_value:
                    print(f"Target Value Found - Row: {row_index}, Column: {col_index}, Value: {cell_value}")
                    value_found = True
                    break  # Exit the inner loop once the value is found

            except Exception as e:
                 # Handle cases where an element is not found
                print(f"Element not found at Row {row_index}, Column {col_index}. Error: {e}")

                if value_found:
                    break  # Exit the outer loop once the value is found

                # If the value is not found, print a message
                if not value_found:
                    print(f"Value '{target_value}' not found in the table.")


except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()




