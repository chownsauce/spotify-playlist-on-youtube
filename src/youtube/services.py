from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.youtube.clients import PlaylistClient
from src.youtube.factories import VideoFactory


class Browser:

	def __init__(self):
		self.driver = webdriver.Chrome()
		self.wait = WebDriverWait(self.driver, 15)


def login_in_youtube(browser, email, password):
	browser.driver.get('https://youtube.com')
	login_url = 'https://accounts.google.com/ServiceLogin?'
	login_button = browser.wait.until(
		EC.visibility_of_element_located((By.XPATH, f'//a[contains(@href, "{login_url}")]')))
	login_button.click()

	email_field = browser.wait.until(
		EC.visibility_of_element_located((By.XPATH, f'//input[@type="email"]')))
	email_field.send_keys(email)
	browser.driver.find_element_by_xpath('//span[contains(text(), "Next")]//ancestor::button[1]').click()

	password_field = browser.wait.until(
		EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]')))
	password_field.send_keys(password)
	browser.driver.find_element_by_xpath('//span[contains(text(), "Next")]//ancestor::button[1]').click()
	
	browser.wait.until(EC.visibility_of_element_located((By.ID, 'img')))


def create_playlist(email, password, playlist_name, search_items):
	browser = Browser()
	login_in_youtube(browser, email, password)

	for item in search_items:
		browser.driver.get(f'https://www.youtube.com/results?search_query={item}')
		browser.wait.until(
			EC.visibility_of_element_located((By.ID, 'video-title'))).click()
		

		save_button = browser.wait.until(
			EC.visibility_of_element_located((By.XPATH, '//a//yt-formatted-string[contains(text(), "Salvar")]'))
		)
		save_button.click()
		
		try :
			browser.wait.until(
				EC.visibility_of_element_located((By.XPATH, '//yt-formatted-string[contains(text(), "AUTOPLAYLIST")]'))
			).click()
		except TimeoutException:
			browser.driver.find_element_by_xpath('//yt-formatted-string[contains(text(), "Create new")]').click()

			playlist_input = browser.wait.until(
				EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Enter playlist name..."]')))
			playlist_input.send_keys(f'AUTOPLAYLIST - {playlist_name}')

			browser.driver.implicitly_wait(5)
			browser.driver.find_element_by_xpath('//a//paper-button[@aria-label="Create"]').click()
		
			browser.driver.implicitly_wait(5)

	browser.driver.close()