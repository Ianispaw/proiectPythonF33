import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def download_song(song_name):

    search_link = 'https://www.youtube.com/results?search_query=' + song_name
    driver.get(search_link)

    time.sleep(1)

    PLAY_primul_video = driver.find_element('xpath',
                                            '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a')
    PLAY_primul_video.click()
    primul_link = driver.current_url
    driver.get('https://ytmp3.nu/l0uU/')
    #/Users/ianispaunoiu/Desktop/facultate/python33/seleniumpythonProject1/reading.txt
    #in reading txt e o lista cu melodii scrise in formatul: "michael jackson - beat it" cate una pe rand

    SEARCH_BOX = driver.find_element('xpath',
                                     '//*[@id="url"]')
    SEARCH_BOX.send_keys(primul_link)

    LUPA = driver.find_element('xpath',
                               '/html/body/form/div[2]/input[2]')
    LUPA.click()

    time.sleep(2)

    DOWNLOAD = driver.find_element('xpath',
                                   '/html/body/form/div[2]/a[1]')
    DOWNLOAD.click()

    time.sleep(2)
    #inchidem fereastra cu reclama
    all_window_handles = driver.window_handles
    current_window_handle = driver.current_window_handle
    for window_handle in all_window_handles:
        if window_handle != current_window_handle:
            driver.switch_to.window(window_handle)
            driver.close()

    driver.switch_to.window(current_window_handle)


path  = '/Users/ianispaunoiu/Desktop/facultate/python33/seleniumpythonProject1/reading.txt'

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get('https://www.youtube.com/')
driver.maximize_window()
BUTON_accept_cookie = driver.find_element('xpath',
                                               '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
BUTON_accept_cookie.click()

time.sleep(2)

with open(path, 'r') as file:
    for line in file:
        download_song(line)
time.sleep(5)
driver.close()
print('procesul de descarcare a fost terminat cu succes. fisierele descarcate se afla in folderul "Downloads".')
