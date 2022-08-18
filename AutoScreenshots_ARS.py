from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import img2pdf

def save_screenshots(selection):

    with open("list_urls.txt") as file:
        for line in file:
            URL = line

            if selection == "1":
                format = ".png"
            else:
                format = ".jp2"

            mod_line = line.replace("/", "").replace(".html", "").replace(".", "").replace(
                "https", "").replace("http", "").replace(":", "").replace("www", "")
            file_name = path + "/output/" + mod_line.strip() + format
            print(file_name)
            options = webdriver.ChromeOptions()
            options.headless = True
            options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            driver.get(URL)
            def S(X): return driver.execute_script(
                'return document.body.parentNode.scroll'+X)
            driver.set_window_size(S('Width'), S('Height'))
            driver.find_element(By.TAG_NAME, 'body').screenshot(file_name)

    driver.quit()

def convert_img_pdf():

    for filename in os.listdir(output_path):
        f_img = os.path.join(output_path, filename)
        if os.path.isfile(f_img):

            result = f_img[f_img.rindex('.')+1:]
            print(result)
            if result == "jp2":
                f_out = f_img.removesuffix(".jp2") + ".pdf"
                print(f_img, f_out)
                with open(f_out, "wb") as f:
                    f.write(img2pdf.convert(f_img))
                os.remove(f_img)

if __name__ == "__main__":

    path = os.getcwd()
    output_path = path + "/output/"
    if os.path.exists(output_path):
        print("Dir exists")
    else:
        os.makedirs(output_path)

    selection = input(
        "Would you like to convert URLs to images/PDFs? Input 1 to select images; Input 2 to select PDFs\n")
    while selection != '1' and selection != '2':
        print('Invalid input')
        selection = input(
            "Would you like to convert URLs to images/PDFs? Input 1 to select images; Input 2 to select PDFs\n")
    save_screenshots(selection)

    if selection == "2":
        convert_img_pdf()
