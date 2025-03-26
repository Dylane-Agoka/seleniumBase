from seleniumbase import Driver
# Initialize the driver with UC mode enabled in GUI mode
driver = Driver(uc=True, headless=False)
# Set the target URL
url = "https://ifcameroun.extranet-aec.com/examinations/examination_type_detail?examinationTypeId=4"
# Open the URL using UC mode
driver.uc_open_with_reconnect(url, reconnect_time=6)
# Wait for the challenge to complete
driver.sleep(15)
# Take a screenshot to verify the result
driver.save_screenshot("cloudflare-challenge.png")
# Close the driver
driver.quit()