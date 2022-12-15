from appium import webdriver
from appium.options.ios import XCUITestOptions

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

def test_1(my_user: str, cool_key: str) -> None:
    user=my_user
    key=cool_key
    remote_url=f"https://{user}:{key}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"

    options = XCUITestOptions
    options.platformName = "iOS"
    options.platformVersion="14"
    options.deviceName="iPhone 11.*"
    options.app="storage:0d4db0bf-5a35-4df6-9024-c3264ffafce2"
    options.locale="en_UK"


    driver = webdriver.Remote(remote_url, options=options)
    driver.implicitly_wait(15)

    driver.quit()

test("my_name", "my_key")
test_1("my_name", "my_key")