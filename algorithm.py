from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# This commented code was my prototype algorithm without using a web script
# In order to see if my algorithm works on its own, then implement automated web script

# def guess_bar(bars_info: dict):
#     # Initially, I was going to use a forEach loop to iterate through the dictionary
#     # for bar, val in bars_info.items():

#     #     # print(f"bar {bar}: {val} grams")

#     # Variables to track left and right sides, as well as index of loop
#     left_scale, right_scale = 0, 0
#     bar_index = 0

#     while(bar_index < 8):
#         # Add first bar in iteration to left scale
#         left_scale += bars_info[bar_index]
#         bar_index+=1

#         # Add second bar in iteration to right scale
#         right_scale += bars_info[bar_index]
#         bar_index+=1

#         # Whichever side is less, is the fake bar 
#         if(left_scale < right_scale):
#             print(f"The fake bar is #{bar_index-2} weighing {bars_info[bar_index-2]} grams.")
#             return
#         elif(left_scale > right_scale):
#             print(f"The fake bar is #{bar_index-1} weighing {bars_info[bar_index-1]} grams.")
#             return
    
#     # By the end of loop if no fake bar was found, then it must be the last one.
#     print(f"The fake bar is #8 weighing {bars_info[8]} grams.")

    

def main():
    # Code to start WebDriver for automated web script
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                options=options)
    driver.get("http://sdetchallenge.fetch.com")
    driver.maximize_window()

    set_index = 0
    counter = 0

    # We have 4 sets of numbers to test (9 bars / 2 sides of scale (rounded down))
    while(set_index < 4):
        # Find left input element and send input
        left_element_ID = "left_" + str(set_index)
        first_entry = driver.find_element(By.ID, left_element_ID)
        first_entry.send_keys(str(counter))
        counter+=1

        #Find right input element and send input
        right_element_ID = "right_" + str(set_index)
        second_entry = driver.find_element(By.ID, right_element_ID)
        second_entry.send_keys(str(counter))
        counter+=1

        # After inputting numbers, click Weigh button
        weigh_button = driver.find_element(By.ID, "weigh")
        weigh_button.click()
        time.sleep(4)

        # Parse text to find either =, <, or >
        result_elements = driver.find_elements(By.CLASS_NAME, "result")
        result = result_elements[0].text
        print("result ", result)

        if '>' in result:
            # The original number is counter-1 because we incremented counter by 1 before
            fake_bar = "coin_" + str(counter-1)
            break
        elif '<' in result:
            # The original number is counter-2 because we incremented counter by 2 before
            fake_bar = "coin_" + str(counter-2)
            break
        else:
            # If reached end and fake not found, it must be last one
            fake_bar = "coin_" + str(counter)

        set_index += 1

    # print("fake_bar", fake_bar)
    answer_button = driver.find_element(By.ID, fake_bar)
    answer_button.click()
    print(f"The fake one is {fake_bar}")

if __name__ == "__main__":
    main()