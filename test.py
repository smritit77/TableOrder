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

# Open the target URL
driver.get("https://testh.tunahms.com/sajha_menu")
sleep(5)

#Test1 = List of occupied
# Locate all elements matching the table title class
# tables = driver.find_elements("xpath", '//div[@class="tableHeader-title OccupiedTable false"]')

# # Loop through each table element and print its text
# for table in tables:
#     table_name = table.text
#     print(table_name)

# Optionally, close the driver after finishing
# driver.quit()

#Test2 = List of unoccupied table
# unoccupied = driver.find_elements("xpath", '//div[@class="tableHeader-title false false"]')

# for table1 in unoccupied:
#     table_unoccupied = table1.text
#     print(table_unoccupied)

# driver.quit()


#click make order
driver.find_element("xpath",'''//*[@id="root"]/section/section[1]/section[2]/div[1]/div/div/button''').click()
sleep(3)

#Euta matra order wala
#click search and search = Sambuca
# driver.find_element("xpath","//input[@placeholder='Search']").click()
# sleep(2)
# figcaptions = driver.find_elements("tag name", 'figcaption')
# # for figcaption in figcaptions:
# #     print(figcaption.text)
# desired_text="Sambuca"
# for figcaption in figcaptions:
#     if figcaption.text.strip() == desired_text:
#         # Click on the parent <figure> element
#         path=f'''//figcaption[text()="{desired_text}"]'''
#         parent_figure = figcaption.find_element('xpath', path)
#         parent_figure.click()
#         sleep(5)
#         break

# #multiple order ko lagi
# desired_texts = ["Sambuca", "Espresso", "Sweet Lassi"]  # List of desired texts
# for text in desired_texts:
#     try:
#         # Locate the <figure> parent of the specific <figcaption> with the desired text
#         figcaption_xpath = f'//figcaption[text()="{text}"]/parent::figure'
#         parent_figure = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, figcaption_xpath))
#         )
#         parent_figure.click()  # Click the parent <figure> element
#         sleep(2)  # Optional pause between clicks for visual confirmation
#         print(f"Clicked on figure with figcaption: {text}")
#     except Exception as e:
#         print(f"Error occurred for text '{text}': {e}")

# # Locate the table element by class name
# cart_table = driver.find_element("xpath", '//div[@class="cartTable"]')  #whole table ko path

# # Find all rows in the table body
# rows = cart_table.find_elements("xpath",'//*[@id="root"]/section/div[2]/div/div/div[3]/div[1]/table/tbody')  ##euta row ko path

# # Loop through each row to increase the quantity
# for row in rows:
#     # Locate all cells in the row
#     quantity_cell = row.find_elements("tag name", "td")   #quantity ko path
    
#     # Select the cell containing the quantity input (assuming it's the third cell, index 2)
#     if len(quantity_cell) > 2:  # Ensure there are enough cells in the row
#         quantity_td = quantity_cell[2]
        
#         # Locate the quantity input within the quantity cell
#         try:
#             quantity_input = quantity_td.find_element("xpath", './/input[@id="exampleForm.ControlInput1"]')  #input ko path
            
#             # Get the current quantity, increment it, and update the field
#             current_quantity = int(quantity_input.get_attribute("value"))
#             new_quantity = current_quantity + 1 # Increment by 1
            
#             # Clear the input and set it to the new quantity
#             quantity_input.clear()
#             quantity_input.send_keys(new_quantity)
#             sleep(1)  # Wait briefly for any UI updates

#         except Exception as e:
#             print("Could not locate the quantity input in this row:", e)

#     else:
#         print("Row does not contain enough cells to locate the quantity cell.")


# Define the list of desired items, increment value, and items to delete
desired_texts = ["Sambuca", "Espresso", "Sweet Lassi", "Kulfi", "Ice Cream Cone", "Ice Cream Fried",
                 "Chicken clear soup", "Veg clear soup", "Cream of tomato soup", "Veg Manchow soup",
                 "Veg Hot and sour soup", "Veg soup", "Bone soup", "Ghundruk ko Jhol",
                 "Chicken Boiled", "Mutton Boiled", "Chicken momo steam", "Chicken momo fry"]
increment_value = 2  # Number to increase quantity by for each item
item_delete = ["Sambuca", "Espresso"]  # Items to delete

# Step 1: Add each desired item to the cart
for text in desired_texts:
    try:
        # Find and click the <figure> element for each desired item
        figcaption_xpath = f'//figcaption[text()="{text}"]/parent::figure'
        parent_figure = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, figcaption_xpath))
        )
        parent_figure.click()
        sleep(2)  # Optional pause for visual confirmation
    except Exception as e:
        print(f"Error occurred for item '{text}': {e}")

# Step 2: Locate the cart table to find, adjust quantities, or delete items
cart_table = driver.find_element(By.XPATH, '//div[@class="cartTable"]')  # Locate the cart table

# Get all rows in the cart table body
rows = cart_table.find_elements(By.XPATH, '//*[@id="root"]/section/div[2]/div/div/div[3]/div[1]/table/tbody/tr')

# Step 3: Loop through each row in the cart to process quantities and deletions
for row in rows:
    # Locate all cells within the row
    cells = row.find_elements(By.TAG_NAME, "td")
    
    # Ensure the row has enough cells (assuming item name is in the second cell)
    if len(cells) > 2:
        item_name = cells[1].text  # Get the item name from the appropriate cell
        
        # Check if the item name is in the increment list
        if item_name in desired_texts:
            quantity_td = cells[2]  # Quantity cell (adjust index if needed)

            try:
                # Locate the quantity input field within the quantity cell
                quantity_input = quantity_td.find_element(By.XPATH, './/input[@id="exampleForm.ControlInput1"]')
                
                # Get current quantity, add increment, and set the new quantity
                current_quantity = int(quantity_input.get_attribute("value"))
                new_quantity = current_quantity + increment_value
                
                # Clear and update the quantity input field with the new quantity
                quantity_input.clear()
                quantity_input.send_keys(str(new_quantity))
                sleep(1)  # Brief pause to allow for UI update
                print(f"Incremented quantity for '{item_name}' to {new_quantity}")
            except Exception as e:
                print(f"Could not locate quantity input for '{item_name}': {e}")

            if item_name in item_delete:
                try:
                   # Locate the delete button within the row (inside the last cell or specific column)
                  delete_button = cells[-1].find_element("xpath", '//*[@id="root"]/section/div[2]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[6]')  # Adjust XPath if needed
                  delete_button.click()  # Click the delete button to remove the item
                  sleep(1)  # Pause for the UI to update
                  print(f"Deleted item: {item_name}")
                except Exception as e:
                   print(f"Could not delete item '{item_name}': {e}")
            continue  # Skip further processing for this item

    else:
        print("Row does not contain enough cells to locate the item name or quantity cell.")
driver.find_element("xpath",'//*[@id="root"]/section/div[2]/div/div/div[3]/div[2]/button').click()





