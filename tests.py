# web_server=webdriver.Chrome('chromedriver.exe')
# web_server.get('http://ozumoney.site/showadv.php?rstr=0.27881727922788113')
num_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# amount=browser.find_element_by_id("moneycount")


'''
x = itertools.product(num_1, repeat=4)
for y in x:
    word = ''
    for z in y:
        word += str(z)
    print(word)
'''


def brute_force():
    x = itertools.product(num_1, repeat=4)
    for y in x:
        word = ''
        for z in y:
            word += str(z)
    pass


def clean_amount(amountx):
    list_of_words = amountx.split(' ')
    valuex = float(list_of_words[0])
    return valuex


def clean_element(elementer):
    for lumps in elementer:
        if lumps=='0' or lumps=='1' or lumps=='2' or  lumps=='3' or lumps=='4' or lumps=='5' or lumps=='6' or lumps=='7' or lumps=='8' or lumps=='9':
            return lumps
        else:
           pass
    print("unable to find")

    
    
def full_ops():
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('http://ozumoney.site/showadv.php?rstr=0.5414269350151115')
    z=input('find input text box:')
    input_text_box = browser.find_element_by_name('capcha')
    z=input('find money counter:')
    amounter = browser.find_element_by_id('moneycount')
    z=input('ready...')

    while True:
        time.sleep(2)
        first_element=browser.find_element_by_xpath('//div[@id="cimg1"]//img[@src]')#2292
        first_element_attribute=first_element.get_attribute("src")
        num_1=clean_element(first_element_attribute)
        print('found num 1',num_1)
    
        second_element=browser.find_element_by_xpath('//div[@id="cimg2"]//img[@src]')
        second_element_attribute=second_element.get_attribute("src")
        num_2=clean_element(second_element_attribute)
        print('found num 2',num_2)

        third_element=browser.find_element_by_xpath('//div[@id="cimg3"]//img[@src]')
        third_element_attribute=third_element.get_attribute("src")
        num_3=clean_element(third_element_attribute)
        print('found num 3',num_3)

        fourth_element=browser.find_element_by_xpath('//div[@id="cimg4"]//img[@src]')
        fourth_element_attribute=fourth_element.get_attribute("src")
        num_4=clean_element(fourth_element_attribute)
        print('found num 4',num_4)
        
        full_nums=str(num_1)+str(num_2)+str(num_3)+str(num_4)
        input_text_box.send_keys(int(full_nums))
        input_text_box.send_keys(u'\ue007')
        print('current amount is',amounter.text)
        
    print('uh ooh')

def main():
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('http://ozumoney.site/showadv.php?rstr=0.5414269350151115')
    z=input('find input text box:')
    input_text_box = browser.find_element_by_name('capcha')
    z=input('find button:')
    button = browser.find_element_by_id('opon')
    z=input('find money counter:')
    amounter = browser.find_element_by_id('moneycount')
    z=input('ready...')
    loop=0
    while True:
        loop+=1
        print('looping @',str(loop))
        x = itertools.product(num_1, repeat=4)
        for y in x:
            word = ''
            for z in y:
                word += str(z)

            print('inputting',word)
            input_text_box.send_keys(int(word))
            print('inputed',word)
            print('now submitting')
            #button.click()
            #print('button clicked')
            input_text_box.send_keys(u'\ue007')
            print('submitted')
            if clean_amount(amounter.text) == clean_amount(amounter.text) + 0.1:
                print(word,'successful')
                print('current amount is',amounter.text)
                break
            else:
                print(word,'failed...trying again')
                continue


if __name__ == '__main__':
    import itertools
    import time
    from selenium import webdriver

    full_ops()
