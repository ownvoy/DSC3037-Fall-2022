from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Gls:
    def get_info(self):
        url = "https://kingoinfo.skku.edu/gaia/nxui/index.html?ticket=GVVsR0gJcOQeScyA"
        browser = webdriver.Chrome()
        browser.get(url)
        browser.implicitly_wait(3)
        # 로그인 수동으로 하기
        sleep(13)

        # 학사 -전공 과목으로 이동
        browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[16]/div/div[1]/input",
        ).send_keys("학사-전공")
        browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[16]/div/div[1]/input",
        ).send_keys(Keys.ENTER)
        browser.implicitly_wait(3)
        year = browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[2]/div/div[1]/input",
        )
        sleep(3)
        year.clear()
        sleep(2)
        year.send_keys("2022학년도 1학기")
        sleep(2)

        college = browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[7]/div/div[1]/input",
        )
        sleep(2)
        college.clear()
        sleep(2)
        college.click()
        college.click()
        sleep(2)
        college.send_keys("경영대학")
        sleep(3)
        college.send_keys(Keys.ENTER)
        sleep(4)

        # 대학 선택하기
        major = browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[9]/div/div[1]/input",
        )
        major.click()
        sleep(2)
        major.send_keys(Keys.DOWN)
        sleep(2)
        major.send_keys(Keys.ENTER)
        sleep(5)

        browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[12]/div",
        ).click()
        sleep(3)

        result = []
        for i in range(60):
            table = browser.find_elements(
                By.XPATH,
                "/html/body/div/div[1]/div/div/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div",
            )
            # 정보 가져오기
            print(len(table))
            for tab in table:
                a = tab.text.split("\n")
                result.append(a)
                print(a)
            # 같은 정보 나오면 그만하기
            if i > 5:
                if len(result[-1]) != 1:
                    if result[-1] == result[-6]:
                        break
            # 밑으로 내려가기 (스크롤)
            scroll = browser.find_element(
                By.XPATH,
                "/html/body/div/div[1]/div/div/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div[3]/div/div[2]/div",
            )
            sleep(2)
            for _ in range(10):
                scroll.click()
        return result


gls = Gls()
gls.get_info()
