from appium import webdriver

def test(my_user: str, cool_key: str) -> None:
    user=my_user
    key=cool_key
    remote_url=f"https://{user}:{key}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"

    desired_cap = {
        'app': 'storage:0d4db0bf-5a35-4df6-9024-c3264ffafce2',
        'platformName': 'iOS',
        'deviceName': 'iPhone 11.*',
        'automationName': 'XCuiTest',
        'appium:locale': 'en_UK'
    }
    
    driver = webdriver.Remote(remote_url, desired_capabilities=desired_cap)
    driver.implicitly_wait(15)

    driver.quit()

test("my_name", "my_key")