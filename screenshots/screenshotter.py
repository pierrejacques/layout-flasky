from selenium import webdriver

def filename_sanitizor(str):
  a = str.replace('http://', '')
  a = a.replace('https://', '')
  a = a.replace('.', '_')
  a = a.replace('+', '_')
  a = a.replace('/', '_')
  a = a.replace('?', '_')
  a = a.replace(':', '_')
  return a

def capture(url):
  print('    ... capturing screenshot')
  file_name = filename_sanitizor(url) + '.png'
  browser = webdriver.Chrome('/chromedriver') # Get local session of chrome
  browser.set_window_size(1200, 900)
  browser.get(url) # Load page
  browser.save_screenshot(file_name)
  browser.close()
  print('    ... captured! save to %s' % file_name)
  return file_name

if __name__ == "__main__":
  capture("http://jinchenhao.phonicavi.com")
