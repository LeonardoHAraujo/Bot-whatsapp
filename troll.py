from selenium import webdriver
import time

class WhatsappBot:
	def __init__(self):
		self.message = "Amor esse é o troll do código. Isso ta sendo enviado de um bot que eu fiz e ele não vai parar kkkk beijo, TE AMO!"
		self.groups = ["Michelle"]
		options = webdriver.ChromeOptions()
		options.add_argument('lang=pt-br')
		self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

	def SendMessage(self):
		# <span dir="auto" title="Lembrete" class="_1hI5g _1XH7x _1VzZY">Lembrete</span>
		# <div tabindex="-1" class="DuUXI">
		# <span data-testid="send" data-icon="send" class="">

		self.driver.get('https://web.whatsapp.com')
		time.sleep(20)

		for group in self.groups:
			chat = self.driver.find_element_by_xpath(f"//span[@title='{group}']")
			time.sleep(3)
			chat.click()

			chatBox = self.driver.find_element_by_class_name('DuUXI')
			time.sleep(3)
			chatBox.click()
			chatBox.send_keys(self.message)

			btn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
			time.sleep(3)
			btn.click()

			time.sleep(3)
			self.looper()

	def looper(self):
		while True:
			chatBox = self.driver.find_element_by_class_name('DuUXI')
			time.sleep(3)
			chatBox.click()
			chatBox.send_keys(self.message)

			btn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
			time.sleep(3)
			btn.click()
		

bot = WhatsappBot()
bot.SendMessage()