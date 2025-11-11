
# DAY 48!!
# CHALLENGE: CREATE A AUTOMATED AND Ultimate Cookie Clicker PLAYING BOT!!!!

#----------Imports------------
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep, time
import csv
import re

print("🚀 Launching Stealth Cookie Clicker Bot...")

options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


#----------Inital page load--------------------
print("⌛ Waiting for game to load...")
wait = WebDriverWait(driver, 20)

try:
  language_button = wait.until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
  language_button.click()
  print("✅ English language selected.")
  
except TimeoutException:
  print("⚠️ Language selector not found, continuing...")
  
# Wait for main game interface....
wait.until(EC.presence_of_all_elements_located((By.ID, "bigCookie")))
print("🍪 Game loaded successfully!!")

sleep(3) # Small delay for animations...

#-----------Game elements-----------
cookie = driver.find_element(By.ID, "bigCookie")
cookie_display = driver.find_element(By.ID, "cookies")

#-----------CSV logger setup---------
with open ("cookie_progress.csv", "w", newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["Time (s)", "Cookies"])
  
#-------------Bot------------
start_time = time()
check_interval = 5 # seconds between store checks..
next_check = time() + check_interval
run_duration = 60 * 5 # run for 5 minutes..
end_time = start_time + run_duration

#-----------Main loop --------------
try:
  while True:
    #---Click Cookie--
    cookie.click()
    
    #--Click golden cookie is found..
    try:
      golden_cookie = driver.find_element(By.CSS_SELECTOR, ".shimmer")
      golden_cookie.click()
      print("✨ Clicked a Golden Cookie!!")
      
    except NoSuchElementException:
      pass
    
    #------Every 5 Seconds: Buy items
    if time() > next_check:
      try:
        # Extrct cookie count safely..
        cookie_text = cookie_display.text
        cookie_numbers = re.findall(r"[\d,]+", cookie_text)
        cookie_count = int(cookie_numbers[0].replace(",", ""))if cookie_numbers else 0
        
        # Fing all available store items
        products =  driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled")
        
        if products:
          #---Buy the most expensive available product
          best_item = products[ -1]
          best_item_id = best_item.get_attribute("id")
          best_item.click()
          print(f"🛒 Bought upgrade: {best_item_id}")
          
        # Find available upgrades (top now)
        upgrades = driver.find_elements(By.CSS_SELECTOR, "div.upgrade.enabled")
        for upgrade in upgrades:
          upgrade.click()
          print("⚙️ Bought an upgrade!!")
          
        # Log progress to csv..
        with open ("cookie_progress.csv", "a", newline="") as file:
          writer = csv.writer(file)
          writer.writerow([round(time() - start_time, 2), cookie_count])
          
      except Exception as e:
        print(f"⚠️ Error during store check: {e}")
        
      next_check = time() + check_interval# Reset timer..
      
    if time() > end_time:
      final_count = cookie_display.text
      print(f"\n🎉 Time's up! Final Cookie Count: {final_count}")
      break
      
except KeyboardInterrupt:
  print("\n🛑 Bot manually stopped by user.")
  
finally:
  print("💾 Saving progress and closing browser...")
  driver.quit()
  print("✅ Browser closed. Goodbey Cookie Master! 🍪")
